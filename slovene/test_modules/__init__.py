#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.test import TestCase

import slovene
from slovene import declension

from language_study.drills.models import WordList

wordlist = WordList.objects.get(name='Slovene Default Words')

verbs = dict()

verb_cases = [{'person': 'First Person', 'number': 'Singular'}]
verb_cases.append({'person': 'Second Person', 'number': 'Singular'})
verb_cases.append({'person': 'Third Person', 'number': 'Singular'})
verb_cases.append({'person': 'First Person', 'number': 'Dual'})
verb_cases.append({'person': 'Second Person', 'number': 'Dual'})
verb_cases.append({'person': 'Third Person', 'number': 'Dual'})
verb_cases.append({'person': 'First Person', 'number': 'Plural'})
verb_cases.append({'person': 'Second Person', 'number': 'Plural'})
verb_cases.append({'person': 'Third Person', 'number': 'Plural'})

imp_cases = [{'person': 'Second Person', 'number': 'Singular'}]
imp_cases.append({'person': 'Third Person', 'number': 'Singular'})
imp_cases.append({'person': 'Second Person', 'number': 'Dual'})
imp_cases.append({'person': 'Third Person', 'number': 'Dual'})
imp_cases.append({'person': 'Second Person', 'number': 'Plural'})
imp_cases.append({'person': 'Third Person', 'number': 'Plural'})

DWs = wordlist.declinableword_set
nouns = dict()
nouns['potnik'] = DWs.get(word__word__contains=u'potnik')
nouns['punca'] = DWs.get(word__word__contains=u'punca')
nouns['ucenec'] = DWs.get(word__word__contains=u'učenec')

adjectives = dict()

decl_cases = [{'number': 'Singular', 'case': 'Nominative'}]
decl_cases.append({'number': 'Dual', 'case': 'Nominative'})
decl_cases.append({'number': 'Plural', 'case': 'Nominative'})
decl_cases.append({'number': 'Singular', 'case': 'Genitive'})
decl_cases.append({'number': 'Dual', 'case': 'Genitive'})
decl_cases.append({'number': 'Plural', 'case': 'Genitive'})
decl_cases.append({'number': 'Singular', 'case': 'Dative'})
decl_cases.append({'number': 'Dual', 'case': 'Dative'})
decl_cases.append({'number': 'Plural', 'case': 'Dative'})
decl_cases.append({'number': 'Singular', 'case': 'Accusative'})
decl_cases.append({'number': 'Dual', 'case': 'Accusative'})
decl_cases.append({'number': 'Plural', 'case': 'Accusative'})
decl_cases.append({'number': 'Singular', 'case': 'Locative'})
decl_cases.append({'number': 'Dual', 'case': 'Locative'})
decl_cases.append({'number': 'Plural', 'case': 'Locative'})
decl_cases.append({'number': 'Singular', 'case': 'Instrumental'})
decl_cases.append({'number': 'Dual', 'case': 'Instrumental'})
decl_cases.append({'number': 'Plural', 'case': 'Instrumental'})

class SloveneTestCase(TestCase):
    def tearDown(self):
        declension.verbose = False
        #conjugation.verbose = False


from slovene.test_modules import regular_nouns

all_tests = []
all_tests.extend(regular_nouns.all_tests)

# vim: et sw=4 sts=4
