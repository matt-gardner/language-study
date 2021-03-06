#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

import codecs
import simplejson

from collections import defaultdict
from copy import deepcopy
from datetime import datetime
from django.contrib.auth.models import User
from language_study.drills.models import *
from optparse import OptionParser

incremental = False
added = []
object_cache = defaultdict(dict)

def add_language():
    language_name = 'Attic Greek'
    module_name = 'attic_greek'
    try:
        language = Language.objects.get(name=language_name)
        if not incremental:
            raise RuntimeError('%s is already in the database!' % language_name)
    except Language.DoesNotExist:
        added.append('Language: ' + language_name)
        language = Language(name=language_name, module_name=module_name)
        language.save()
    object_cache['Language'][language_name] = language

    f = codecs.open('attic_greek/language_data.json', 'r', 'utf-8')
    json = simplejson.load(f)

    args = {'language': language}

    for name in json['Declensions']:
        args['name'] = name
        add_or_fail(Declension, args)

    for name in json['Genders']:
        args['name'] = name
        add_or_fail(Gender, args)

    for name in json['Cases']:
        args['name'] = name
        add_or_fail(Case, args)

    for name in json['Persons']:
        args['name'] = name
        add_or_fail(Person, args)

    for name in json['Numbers']:
        args['name'] = name
        add_or_fail(Number, args)

    for name in json['Tenses']:
        args['name'] = name
        add_or_fail(Tense, args)

    for name in json['Moods']:
        args['name'] = name
        add_or_fail(Mood, args)

    for name in json['Voices']:
        args['name'] = name
        add_or_fail(Voice, args)

    for name in json['Declinable Types']:
        args['name'] = name
        add_or_fail(DeclinableType, args)

    for name in json['Conjugations']:
        args['name'] = name
        add_or_fail(Conjugation, args)

    # Default User
    user_args = {'username': "attic_greek_default_user"}
    add_or_fail(User, user_args)
    user = object_cache['User'][user_args['username']]
    user.set_password('default')
    user.save()

    # Default WordList
    args['name'] = 'Attic Greek Default Words'
    args['user'] = user
    add_or_fail(WordList, args)

    word_args = {'wordlist': object_cache['WordList'][args['name']]}
    create_args = {'last_reviewed': datetime.now()}
    create_args['date_entered'] = datetime.now()
    create_args['next_review'] = datetime.now()
    create_args['last_wrong'] = datetime.now()

    for verb in json['Verbs']:
        word_args['word'] = verb['word']
        word_args['definition'] = verb['definition']
        word = add_or_fail(Word, word_args, create_args)
        v_args = {'word': word}
        v_args['wordlist'] = word_args['wordlist']
        v_args['conjugation'] = object_cache['Conjugation'][verb['conjugation']]
        add_or_fail(Verb, v_args)
        if "tenses with no passive" in verb:
            for tense in verb["tenses with no passive"]:
                tense_with_no_passive(verb['word'], tense)
        if "irregular forms" in verb:
            for form in verb["irregular forms"]:
                person = form['Person']
                number = form['Number']
                tense = form['Tense']
                mood = form['Mood']
                voice = form['Voice']
                f = form['Form']
                irregular_verb_form(verb['word'], person, number, tense, mood,
                        voice, f)
        if "irregular stems" in verb:
            for stem in verb["irregular stems"]:
                tense = stem['Tense']
                mood = stem['Mood']
                voice = stem['Voice']
                s = stem['Stem']
                irregular_verb_stem(verb['word'], tense, mood, voice, s)
        if "irregular augmented stems" in verb:
            for stem in verb["irregular augmented stems"]:
                tense = stem['Tense']
                s = stem['Stem']
                irregular_verb_aug_stem(verb['word'], tense, mood, voice, s)

    word_args = {'wordlist': object_cache['WordList'][args['name']]}
    create_args = {'last_reviewed': datetime.now()}
    create_args['date_entered'] = datetime.now()
    create_args['next_review'] = datetime.now()
    create_args['last_wrong'] = datetime.now()
    for noun in json['Nouns']:
        add_declinable_type(noun, 'Noun', word_args, create_args)
    for adjective in json['Adjectives']:
        add_declinable_type(adjective, 'Adjective', word_args, create_args)

    if not added:
        print 'Nothing added to the database'


