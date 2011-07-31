#!/usr/bin/env python

from copy import copy
import random as r
import simplejson

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from language_study.drills.models import *
from language_study.drills.views.common import base_context
from language_study.drills.views.common import devariablize
from language_study.drills.views.filters import filter_words
from language_study.drills.views import form_table_util
from form_table_util import create_table

def base_form_drill_context(request, listname):
    context = base_context(request)
    context['nav_page'] = 'nav_forms'

    wordlist = get_object_or_404(WordList, user=request.user, name=listname)

    context['wordlist'] = wordlist

    #context['tags'] = wordlist.tag_set.all()
    #filters = request.session.get('filters', [])
    #verbs, filter_form = filter_words(verbs, filters)
    #context['filter'] = filter_form
    return context


@login_required
def drill_conjugations(request, listname):
    context = base_form_drill_context(request, listname)
    request.session['review-style'] = 'conjugation'
    context['review_type'] = 'conjugation'
    language = context['wordlist'].language
    context['persons'] = language.person_set.all()
    context['numbers'] = language.number_set.all()
    context['tenses'] = language.tense_set.all()
    context['moods'] = language.mood_set.all()
    context['voices'] = language.voice_set.all()
    verbs = context['wordlist'].verb_set.all()
    if verbs:
        verb = r.choice(list(verbs))
        request.session['word-id'] = verb.id
        context['verb_id'] = verb.id
        form = get_random_form_from_session(request, listname)
        context['inflected_form'] = form
        context['num_verbs'] = verbs.count()
        request.session['verbs-reviewed'] = 0
        context['verbs_reviewed'] = 0
    return render_to_response('forms/drill_verbs.html', context)


@login_required
def drill_declensions(request, listname):
    context = base_form_drill_context(request, listname)
    request.session['review-style'] = 'declension'
    context['review_type'] = 'declension'
    language = context['wordlist'].language
    context['genders'] = language.gender_set.all()
    context['numbers'] = language.number_set.all()
    context['cases'] = language.case_set.all()
    words = context['wordlist'].declinableword_set.all()
    if words:
        word = r.choice(list(words))
        request.session['word-id'] = word.id
        context['word_id'] = word.id
        form = get_random_form_from_session(request, listname)
        context['inflected_form'] = form
        context['num_words'] = words.count()
        request.session['words-reviewed'] = 0
        context['words_reviewed'] = 0
    return render_to_response('forms/drill_nouns.html', context)


@login_required
def view_forms(request, listname):
    context, verbs = base_form_drill_context(request, listname)
    if verbs:
        verb = verbs[0]
        request.session['word-id'] = verb.id
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
    verb = Verb.objects.get(pk=session['word-id'])
    language = verb.wordlist.language
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


def decline_word_from_session(session, raise_errors=False, all_forms=False):
    word = DeclinableWord.objects.get(pk=session['word-id'])
    language = word.wordlist.language
    decl_cls = __import__(language.module_name)\
            .mapping[word.declension.name][word.type.name]
    decl = decl_cls(word.word.word, word.id)
    args = dict()
    args['gender'] = Gender.objects.get(pk=session['gender-id']).name
    args['number'] = Number.objects.get(pk=session['number-id']).name
    args['case'] = Case.objects.get(pk=session['case-id']).name
    try:
        form = decl.decline(**args)
        session['form'] = form
        return form
    except (KeyError, ValueError) as e:
        if raise_errors:
            raise
        return unicode(e)


def get_random_form_from_session(request, listname):
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    if request.session['review-style'] == 'conjugation':
        words = wordlist.verb_set.all()
    elif request.session['review-style'] == 'declension':
        words = wordlist.declinableword_set.all()
    request.session['word-id'] = r.choice(list(words)).id
    while True:
        random_form(request, wordlist)
        print request.session
        try:
            if request.session['review-style'] == 'conjugation':
                form = conj_verb_from_session(request.session, True)
            elif request.session['review-style'] == 'declension':
                form = decline_word_from_session(request.session, True)
            break
        except (ValueError, KeyError):
            pass
    return form


