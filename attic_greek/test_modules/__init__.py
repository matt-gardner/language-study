#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.test import TestCase

import attic_greek

from attic_greek import conjugation
from attic_greek import declension
from language_study.drills.models import DeclinableWord
from language_study.drills.models import Verb

verbs = dict()
verbs['aggello'] = Verb.objects.get(word__word__contains=u'ἀγγέλλω')
verbs['aischunomai'] = Verb.objects.get(word__word__contains=u'αἰσχύνομαι')
verbs['dhloo'] = Verb.objects.get(word__word__contains=u'δηλόω')
verbs['deiknumi'] = Verb.objects.get(word__word__contains=u'δείκνυμι')
verbs['didomi'] = Verb.objects.get(word__word__contains=u'δίδωμι')
verbs['eimi'] = Verb.objects.get(word__word__contains=u'εἰμί')
verbs['eimi2'] = Verb.objects.get(word__word__contains=u'εἶμι')
verbs['elauno'] = Verb.objects.get(word__word__contains=u'ἐλαύνω')
verbs['elegxo'] = Verb.objects.get(word__word__contains=u'ἐλέγχω')
verbs['erxomai'] = Verb.objects.get(word__word__contains=u'ἔρχομαι')
verbs['ethelo'] = Verb.objects.get(word__word__contains=u'ἐθέλω')
verbs['faino'] = Verb.objects.get(word__word__contains=u'φαίνω')
verbs['fobeomai'] = Verb.objects.get(word__word__contains=u'φοβέομαι')
verbs['grafo'] = Verb.objects.get(word__word__contains=u'γράφω')
verbs['gignosko'] = Verb.objects.get(word__word__contains=u'γιγνώσκω')
verbs['hiemi'] = Verb.objects.get(word__word__contains=u'ἵημι')
verbs['histemi'] = Verb.objects.get(word__word__contains=u'ἵστημι')
verbs['keleuo'] = Verb.objects.get(word__word__contains=u'κελεύω')
verbs['maxomai'] = Verb.objects.get(word__word__contains=u'μάχομαι')
verbs['nikao'] = Verb.objects.get(word__word__contains=u'νικάω')
verbs['paideuo'] = Verb.objects.get(word__word__contains=u'παιδεύω')
verbs['pempo'] = Verb.objects.get(word__word__contains=u'πέμπω')
verbs['phemi'] = Verb.objects.get(word__word__contains=u'φημί')
verbs['poieo'] = Verb.objects.get(word__word__contains=u'ποιέω')
verbs['tatto'] = Verb.objects.get(word__word__contains=u'τάττω')
verbs['tithemi'] = Verb.objects.get(word__word__contains=u'τίθημι')

verb_cases = [{'person': 'First Person', 'number': 'Singular'}]
verb_cases.append({'person': 'Second Person', 'number': 'Singular'})
verb_cases.append({'person': 'Third Person', 'number': 'Singular'})
verb_cases.append({'person': 'First Person', 'number': 'Plural'})
verb_cases.append({'person': 'Second Person', 'number': 'Plural'})
verb_cases.append({'person': 'Third Person', 'number': 'Plural'})

imp_cases = [{'person': 'Second Person', 'number': 'Singular'}]
imp_cases.append({'person': 'Third Person', 'number': 'Singular'})
imp_cases.append({'person': 'Second Person', 'number': 'Plural'})
imp_cases.append({'person': 'Third Person', 'number': 'Plural'})

DW = DeclinableWord
nouns = dict()
nouns['techne'] = DW.objects.get(word__word__contains=u'τέχνη')
nouns['chora'] = DW.objects.get(word__word__contains=u'χώρα')
nouns['psuche'] = DW.objects.get(word__word__contains=u'ψυχή')
nouns['agora'] = DW.objects.get(word__word__contains=u'ἀγορά')
nouns['logos'] = DW.objects.get(word__word__contains=u'λόγος')
nouns['ergon'] = DW.objects.get(word__word__contains=u'ἔργον')
nouns['anthropos'] = DW.objects.get(word__word__contains=u'ἄνθρωπος')
nouns['adelphos'] = DW.objects.get(word__word__contains=u'ἀδελφός')
nouns['nesos'] = DW.objects.get(word__word__contains=u'νῆσος')
nouns['doron'] = DW.objects.get(word__word__contains=u'δῶρον')

decl_cases = [{'number': 'Singular', 'case': 'Nominative'}]
decl_cases.append({'number': 'Singular', 'case': 'Genitive'})
decl_cases.append({'number': 'Singular', 'case': 'Dative'})
decl_cases.append({'number': 'Singular', 'case': 'Accusative'})
decl_cases.append({'number': 'Singular', 'case': 'Vocative'})
decl_cases.append({'number': 'Plural', 'case': 'Nominative'})
decl_cases.append({'number': 'Plural', 'case': 'Genitive'})
decl_cases.append({'number': 'Plural', 'case': 'Dative'})
decl_cases.append({'number': 'Plural', 'case': 'Accusative'})
decl_cases.append({'number': 'Plural', 'case': 'Vocative'})

class GreekTestCase(TestCase):
    def tearDown(self):
        conjugation.verbose = False
        declension.verbose = False


from attic_greek.test_modules import athematic
from attic_greek.test_modules import consonant_stems
from attic_greek.test_modules import contracted
from attic_greek.test_modules import contracted_future
from attic_greek.test_modules import deponent
from attic_greek.test_modules import erxomai
from attic_greek.test_modules import regular_verbs
from attic_greek.test_modules import regular_nouns
from attic_greek.test_modules import vowel_augment

all_tests = []
all_tests.extend(athematic.all_tests)
all_tests.extend(consonant_stems.all_tests)
all_tests.extend(contracted.all_tests)
all_tests.extend(contracted_future.all_tests)
all_tests.extend(deponent.all_tests)
all_tests.extend(erxomai.all_tests)
all_tests.extend(regular_verbs.all_tests)
all_tests.extend(regular_nouns.all_tests)
all_tests.extend(vowel_augment.all_tests)

# vim: et sw=4 sts=4
