#!/usr/bin/env python

import simplejson

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from language_study.drills.common import devariablize
from language_study.drills.filters import filter_words
from language_study.drills.models import Mood
from language_study.drills.models import Number
from language_study.drills.models import Person
from language_study.drills.models import Tense
from language_study.drills.models import Verb
from language_study.drills.models import Voice

def base_form_drill_context(request):
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

    list_name = request.session.get('wordlist-name', '')
    if list_name:
        wordlist = lists.get(name=list_name)
    else:
        wordlist = lists[0]
        request.session['wordlist-name'] = wordlist.name

    context['wordlist'] = wordlist
    language = wordlist.language
    context['persons'] = language.person_set.all()
    context['cur_person'] = context['persons'][0]
    request.session['person-id'] = context['cur_person'].id
    context['numbers'] = language.number_set.all()
    context['cur_number'] = context['numbers'][0]
    request.session['number-id'] = context['cur_number'].id
    context['tenses'] = language.tense_set.all()
    context['cur_tense'] = context['tenses'][0]
    request.session['tense-id'] = context['cur_tense'].id
    context['moods'] = language.mood_set.all()
    context['cur_mood'] = context['moods'][0]
    request.session['mood-id'] = context['cur_mood'].id
    context['voices'] = language.voice_set.all()
    context['cur_voice'] = context['voices'][0]
    request.session['voice-id'] = context['cur_voice'].id

    context['tags'] = wordlist.tag_set.all()
    # we can't do wordlist.verb_set.all() because of the way django inheritance
    # works
    verbs = Verb.objects.filter(wordlist=wordlist)
    filters = request.session.get('filters', [])
    verbs, filter_form = filter_words(verbs, filters)
    context['filter'] = filter_form
    context['num_words'] = len(verbs)
    return context, verbs


@login_required
def index(request):
    context, verbs = base_form_drill_context(request)
    if verbs:
        verb = verbs[0]
        request.session['verb-id'] = verb.id
        context['inflected_form'] = conj_verb_from_session(request.session)
        context['num_verbs'] = verbs.count()
        request.session['verbs-reviewed'] = 0
        context['verbs_reviewed'] = 0
    return render_to_response('drill_forms.html', context)


def conj_verb_from_session(session):
    verb = Verb.objects.get(pk=session['verb-id'])
    language = verb.wordlist.language
    conj_cls = __import__(language.module_name).mapping[verb.conjugation.name]
    conj = conj_cls(verb.word)
    args = dict()
    if session['person-id']:
        args['person'] = Person.objects.get(pk=session['person-id']).name
    else:
        args['person'] = None
    if session['number-id']:
        args['number'] = Number.objects.get(pk=session['number-id']).name
    else:
        args['number'] = None
    args['tense'] = Tense.objects.get(pk=session['tense-id']).name
    args['mood'] = Mood.objects.get(pk=session['mood-id']).name
    args['voice'] = Voice.objects.get(pk=session['voice-id']).name
    try:
        return conj.conjugate(**args)
    except ValueError as e:
        return unicode(e)


def inflect_form(request, person, number, tense, mood, voice):
    person = devariablize(person)
    if person:
        request.session['person-id'] = Person.objects.get(name=person).id
    else:
        request.session['person-id'] = None
    number = devariablize(number)
    if number:
        request.session['number-id'] = Number.objects.get(name=number).id
    else:
        request.session['number-id'] = None
    tense = devariablize(tense)
    request.session['tense-id'] = Tense.objects.get(name=tense).id
    mood = devariablize(mood)
    request.session['mood-id'] = Mood.objects.get(name=mood).id
    voice = devariablize(voice)
    request.session['voice-id'] = Voice.objects.get(name=voice).id
    ret_val = dict()
    ret_val['inflected_form'] = conj_verb_from_session(request.session)
    return HttpResponse(simplejson.dumps(ret_val))


# vim: et sw=4 sts=4