#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.test import TestCase

from attic_greek.conjugation import GreekConjugation
from attic_greek.test_modules import verbs, cases
import unicodedata

class ContractedFutureTest(TestCase):
    """We just test a few forms here, because we've tested most of this already.
    The main point here is just to be sure that contraction works in the future
    tenses.
    """
    def test_elauno(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐλῶ', u'ἐλᾷς', u'ἐλᾷ', u'ἐλῶμεν', u'ἐλᾶτε', u'ἐλῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['elauno'])
        for case, answer in zip(cases, answers):
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
        conj = GreekConjugation(verbs['aggello'])
        for case, answer in zip(cases, answers):
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
        conj = GreekConjugation(verbs['maxomai'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


all_tests = [ContractedFutureTest]

# vim: et sw=4 sts=4
