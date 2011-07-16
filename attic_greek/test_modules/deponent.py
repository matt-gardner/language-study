#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from attic_greek.conjugation import GreekConjugation
from attic_greek.test_modules import verbs, verb_cases, GreekTestCase
import unicodedata

class DeponentFormsTest(GreekTestCase):
    """We just test a few forms here, because we've tested most of this already.
    The main point here is just to be sure that deponent forms work when the
    principle part has a deponent ending, and that active forms are not allowed
    to be produced.
    """
    def test_maxomai(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐμαχεσάμην', u'ἐμαχέσω', u'ἐμαχέσατο', u'ἐμαχεσάμεθα',
                u'ἐμαχέσασθε', u'ἐμαχέσαντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['maxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_no_active_moxomai(self):
        args = {}
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        conj = GreekConjugation(verbs['maxomai'].word.word)
        for tense in ['Present', 'Imperfect', 'Future', 'Aorist', 'Perfect',
                'Pluperfect']:
            args['tense'] = tense
            for case in verb_cases:
                args.update(case)
                self.assertRaises(ValueError, conj.conjugate, **args)


all_tests = [DeponentFormsTest]

# vim: et sw=4 sts=4
