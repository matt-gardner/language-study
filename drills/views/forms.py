#!/usr/bin/env python

from copy import copy
import random as r
import simplejson

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from language_study.drills.models import Mood
from language_study.drills.models import Number
from language_study.drills.models import Person
from language_study.drills.models import Tense
from language_study.drills.models import Verb
from language_study.drills.models import Voice
from language_study.drills.models import WordList
from language_study.drills.views.common import base_context
from language_study.drills.views.common import devariablize
from language_study.drills.views.filters import filter_words
from language_study.drills.views import form_table_util
from form_table_util import create_table

def base_form_drill_context(request, listname):
    context = base_context(request)
    context['nav_page'] = 'nav_forms'

    errors = request.session.get('errors', None)
    if errors:
        if isinstance(errors, list):
            context['errors'] = errors
        else:
            context['errors'] = [errors]
        del request.session['errors']

    context['greeting'] = 'Hello %s!' % request.user.first_name

    wordlist = request.user.wordlist_set.get(name=listname)

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
    verbs = Verb.objects.filter(word__wordlist=wordlist)
    filters = request.session.get('filters', [])
    verbs, filter_form = filter_words(verbs, filters)
    context['filter'] = filter_form
    context['verbs'] = verbs
    return context, verbs


@login_required
def main(request, listname):
    context, verbs = base_form_drill_context(request, listname)
    if verbs:
        try:
            current_word = request.session.get('word-number', 0)
            word_id = request.session['words'][current_word].id
            verb = verbs.get(word__id=word_id)
        except (Verb.DoesNotExist, IndexError, ValueError, KeyError):
            verb = verbs[0]
        request.session['verb-id'] = verb.id
        context['verb_id'] = verb.id
        context['inflected_form'] = conj_verb_from_session(request.session)
        context['num_verbs'] = verbs.count()
        request.session['verbs-reviewed'] = 0
        context['verbs_reviewed'] = 0
    return render_to_response('forms/drill_forms.html', context)


@login_required
def view_forms(request, listname):
    context, verbs = base_form_drill_context(request, listname)
    if verbs:
        verb = verbs[0]
        request.session['verb-id'] = verb.id
        context['verb_id'] = verb.id
        context['inflected_form'] = conj_verb_from_session(request.session,
                all_forms=True)
        context['num_verbs'] = verbs.count()
    return render_to_response('forms/view_forms.html', context)


@login_required
def view_table(request, listname, verb_id):
    context = base_context(request)
    context['nav_page'] = 'nav_forms'
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    context['wordlist'] = wordlist
    verb = get_object_or_404(Verb, pk=verb_id, word__wordlist=wordlist)
    context['verbs'] = [word.verb for word in
            wordlist.word_set.filter(verb__isnull=False)]
    context['current_verb'] = verb
    language = wordlist.language
    persons = [p.name for p in language.person_set.all() if p.name != 'None']
    numbers = [n.name for n in language.number_set.all() if n.name != 'None']
    context['persons'] = persons
    context['numbers'] = numbers
    person = request.session.get('current_person', persons[0])
    context['current_person'] = person
    number = request.session.get('current_number', numbers[0])
    context['current_number'] = number
    context['table'] = create_table(verb, person, number)
    return render_to_response('forms/table_view.html', context)

@login_required
def update_table(request, listname, verb_id, person, number):
    person = devariablize(person)
    request.session['current_person'] = person
    number = devariablize(number)
    request.session['current_number'] = number
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    verb = get_object_or_404(Verb, pk=verb_id, word__wordlist=wordlist)
    return HttpResponse(create_table(verb, person, number))


def conj_verb_from_session(session, raise_errors=False, all_forms=False):
    verb = Verb.objects.get(pk=session['verb-id'])
    language = verb.word.wordlist.language
    conj_cls = __import__(language.module_name).mapping[verb.conjugation.name]
    conj = conj_cls(verb.word.word, verb.id)
    args = dict()
    args['person'] = Person.objects.get(pk=session['person-id']).name
    args['number'] = Number.objects.get(pk=session['number-id']).name
    args['tense'] = Tense.objects.get(pk=session['tense-id']).name
    args['mood'] = Mood.objects.get(pk=session['mood-id']).name
    args['voice'] = Voice.objects.get(pk=session['voice-id']).name
    try:
        forms = conj.conjugate(**args)
        if not all_forms:
            form = r.choice(forms)
        else:
            form = ', '.join(forms)
        session['form'] = form
        return form
    except ValueError as e:
        if raise_errors:
            raise
        return unicode(e)


