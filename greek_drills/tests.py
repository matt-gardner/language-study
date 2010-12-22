# -*- encoding: utf-8 -*-
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

from conjugation import GreekConjugation
import unicodedata

class RegularConjugationTest(TestCase):
    def setUp(self):
        self.paideuw = u'παιδεύω, παιδεύσω, ἐπαίδευσα, πεπαίδευκα, πεπαίδευμαι,'
        self.paideuw += u'ἐπαιδεύθην'
        self.cases = [{'person': 'First Person', 'number': 'Singular'}]
        self.cases.append({'person': 'Second Person', 'number': 'Singular'})
        self.cases.append({'person': 'Third Person', 'number': 'Singular'})
        self.cases.append({'person': 'First Person', 'number': 'Plural'})
        self.cases.append({'person': 'Second Person', 'number': 'Plural'})
        self.cases.append({'person': 'Third Person', 'number': 'Plural'})

    # PRESENT TENSE TESTS
    def test_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'παιδεύω', u'παιδεύεις', u'παιδεύει', u'παιδεύομεν',
                u'παιδεύετε', u'παιδεύουσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'παιδεύω', u'παιδεύῃς', u'παιδεύῃ', u'παιδεύωμεν',
                u'παιδεύητε', u'παιδεύωσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'παιδεύοιμι', u'παιδεύοις', u'παιδεύοι', u'παιδεύοιμεν',
                u'παιδεύοιτε', u'παιδεύοιεν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

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
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_inf_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = None
        args['number'] = None
        answer = u'παιδεύειν'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(self.paideuw)
        self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_ind_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'παιδεύομαι', u'παιδεύει', u'παιδεύεται', u'παιδευόμεθα',
                u'παιδεύεσθε', u'παιδεύονται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_subj_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'παιδεύωμαι', u'παιδεύῃ', u'παιδεύηται', u'παιδευώμεθα',
                u'παιδεύησθε', u'παιδεύωνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'παιδευοίμην', u'παιδεύοιο', u'παιδεύοιτο', u'παιδευοίμεθα',
                u'παιδεύοισθε', u'παιδεύοιντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_imp_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'παιδεύου', u'παιδευέσθω', u'παιδεύεσθε', u'παιδευέσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_inf_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = None
        args['number'] = None
        answer = u'παιδεύεσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(self.paideuw)
        self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_ind_pass(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Passive'
        answers = [u'παιδεύομαι', u'παιδεύει', u'παιδεύεται', u'παιδευόμεθα',
                u'παιδεύεσθε', u'παιδεύονται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_subj_pass(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Passive'
        answers = [u'παιδεύωμαι', u'παιδεύῃ', u'παιδεύηται', u'παιδευώμεθα',
                u'παιδεύησθε', u'παιδεύωνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_opt_pass(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Passive'
        answers = [u'παιδευοίμην', u'παιδεύοιο', u'παιδεύοιτο', u'παιδευοίμεθα',
                u'παιδεύοισθε', u'παιδεύοιντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_imp_pass(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Passive'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'παιδεύου', u'παιδευέσθω', u'παιδεύεσθε', u'παιδευέσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_present_inf_pass(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Passive'
        args['person'] = None
        args['number'] = None
        answer = u'παιδεύεσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(self.paideuw)
        self.failUnlessEqual(conj.conjugate(**args), answer)

    # IMPERFECT TENSE TESTS
    def test_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐπαίδευον', u'ἐπαίδευες', u'ἐπαίδευε', u'ἐπαιδεύομεν',
                u'ἐπαιδεύετε', u'ἐπαίδευον']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_imperfect_ind_mid(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐπαιδευόμην', u'ἐπαιδεύου', u'ἐπαιδεύετο', u'ἐπαιδευόμεθα',
                u'ἐπαιδεύεσθε', u'ἐπαιδεύοντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_imperfect_ind_pass(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Passive'
        answers = [u'ἐπαιδευόμην', u'ἐπαιδεύου', u'ἐπαιδεύετο', u'ἐπαιδευόμεθα',
                u'ἐπαιδεύεσθε', u'ἐπαιδεύοντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    # FUTURE TENSE TESTS
    def test_future_ind_act(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'παιδεύσω', u'παιδεύσεις', u'παιδεύσει', u'παιδεύσομεν',
                u'παιδεύσετε', u'παιδεύσουσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_future_opt_act(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'παιδεύσοιμι', u'παιδεύσοις', u'παιδεύσοι', u'παιδεύσοιμεν',
                u'παιδεύσοιτε', u'παιδεύσοιεν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_future_inf_act(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = None
        args['number'] = None
        answer = u'παιδεύσειν'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(self.paideuw)
        self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_future_ind_mid(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'παιδεύσομαι', u'παιδεύσει', u'παιδεύσεται',
                u'παιδευσόμεθα', u'παιδεύσεσθε', u'παιδεύσονται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_future_opt_mid(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'παιδευσοίμην', u'παιδεύσοιο', u'παιδεύσοιτο',
                u'παιδευσοίμεθα', u'παιδεύσοισθε', u'παιδεύσοιντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(self.paideuw)
        for case, answer in zip(self.cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), answer)

    def test_future_inf_mid(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = None
        args['number'] = None
        answer = u'παιδεύσεσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(self.paideuw)
        self.failUnlessEqual(conj.conjugate(**args), answer)

    # AORIST TENSE TESTS
    # PERFECT TENSE TESTS
    # PLUPERFECT TENSE TESTS

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

