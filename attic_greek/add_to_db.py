#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

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

    # Declensions
    args = {'name': 'First Declension', 'language': language}
    add_or_fail(Declension, args)
    args['name'] = 'Second Declension'
    add_or_fail(Declension, args)
    args['name'] = 'Third Declension'
    add_or_fail(Declension, args)

    # Cases
    args['name'] = 'Nominative'
    add_or_fail(Number, args)
    args['name'] = 'Genitive'
    add_or_fail(Number, args)
    args['name'] = 'Dative'
    add_or_fail(Number, args)
    args['name'] = 'Accusative'
    add_or_fail(Number, args)
    args['name'] = 'Vocative'
    add_or_fail(Number, args)

    # Numbers
    args['name'] = 'Singular'
    add_or_fail(Number, args)
    args['name'] = 'Plural'
    add_or_fail(Number, args)
    args['name'] = 'None'
    add_or_fail(Number, args)

    # Genders
    args['name'] = 'Masculine'
    add_or_fail(Gender, args)
    args['name'] = 'Feminine'
    add_or_fail(Gender, args)
    args['name'] = 'Neuter'
    add_or_fail(Gender, args)

    # DeclinableTypes
    args['name'] = 'Noun'
    add_or_fail(DeclinableType, args)
    args['name'] = 'Pronoun'
    add_or_fail(DeclinableType, args)
    args['name'] = 'Adjective'
    add_or_fail(DeclinableType, args)

    # Conjugations
    args['name'] = 'Thematic'
    add_or_fail(Conjugation, args)
    args['name'] = 'Athematic'
    add_or_fail(Conjugation, args)

    # Persons
    args['name'] = 'First Person'
    add_or_fail(Person, args)
    args['name'] = 'Second Person'
    add_or_fail(Person, args)
    args['name'] = 'Third Person'
    add_or_fail(Person, args)
    args['name'] = 'None'
    add_or_fail(Person, args)

    # Tenses
    args['name'] = 'Present'
    add_or_fail(Tense, args)
    args['name'] = 'Imperfect'
    add_or_fail(Tense, args)
    args['name'] = 'Future'
    add_or_fail(Tense, args)
    args['name'] = 'Aorist'
    add_or_fail(Tense, args)
    args['name'] = 'Perfect'
    add_or_fail(Tense, args)
    args['name'] = 'Pluperfect'
    add_or_fail(Tense, args)

    # Voices
    args['name'] = 'Active'
    add_or_fail(Voice, args)
    args['name'] = 'Middle'
    add_or_fail(Voice, args)
    args['name'] = 'Passive'
    add_or_fail(Voice, args)

    # Moods
    args['name'] = 'Indicative'
    add_or_fail(Mood, args)
    args['name'] = 'Subjunctive'
    add_or_fail(Mood, args)
    args['name'] = 'Optative'
    add_or_fail(Mood, args)
    args['name'] = 'Imperative'
    add_or_fail(Mood, args)
    args['name'] = 'Infinitive'
    add_or_fail(Mood, args)

    # Default WordList
    args['name'] = 'Attic Greek Default Words'
    # TODO: make this a little better...  Maybe make a default user
    args['user'] = User.objects.get(pk=1)
    add_or_fail(WordList, args)

    # Words
    # Thematic verbs
    args = {'wordlist': object_cache['WordList'][args['name']]}
    args['conjugation'] = object_cache['Conjugation']['Thematic']
    args['word'] = u'ἀγγέλλω, ἀγγελῶ, ἤγγειλα, ἤγγελκα, ἤγγελμαι, ἠγγέλθην'
    args['definition'] = u'to announce'
    create_args = {'last_reviewed': datetime.now()}
    add_or_fail(Verb, args, create_args)
    args['word'] = u'αἰσχύνομαι, αἰσχυνοῦμαι, _, _, ᾔσχυμμαι, ᾐσχύνθην'
    args['definition'] = u'to be ashamed'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'δηλόω, δηλώσω, ἐδήλωσα, δεδήλωκα, δεδήλωμαι, ἐδηλώθην'
    args['definition'] = u'to make clear'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'ἐλαύνω, ἐλάω, ἤλασα, ἐλήλακα, ἐλήλαμαι, ἠλάθην'
    args['definition'] = u'to drive, march'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'ἐλέγχω, ἐλέγξω, ἤλεγξα, _, ἐλήλεγμαι, ἠλέγχθην'
    args['definition'] = u"I'm not sure..."
    add_or_fail(Verb, args, create_args)
    args['word'] = u'ἔρχομαι, ἐλεύσομαι, ἦλθον, ἐλήλυθα, _, _'
    args['definition'] = u'to come'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'ἐθέλω, ἐθελήσω, ἠθέλησα, ἠθέληκα, _, _'
    args['definition'] = u'to wish, want'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'φαίνω, φανῶ, ἔφηνα, πέφηνα, πέφασμαι, ἐφάνην'
    args['definition'] = u'to show'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'φοβέομαι, φοβήσομαι, _, _, πεφόβημαι, ἐφοβήθην'
    args['definition'] = u'to fear, be afraid'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'γράφω, γράψω, ἔγραψα, γέγραφα, γέγραμμαι, ἐγράφην'
    args['definition'] = u'to write, draw'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'κελεύω, κελεύσω, ἐκέλευσα, κεκέλευκα, κεκέλευσμαι, '\
            u'ἐκελεύσθην'
    args['definition'] = u'to command, order'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'μάχομαι, μαχοῦμαι, ἐμαχεσάμην, _, μεμάχημαι, _'
    args['definition'] = u'to fight'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'νικάω, νικήσω, ἐνίκησα, νενίκηκα, νενίκημαι, ἐνικήθην'
    args['definition'] = u'to win, conquer, be victorious'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'παιδεύω, παιδεύσω, ἐπαίδευσα, πεπαίδευκα, πεπαίδευμαι, '\
            u'ἐπαιδεύθην'
    args['definition'] = u'to teach'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'πέμπω, πέμψω, ἔπεμψα, πέπομφα, πέπεμμαι, ἐπέμφθην'
    args['definition'] = u'to send'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'ποιέω, ποιήσω, ἐποίησα, πεποίηκα, πεποίημαι, ἐποιήθην'
    args['definition'] = u'to do'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'τάττω, τάξω, ἔταξα, τέταχα, τέταγμαι, ἐτάχθην'
    args['definition'] = u'to arrange, station, align, order'
    add_or_fail(Verb, args, create_args)

    # Athematic verbs
    irreg_args = {}
    args['conjugation'] = object_cache['Conjugation']['Athematic']
    args['word'] = u'δίδωμι, δώσω, ἔδωκα, δέδωκα, δέδομαι, ἐδόθην'
    args['definition'] = u'to give'
    add_or_fail(Verb, args, create_args)
    irregular_verb_form(args['word'], 'First Person', 'Singular', 'Imperfect',
            'Indicative', 'Active', u'ἐδίδουν')
    irregular_verb_form(args['word'], 'Second Person', 'Singular', 'Imperfect',
            'Indicative', 'Active', u'ἐδίδους')
    irregular_verb_form(args['word'], 'Third Person', 'Singular', 'Imperfect',
            'Indicative', 'Active', u'ἐδίδου')
    irregular_verb_form(args['word'], 'Second Person', 'Singular', 'Present',
            'Imperative', 'Active', u'δίδου')
    args['word'] = u'ἵστημι, στήσω, ἔστησα, ἕστηκα, ἕσταμαι, ἐστάθην'
    args['definition'] = u'to stand'
    add_or_fail(Verb, args, create_args)
    args['word'] = u'τίθημι, θήσω, ἔθηκα, τέθηκα, τέθειμαι, ἐτέθην'
    args['definition'] = u'to put'
    add_or_fail(Verb, args, create_args)

    for a in added:
        print 'Added:', a
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


def add_or_fail(model, query_args, create_args={}):
    global object_cache
    if 'name' in query_args:
        output = query_args['name']
    elif 'word' in query_args:
        output = query_args['word']
    elif 'form' in query_args:
        output = query_args['form']
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
    object_cache[model.__name__][output] = obj


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
    options, args = parser.parse_args()
    if options.incremental:
        incremental = True
    add_language()

# vim: et sw=4 sts=4
