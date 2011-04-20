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

    # Default WordList
    args['name'] = 'Attic Greek Default Words'
    # TODO: make this a little better...  Maybe make a default user
    args['user'] = User.objects.get(pk=1)
    add_or_fail(WordList, args)

    args = {'wordlist': object_cache['WordList'][args['name']]}
    create_args = {'last_reviewed': datetime.now()}
    for verb in json['Verbs']:
        args['conjugation'] = object_cache['Conjugation'][verb['conjugation']]
        args['word'] = verb['word']
        args['definition'] = verb['definition']
        add_or_fail(Verb, args, create_args)
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

    if not added:
        print 'Nothing added to the database'


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


def add_or_fail(model, query_args, create_args={}):
    global object_cache
    if 'name' in query_args:
        output = query_args['name']
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
