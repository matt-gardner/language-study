#!/usr/bin/env python

from django import forms
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.utils import simplejson

from datetime import datetime

from language_study.drills.models import Word, WordList, Tag, Verb
from language_study.drills.views.filters import filter_words


def logout(request):
    logout_user(request)
    return HttpResponseRedirect('/')


def base_context(request):
    context = RequestContext(request)
    if isinstance(request.user, AnonymousUser):
        context['logged_in'] = False
    else:
        context['logged_in'] = True
    errors = request.session.get('errors', None)
    if errors:
        if isinstance(errors, list):
            context['errors'] = errors
        else:
            context['errors'] = [errors]
        del request.session['errors']
    return context


# Tag stuff
###########

def add_tag(request, listname, next_url):
    name = request.POST['name']

    wordlist = WordList.objects.get(name=listname)
    tag = Tag(name=name, wordlist=wordlist)
    tag.save()
    return HttpResponseRedirect(next_url)


def add_tag_to_word(request, listname, tag):
    wordlist = WordList.objects.get(name=listname)
    tag = wordlist.tag_set.get(name=tag)
    word = wordlist.word_set.get(pk=request.session['word-id'])
    word.tags.add(tag)
    ret_val = dict()
    ret_val['tags'] = render_tags(word.tags.all())
    return HttpResponse(simplejson.dumps(ret_val))


def remove_tag_from_word(request, listname, tag):
    wordlist = WordList.objects.get(name=listname)
    tag = wordlist.tag_set.get(name=tag)
    word = wordlist.word_set.get(pk=request.session['word-id'])
    word.tags.remove(tag)
    ret_val = dict()
    ret_val['tags'] = render_tags(word.tags.all())
    return HttpResponse(simplejson.dumps(ret_val))


def render_tags(tags):
    tags = list(tags)
    string = u''
    if not tags:
        return u'This word has no tags'
    string += u'<table>'
    for tag in tags:
        string += u'<tr>'
        string += u'<td>'
        string += tag.name
        string += u'</td>'
        string += u'<td></td><td></td><td></td><td></td>'
        string += u'<td class="remove" onclick="remove_tag(\'%s\')">' % tag.name
        string += 'X'
        string += u'</td>'
        string += u'</tr>'
    string += u'</table>'
    return string


# Other general methods
#######################

def devariablize(string):
    return ' '.join([s.capitalize() for s in string.split('_')])


# Classes that help out with things
###################################

class AjaxWord(object):
    def __init__(self, word):
        self.word = word.word
        self.definition = word.definition
        self.difficulty = word.average_difficulty
        self.review_count = word.review_count
        self.id = word.id
        self.tags = None
        try:
            v = word.verb
            self.is_verb = True
        except Verb.DoesNotExist:
            self.is_verb = False

    def get_tags(self):
        word = Word.objects.get(pk=self.id)
        self.tags = render_tags(word.tags.all())


# vim: et sts=4 sw=4