def random_form(request, wordlist):
    language = wordlist.language
    request.session['gender-id'] = r.choice(list(language.gender_set.all())).id
    request.session['case-id'] = r.choice(list(language.case_set.all())).id
    request.session['mood-id'] = r.choice(list(language.mood_set.all())).id
    request.session['person-id'] = r.choice(list(language.person_set.all())).id
    request.session['number-id'] = r.choice(list(language.number_set.all())).id
    request.session['tense-id'] = r.choice(list(language.tense_set.all())).id
    request.session['voice-id'] = r.choice(list(language.voice_set.all())).id


def get_new_random_form(request, listname):
    form = get_random_form_from_session(request, listname)
    ret_val = dict()
    ret_val['inflected_form'] = form
    request.session['form'] = form
    return HttpResponse(simplejson.dumps(ret_val))


def get_new_verb(request, id):
    request.session['word-id'] = id
    ret_val = dict()
    ret_val['inflected_form'] = conj_verb_from_session(request.session)
    return HttpResponse(simplejson.dumps(ret_val))


def guess_verb_form(request, person, number, tense, mood, voice):
    guessed = dict()
    guessed['person'] = Person.objects.get(name=devariablize(person)).name
    guessed['number'] = Number.objects.get(name=devariablize(number)).name
    guessed['tense'] = Tense.objects.get(name=devariablize(tense)).name
    guessed['mood'] = Mood.objects.get(name=devariablize(mood)).name
    guessed['voice'] = Voice.objects.get(name=devariablize(voice)).name
    form = request.session['form']
    verb = Verb.objects.get(pk=request.session['word-id'])
    language = verb.word.wordlist.language
    acceptable = get_matching_verb_forms(language, verb, form)
    ret_val = dict()
    fields = ['person', 'number', 'tense', 'mood', 'voice']
    if guessed in acceptable:
        ret_val['result'] = 'Correct!'
        alternate = alternate_forms(guessed, acceptable, fields)
        if alternate:
            ret_val['result'] += '<br>Also acceptable: ' + alternate
    else:
        ret_val['result'] = 'Wrong in: ' + form_errors(guessed, acceptable,
                fields)
    return HttpResponse(simplejson.dumps(ret_val))


def guess_noun_form(request, gender, number, case):
    guessed = dict()
    guessed['gender'] = Gender.objects.get(name=devariablize(gender)).name
    guessed['number'] = Number.objects.get(name=devariablize(number)).name
    guessed['case'] = Case.objects.get(name=devariablize(case)).name
    form = request.session['form']
    word = DeclinableWord.objects.get(pk=request.session['word-id'])
    language = word.word.wordlist.language
    acceptable = get_matching_noun_forms(language, word, form)
    ret_val = dict()
    fields = ['gender', 'number', 'case']
    if guessed in acceptable:
        ret_val['result'] = 'Correct!'
        alternate = alternate_forms(guessed, acceptable, fields)
        if alternate:
            ret_val['result'] += '<br>Also acceptable: ' + alternate
    else:
        ret_val['result'] = 'Wrong in: ' + form_errors(guessed, acceptable,
                fields)
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


def get_matching_verb_forms(language, verb, form):
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


def get_matching_noun_forms(language, word, form):
    decl_cls = __import__(language.module_name)\
            .mapping[word.declension.name][word.type.name]
    decl = decl_cls(word.word.word)
    genders = language.gender_set.all()
    numbers = language.number_set.all()
    cases = language.case_set.all()
    forms = []
    args = dict()
    for g in genders:
        args['gender'] = g.name
        for n in numbers:
            args['number'] = n.name
            for c in cases:
                args['case'] = c.name
                try:
                    cand_form = decl.decline(**args)
                    if cand_form == form:
                        forms.append(copy(args))
                except (ValueError, TypeError, KeyError):
                    continue
    return forms


def form_errors(guessed, acceptable, fields):
    errors = ''
    for field in fields:
        if guessed[field] not in [a[field] for a in acceptable]:
            if errors:
                errors += ', '
            errors += devariablize(field)
    return errors


def alternate_forms(guessed, acceptable, fields):
    forms = ''
    acceptable.remove(guessed)
    for alternate in acceptable:
        if forms:
            forms += '; '
        forms += form_difference(guessed, alternate, fields)
    return forms


def form_difference(guess, alternate, fields):
    diff = ''
    for field in fields:
        if guess[field] != alternate[field]:
            if diff:
                diff += ', '
            diff += alternate[field]
    return diff



# vim: et sw=4 sts=4
