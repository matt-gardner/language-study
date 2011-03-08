#!/usr/bin/env python

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

from language_study.drills.models import *
from optparse import OptionParser

def add_language(incremental=False):
    language_name = 'Attic Greek'
    module_name = 'attic_greek'
    added = []
    try:
        language = Language.objects.get(name=language_name)
        if not incremental:
            raise RuntimeError('%s is already in the database!' % language_name)
    except Language.DoesNotExist:
        added.append('Language: ' + language_name)
        language = Language(name=language_name, module_name=module_name)
        language.save()
    # Declensions
    add_or_fail('First Declension', Declension, language, incremental, added)
    add_or_fail('Second Declension', Declension, language, incremental, added)
    add_or_fail('Third Declension', Declension, language, incremental, added)
    # Cases
    add_or_fail('Nominative', Case, language, incremental, added)
    add_or_fail('Genitive', Case, language, incremental, added)
    add_or_fail('Dative', Case, language, incremental, added)
    add_or_fail('Accusative', Case, language, incremental, added)
    add_or_fail('Vocative', Case, language, incremental, added)
    # Numbers
    add_or_fail('Singular', Number, language, incremental, added)
    add_or_fail('Plural', Number, language, incremental, added)
    add_or_fail('None', Number, language, incremental, added)
    # Genders
    add_or_fail('Masculine', Gender, language, incremental, added)
    add_or_fail('Feminine', Gender, language, incremental, added)
    add_or_fail('Neuter', Gender, language, incremental, added)
    # DeclinableTypes
    add_or_fail('Noun', DeclinableType, language, incremental, added)
    add_or_fail('Pronoun', DeclinableType, language, incremental, added)
    add_or_fail('Adjective', DeclinableType, language, incremental, added)
    # Conjugations
    add_or_fail('Thematic', Conjugation, language, incremental, added)
    # Persons
    add_or_fail('First Person', Person, language, incremental, added)
    add_or_fail('Second Person', Person, language, incremental, added)
    add_or_fail('Third Person', Person, language, incremental, added)
    add_or_fail('None', Person, language, incremental, added)
    # Tenses
    add_or_fail('Present', Tense, language, incremental, added)
    add_or_fail('Imperfect', Tense, language, incremental, added)
    add_or_fail('Future', Tense, language, incremental, added)
    add_or_fail('Aorist', Tense, language, incremental, added)
    add_or_fail('Perfect', Tense, language, incremental, added)
    add_or_fail('Pluperfect', Tense, language, incremental, added)
    # Voices
    add_or_fail('Active', Voice, language, incremental, added)
    add_or_fail('Middle', Voice, language, incremental, added)
    add_or_fail('Passive', Voice, language, incremental, added)
    # Moods
    add_or_fail('Indicative', Mood, language, incremental, added)
    add_or_fail('Subjunctive', Mood, language, incremental, added)
    add_or_fail('Optative', Mood, language, incremental, added)
    add_or_fail('Imperative', Mood, language, incremental, added)
    add_or_fail('Infinitive', Mood, language, incremental, added)
    for a in added:
        print 'Added:', a
    if not added:
        print 'Nothing added to the database'


def add_or_fail(name, model, language, incremental, added):
    try:
        obj = model.objects.get(name=name, language=language)
        if not incremental:
            raise RuntimeError('%s is already in the database!' % name)
    except model.DoesNotExist:
        obj = model(name=name, language=language)
        obj.save()
        added.append(model.__name__ + ': ' + name)


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
    add_language(incremental=options.incremental)

# vim: et sw=4 sts=4