def random_form(session):
    verb = Verb.objects.get(pk=session['verb-id'])
    language = verb.word.wordlist.language
    session['mood-id'] = r.choice(list(language.mood_set.all())).id
    session['person-id'] = r.choice(list(language.person_set.all())).id
    session['number-id'] = r.choice(list(language.number_set.all())).id
    session['tense-id'] = r.choice(list(language.tense_set.all())).id
    session['voice-id'] = r.choice(list(language.voice_set.all())).id


def get_new_random_form(request):
    while True:
        random_form(request.session)
        try:
            form = conj_verb_from_session(request.session, True)
            break
        except ValueError:
            pass
    ret_val = dict()
    ret_val['inflected_form'] = form
    request.session['form'] = form
    return HttpResponse(simplejson.dumps(ret_val))


def get_new_verb(request, id):
    request.session['verb-id'] = id
    ret_val = dict()
    ret_val['inflected_form'] = conj_verb_from_session(request.session)
    return HttpResponse(simplejson.dumps(ret_val))


def guess_form(request, person, number, tense, mood, voice):
    guessed = dict()
    guessed['person'] = Person.objects.get(name=devariablize(person)).name
    guessed['number'] = Number.objects.get(name=devariablize(number)).name
    guessed['tense'] = Tense.objects.get(name=devariablize(tense)).name
    guessed['mood'] = Mood.objects.get(name=devariablize(mood)).name
    guessed['voice'] = Voice.objects.get(name=devariablize(voice)).name
    form = request.session['form']
    verb = Verb.objects.get(pk=request.session['verb-id'])
    language = verb.word.wordlist.language
    acceptable = get_matching_forms(language, verb, form)
    ret_val = dict()
    if guessed in acceptable:
        ret_val['result'] = 'Correct!'
        alternate = alternate_forms(guessed, acceptable)
        if alternate:
            ret_val['result'] += '<br>Also acceptable: ' + alternate
    else:
        ret_val['result'] = 'Wrong in: ' + form_errors(guessed, acceptable)
        ret_val['result'] += '<br>' + form
    return HttpResponse(simplejson.dumps(ret_val))


def inflect_form(request, person, number, tense, mood, voice):
    person = devariablize(person)
    request.session['person-id'] = Person.objects.get(name=person).id
    number = devariablize(number)
    request.session['number-id'] = Number.objects.get(name=number).id
    tense = devariablize(tense)
    request.session['tense-id'] = Tense.objects.get(name=tense).id
    mood = devariablize(mood)
    request.session['mood-id'] = Mood.objects.get(name=mood).id
    voice = devariablize(voice)
    request.session['voice-id'] = Voice.objects.get(name=voice).id
    ret_val = dict()
    ret_val['inflected_form'] = conj_verb_from_session(request.session)
    return HttpResponse(simplejson.dumps(ret_val))


def get_matching_forms(language, verb, form):
    conj_cls = __import__(language.module_name).mapping[verb.conjugation.name]
    conj = conj_cls(verb.word.word)
    persons = language.person_set.all()
    numbers = language.number_set.all()
    tenses = language.tense_set.all()
    moods = language.mood_set.all()
    voices = language.voice_set.all()
    forms = []
    args = dict()
    for t in tenses:
        args['tense'] = t.name
        for v in voices:
            args['voice'] = v.name
            for m in moods:
                args['mood'] = m.name
                for p in persons:
                    args['person'] = p.name
                    for n in numbers:
                        args['number'] = n.name
                        try:
                            cand_forms = conj.conjugate(**args)
                            for cand_form in cand_forms:
                                if cand_form == form:
                                    forms.append(copy(args))
                        except (ValueError, TypeError):
                            continue
    return forms


def form_errors(guessed, acceptable):
    errors = ''
    fields = ['person', 'number', 'tense', 'mood', 'voice']
    for field in fields:
        if guessed[field] not in [a[field] for a in acceptable]:
            if errors:
                errors += ', '
            errors += devariablize(field)
    return errors


def alternate_forms(guessed, acceptable):
    forms = ''
    acceptable.remove(guessed)
    for alternate in acceptable:
        if forms:
            forms += '; '
        forms += form_difference(guessed, alternate)
    return forms


def form_difference(guess, alternate):
    diff = ''
    fields = ['person', 'number', 'tense', 'mood', 'voice']
    for field in fields:
        if guess[field] != alternate[field]:
            if diff:
                diff += ', '
            diff += alternate[field]
    return diff



# vim: et sw=4 sts=4