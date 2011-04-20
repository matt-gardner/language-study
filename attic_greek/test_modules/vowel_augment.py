#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from attic_greek import conjugation
from attic_greek.conjugation import GreekConjugation
from attic_greek.test_modules import verbs, cases, GreekTestCase
import unicodedata

class VowelAugmentTest(GreekTestCase):
    def test_ethelo_imperfect(self):
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

    def test_ethelo_aorist(self):
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

    def test_ethelo_pluperfect(self):
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
