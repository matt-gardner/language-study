#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.test import TestCase

import attic_greek

from attic_greek import conjugation
from language_study.drills.models import Verb

verbs = dict()
verbs['aggello'] = Verb.objects.get(word__contains=u'ἀγγέλλω')
verbs['aischunomai'] = Verb.objects.get(word__contains=u'αἰσχύνομαι')
verbs['dhloo'] = Verb.objects.get(word__contains=u'δηλόω')
verbs['deiknumi'] = Verb.objects.get(word__contains=u'δείκνυμι')
verbs['didomi'] = Verb.objects.get(word__contains=u'δίδωμι')
verbs['eimi'] = Verb.objects.get(word__contains=u'εἰμί')
verbs['elauno'] = Verb.objects.get(word__contains=u'ἐλαύνω')
verbs['elegxo'] = Verb.objects.get(word__contains=u'ἐλέγχω')
verbs['erxomai'] = Verb.objects.get(word__contains=u'ἔρχομαι')
verbs['ethelo'] = Verb.objects.get(word__contains=u'ἐθέλω')
verbs['faino'] = Verb.objects.get(word__contains=u'φαίνω')
verbs['fobeomai'] = Verb.objects.get(word__contains=u'φοβέομαι')
verbs['grafo'] = Verb.objects.get(word__contains=u'γράφω')
verbs['gignosko'] = Verb.objects.get(word__contains=u'γιγνώσκω')
verbs['histemi'] = Verb.objects.get(word__contains=u'ἵστημι')
verbs['keleuo'] = Verb.objects.get(word__contains=u'κελεύω')
verbs['maxomai'] = Verb.objects.get(word__contains=u'μάχομαι')
verbs['nikao'] = Verb.objects.get(word__contains=u'νικάω')
verbs['paideuo'] = Verb.objects.get(word__contains=u'παιδεύω')
verbs['pempo'] = Verb.objects.get(word__contains=u'πέμπω')
verbs['phemi'] = Verb.objects.get(word__contains=u'φημί')
verbs['poieo'] = Verb.objects.get(word__contains=u'ποιέω')
verbs['tatto'] = Verb.objects.get(word__contains=u'τάττω')
verbs['tithemi'] = Verb.objects.get(word__contains=u'τίθημι')

cases = [{'person': 'First Person', 'number': 'Singular'}]
cases.append({'person': 'Second Person', 'number': 'Singular'})
cases.append({'person': 'Third Person', 'number': 'Singular'})
cases.append({'person': 'First Person', 'number': 'Plural'})
cases.append({'person': 'Second Person', 'number': 'Plural'})
cases.append({'person': 'Third Person', 'number': 'Plural'})

imp_cases = [{'person': 'Second Person', 'number': 'Singular'}]
imp_cases.append({'person': 'Third Person', 'number': 'Singular'})
imp_cases.append({'person': 'Second Person', 'number': 'Plural'})
imp_cases.append({'person': 'Third Person', 'number': 'Plural'})

class GreekTestCase(TestCase):
    def tearDown(self):
        conjugation.verbose = False


from attic_greek.test_modules import athematic
from attic_greek.test_modules import consonant_stems
from attic_greek.test_modules import contracted
from attic_greek.test_modules import contracted_future
from attic_greek.test_modules import erxomai
from attic_greek.test_modules import regular
from attic_greek.test_modules import vowel_augment

all_tests = []
all_tests.extend(athematic.all_tests)
all_tests.extend(consonant_stems.all_tests)
all_tests.extend(contracted.all_tests)
all_tests.extend(contracted_future.all_tests)
all_tests.extend(erxomai.all_tests)
all_tests.extend(regular.all_tests)
all_tests.extend(vowel_augment.all_tests)

# vim: et sw=4 sts=4
