#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.test import TestCase

from attic_greek import conjugation
from attic_greek.conjugation import AthematicConjugation
from attic_greek.conjugation import GreekConjugation
from attic_greek.test_modules import verbs, cases
import unicodedata

class DidomiTest(TestCase):
    # PRESENT TENSE TESTS
    def test_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'δίδωμι', u'δίδως', u'δίδωσι', u'δίδομεν',
                u'δίδοτε', u'διδόασι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'διδῶ', u'διδῷς', u'διδῷ', u'διδῶμεν',
                u'διδῶτε', u'διδῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'διδοίην', u'διδοίης', u'διδοίη', u'διδοίημεν',
                u'διδοίητε', u'διδοίησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    # FIXME
    def test_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'παίδευε', u'παιδευέτω', u'παιδεύετε', u'παιδευόντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['paideuo'].word)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_inf_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'διδόναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['didomi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_ind_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'δίδομαι', u'δίδοσαι', u'δίδοται', u'διδόμεθα',
                u'δίδοσθε', u'δίδονται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'διδῶμαι', u'διδῷ', u'διδῶται', u'διδώμεθα',
                u'διδῶσθε', u'διδῶνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    # FIXME
    def test_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'παιδευοίμην', u'παιδεύοιο', u'παιδεύοιτο', u'παιδευοίμεθα',
                u'παιδεύοισθε', u'παιδεύοιντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['paideuo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'δίδοσο', u'διδόσθω', u'δίδοσθε', u'διδόσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_inf_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'δίδοσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['didomi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    # FIXME
    def test_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐπαίδευον', u'ἐπαίδευες', u'ἐπαίδευε', u'ἐπαιδεύομεν',
                u'ἐπαιδεύετε', u'ἐπαίδευον']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['paideuo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_imperfect_ind_mid(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐδιδόμην', u'ἐδίδοσο', u'ἐδίδοτο', u'ἐδιδόμεθα',
                u'ἐδίδοσθε', u'ἐδίδοντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


all_tests = [DidomiTest]

# vim: et sw=4 sts=4