def add_declinable_type(decl, type, word_args, create_args):
    word_args['word'] = decl['word']
    word_args['definition'] = decl['definition']
    word = add_or_fail(Word, word_args, create_args)
    n_args = {'word': word}
    n_args['wordlist'] = word_args['wordlist']
    n_args['declension'] = object_cache['Declension'][decl['declension']]
    n_args['type'] = object_cache['DeclinableType'][type]
    add_or_fail(DeclinableWord, n_args)
    if "irregular forms" in decl:
        for form in decl["irregular forms"]:
            gender = form['Gender']
            number = form['Number']
            case = form['Case']
            f = form['Form']
            irregular_declinable_form(decl['word'], gender, number, case, f)
    if "long penult" in decl and decl["long penult"] == 'True':
        args = {'declinable': object_cache['DeclinableWord'][decl['word']]}
        add_or_fail(LongPenult, args)


def tense_with_no_passive(verb, tense):
    args = {}
    args['verb'] = object_cache['Verb'][verb]
    args['tense'] = object_cache['Tense'][tense]
    add_or_fail(VerbTenseWithNoPassive, args)


def irregular_verb_form(verb, person, number, tense, mood, voice, form):
    args = {}
    args['verb'] = object_cache['Verb'][verb]
    args['person'] = object_cache['Person'][person]
    args['number'] = object_cache['Number'][number]
    args['tense'] = object_cache['Tense'][tense]
    args['mood'] = object_cache['Mood'][mood]
    args['voice'] = object_cache['Voice'][voice]
    args['form'] = form
    add_or_fail(IrregularVerbForm, args)


def irregular_verb_stem(verb, tense, mood, voice, stem):
    args = {}
    args['verb'] = object_cache['Verb'][verb]
    args['tense'] = object_cache['Tense'][tense]
    args['mood'] = object_cache['Mood'][mood]
    args['voice'] = object_cache['Voice'][voice]
    args['stem'] = stem
    add_or_fail(IrregularVerbStem, args)


def irregular_verb_aug_stem(verb, tense, mood, voice, stem):
    args = {}
    args['verb'] = object_cache['Verb'][verb]
    args['tense'] = object_cache['Tense'][tense]
    args['stem'] = stem
    add_or_fail(IrregularVerbAugmentedStem, args)


def irregular_declinable_form(declinable, gender, number, case, form):
    args = {}
    args['declinable'] = object_cache['DeclinableWord'][declinable]
    args['gender'] = object_cache['Gender'][gender]
    args['number'] = object_cache['Number'][number]
    args['case'] = object_cache['Case'][case]
    args['form'] = form
    add_or_fail(IrregularDeclinableForm, args)


def add_or_fail(model, query_args, create_args={}):
    global object_cache
    if 'username' in query_args:
        output = query_args['username']
    elif 'name' in query_args:
        output = query_args['name']
    elif 'conjugation' in query_args:
        output = query_args['word'].word
    elif 'declension' in query_args:
        output = query_args['word'].word
    elif 'declinable' in query_args:
        output = query_args['declinable'].word.word
    elif 'word' in query_args:
        output = query_args['word']
    elif 'form' in query_args:
        output = query_args['form']
    elif 'stem' in query_args:
        output = query_args['stem']
    else:
        output = 'Something'
    try:
        obj = model.objects.get(**query_args)
        if not incremental:
            raise RuntimeError('%s is already in the database!' % name)
    except model.DoesNotExist:
        query_args.update(create_args)
        obj = model(**query_args)
        obj.save()
        global added
        added.append(model.__name__ + ': ' + output)
        print 'Added:', added[-1]
        for key in create_args:
            del query_args[key]
    object_cache[model.__name__][output] = obj
    return obj


def dump_fixture_file(filename):
    from subprocess import Popen
    proc = Popen('python manage.py dumpdata drills --indent=2 >%s' % filename,
            shell=True)
    proc.wait()
    print 'Created fixture file %s' % filename


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-i', '--incremental',
            dest='incremental',
            action='store_true',
            help='Incrementally add this to the database (i.e., if parts are '
            'already there, only add what is missing).  If this option is not '
            'given, we throw an exception if we find something that is already '
            'in the database.',
            )
    parser.add_option('-f', '--fixture',
            dest='fixture',
            action='store_true',
            help='Dump a fixture file (mostly for use with running tests)',
            )
    options, args = parser.parse_args()
    if options.incremental:
        incremental = True
    add_language()
    if options.fixture:
        dump_fixture_file('attic_greek/fixtures/initial_data.json')

# vim: et sw=4 sts=4
