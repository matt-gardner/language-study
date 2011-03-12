#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.test import TestCase

from attic_greek.conjugation import GreekConjugation
import unicodedata

class ContractedFutureTest(TestCase):
    """We just test a few forms here, because we've tested most of this already.
    The main point here is just to be sure that contraction works in the future
    tenses.
    """
    def setUp(self):
        self.elauno = u'ἐλαύνω, ἐλάω, ἤλασα, ἐλήλακα, ἐλήλαμαι, ἠλάθην'
        self.aggello = u'ἀγγέλλω, ἀγγελῶ, ἤγγειλα, ἤγγελκα, ἤγγελμαι, ἠγγέλθην'
        self.maxomai = u'μάχομαι, μαχοῦμαι, ἐμαχεσάμην, _, μεμάχημαι, _'
        self.cases = [{'person': 'First Person', 'number': 'Singular'}]
        self.cases.append({'person': 'Second Person', 'number': 'Singular'})
        self.cases.append({'person': 'Third Person', 'number': 'Singular'})
        self.cases.append({'person': 'First Person', 'number': 'Plural'})
        self.cases.append({'person': 'Second Person', 'number': 'Plural'})
        self.cases.append({'person': 'Third Person', 'number': 'Plural'})

    def test_elauno(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐλῶ', u'ἐλᾷς', u'ἐλᾷ', u'ἐλῶμεν', u'ἐλᾶτε', u'ἐλῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.elauno)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aggello(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἀγγελῶ', u'ἀγγελεῖς', u'ἀγγελεῖ', u'ἀγγελοῦμεν',
                u'ἀγγελεῖτε', u'ἀγγελοῦσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.aggello)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_maxomai(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle' # TODO: Should be deponent...
        answers = [u'μαχοῦμαι', u'μαχεῖ', u'μαχεῖται', u'μαχούμεθα',
                u'μαχεῖσθε', u'μαχοῦνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.maxomai)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


all_tests = [ContractedFutureTest]

# vim: et sw=4 sts=4
