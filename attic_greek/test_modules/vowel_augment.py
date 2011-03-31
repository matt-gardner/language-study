#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.test import TestCase

from attic_greek.conjugation import GreekConjugation
from attic_greek.test_modules import verbs, cases
import unicodedata

class VowelAugmentTest(TestCase):
    def test_ethelo(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἤθελον', u'ἤθελες', u'ἤθελε', u'ἠθέλομεν',
                u'ἠθέλετε', u'ἤθελον']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['ethelo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἠθέλησα', u'ἠθέλησας', u'ἠθέλησε', u'ἠθελήσαμεν',
                u'ἠθελήσατε', u'ἠθέλησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['ethelo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἠθελήκη', u'ἠθελήκης', u'ἠθελήκει', u'ἠθελήκεμεν',
                u'ἠθελήκετε', u'ἠθελήκεσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['ethelo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


all_tests = [VowelAugmentTest]

# vim: et sw=4 sts=4
