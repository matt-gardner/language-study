#!/usr/bin/env python

from django import forms
from django.db.models import Avg
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.utils import simplejson

from datetime import datetime
from random import shuffle

from language_study.drills.models import Word, WordList, Tag, Verb
from language_study.drills.filters import filter_words

# Word list stuff
#################

def create_word_list(request, next_url):
    wordlist = WordList(name=request.POST['name'], user=request.user)
    wordlist.save()
    request.session['wordlist-name'] = request.POST['name']
    request.session['word-number'] = 0
    request.session['words'] = []
    return HttpResponseRedirect(next_url)


def delete_word_list(request, name, next_url):
    wordlist = WordList.objects.get(name=name)
    wordlist.delete()
    del request.session['wordlist-name']
    request.session['word-number'] = 0
    return HttpResponseRedirect(next_url)


def get_word_list(request, name):
    request.session['wordlist-name'] = name
    request.session['word-number'] = 0
    wordlist = request.user.wordlist_set.get(name=name)
    words = wordlist.word_set.all()
    request.session['words'] = [AjaxWord(c) for c in words]
    return return_word_from_session(request)


def add_word_to_list(request, next_url):
    word = request.POST['word']
    request.session['errors'] = []
    if not word:
        request.session['errors'].append("You didn't enter a word!")

    definition = request.POST['definition']
    if not definition:
        request.session['errors'].append("You didn't enter any definition!")

    list_name = request.session.get('wordlist-name', None)
    if not list_name:
        request.session['errors'].append("You didn't select a word list!")

    if request.session['errors']:
        return HttpResponseRedirect(next_url)

    del request.session['errors']
    now = datetime.now()
    wordlist = WordList.objects.get(name=list_name)
    word = Word(wordlist=wordlist, word=word, definition=definition,
            last_reviewed=now, date_entered=now)
    word.save()
    wordlist.save()
    return HttpResponseRedirect(next_url)


def reorder_word_list(request, ordering):
    request.session['ordering'] = ordering
    reorder_words_in_session(request)
    return return_word_from_session(request)


def reorder_words_in_session(request, word_number=0):
    ordering = request.session.get('ordering', 'date_entered')
    if ordering == 'random':
        shuffle(request.session['words'])
        request.session['word-number'] = 0
        return
    filters = request.session.get('filters', [])
    wordlist_name = request.session['wordlist-name']
    wordlist = request.user.wordlist_set.get(name=wordlist_name)
    words, _ = filter_words(wordlist.word_set, filters)
    if ordering == 'alphabetical':
        words = words.order_by('word')
    elif ordering == 'last_reviewed':
        words = words.order_by('last_reviewed')
    elif ordering == 'least_reviewed':
        words = words.order_by('review_count')
    elif ordering == 'date_entered':
        words = words.order_by('date_entered')
    elif ordering == 'difficulty':
        words = words.order_by('-average_difficulty')
    request.session['words'] = [AjaxWord(c) for c in words]
    request.session['word-number'] = word_number


# Tag stuff
###########

def add_tag(request, next_url):
    name = request.POST['name']
    request.session['errors'] = []
    list_name = request.session.get('wordlist-name', None)
    if not list_name:
        request.session['errors'].append("You didn't select a word list!")

    if request.session['errors']:
        return HttpResponseRedirect(next_url)

    del request.session['errors']
    wordlist = WordList.objects.get(name=list_name)
    tag = Tag(name=name, wordlist=wordlist)
    tag.save()
    return HttpResponseRedirect(next_url)


def add_tag_to_word(request, tag):
    list_name = request.session.get('wordlist-name', None)
    wordlist = WordList.objects.get(name=list_name)
    tag = wordlist.tag_set.get(name=tag)
    word = wordlist.word_set.get(pk=request.session['word-id'])
    word.tags.add(tag)
    ret_val = dict()
    ret_val['tags'] = render_tags(word.tags.all())
    return HttpResponse(simplejson.dumps(ret_val))


def remove_tag_from_word(request, tag):
    list_name = request.session.get('wordlist-name', None)
    wordlist = WordList.objects.get(name=list_name)
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


# The general "return a word" AJAX function
###########################################

def return_word_from_session(request):
    return HttpResponse(simplejson.dumps(get_word_info_from_session(request)))


def get_word_info_from_session(request):
    ret_val = dict()
    words = request.session['words']
    num_words = len(words)
    current_word = request.session['word-number']
    current_word %= num_words
    request.session['word-number'] = current_word
    request.session['word-id'] = words[current_word].id
    words[current_word].get_tags()
    ret_val['by_definition'] = request.session.get('by-definition', False)
    ret_val['word'] = vars(words[current_word])
    ret_val['word_number'] = current_word + 1
    ret_val['num_words'] = num_words
    ret_val['difficulty'] = sum([c.difficulty for c in words])/len(words)
    return ret_val


# Other general methods
#######################

def review_styles():
    styles = []
    styles.append(ReviewStyle('Review All Words', '/all-words/'))
    styles.append(ReviewStyle('By Difficulty', '/difficulty/'))
    styles.append(ReviewStyle('Daily Review', '/daily/'))
    return styles


def next_word(request, difficulty=None):
    if difficulty:
        word = update_word_difficulty_from_session(request, difficulty)
        ajaxword = request.session['words'][request.session['word-number']]
        ajaxword.difficulty = word.average_difficulty
        ajaxword.review_count = word.review_count
    request.session['word-number'] += 1
    return return_word_from_session(request)


def prev_word(request):
    request.session['word-number'] -= 1
    return return_word_from_session(request)


def update_word_difficulty_from_session(request, difficulty):
    wordlist_name = request.session['wordlist-name']
    wordlist = request.user.wordlist_set.get(name=wordlist_name)
    word = wordlist.word_set.get(pk=request.session['word-id'])
    word.update_difficulty(Word.DIFFICULTY_SCORES[difficulty])
    word.reviewed()
    return word


def set_by_definition(request, value):
    if value == 'true':
        request.session['by-definition'] = True
    else:
        request.session['by-definition'] = False
    return return_word_from_session(request)


def devariablize(string):
    return ' '.join([s.capitalize() for s in string.split('_')])


def base_review_context(request):
    context = RequestContext(request)

    errors = request.session.get('errors', None)
    if errors:
        if isinstance(errors, list):
            context['errors'] = errors
        else:
            context['errors'] = [errors]
        del request.session['errors']

    context['greeting'] = 'Hello %s!' % request.user.first_name

    lists = request.user.wordlist_set.all()
    context['wordlists'] = lists

    context['review_styles'] = review_styles()

    list_name = request.session.get('wordlist-name', '')
    if list_name:
        wordlist = lists.get(name=list_name)
    else:
        wordlist = lists[0]
        request.session['wordlist-name'] = wordlist.name

    context['wordlist'] = wordlist

    context['tags'] = wordlist.tag_set.all()
    words = wordlist.word_set
    filters = request.session.get('filters', [])
    words, filter_form = filter_words(words, filters)
    context['filter'] = filter_form
    context['num_words'] = len(words)
    if words:
        ave_difficulty = words.aggregate(ave=Avg('average_difficulty'))['ave']
        context['average_difficulty'] = ave_difficulty
    return context, words


# Classes that help out with things
###################################

class ReviewStyle(object):
    def __init__(self, name, link):
        self.name = name
        self.link = link


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
