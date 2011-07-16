#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from attic_greek import conjugation
from attic_greek.conjugation import GreekConjugation
from attic_greek.test_modules import verbs, verb_cases, imp_cases, GreekTestCase
import unicodedata

class ErxomaiTest(GreekTestCase):
    # PRESENT TENSE TESTS
    def test_present_ind_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἔρχομαι', u'ἔρχει', u'ἔρχεται', u'ἐρχόμεθα',
                u'ἔρχεσθε', u'ἔρχονται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'ἔρχωμαι', u'ἔρχῃ', u'ἔρχηται', u'ἐρχώμεθα',
                u'ἔρχησθε', u'ἔρχωνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'ἐρχοίμην', u'ἔρχοιο', u'ἔρχοιτο', u'ἐρχοίμεθα',
                u'ἔρχοισθε', u'ἔρχοιντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        answers = [u'ἔρχου', u'ἐρχέσθω', u'ἔρχεσθε', u'ἐρχέσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(imp_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_inf_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ἔρχεσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['erxomai'].word.word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_imperfect_ind_mid(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἠρχόμην', u'ἤρχου', u'ἤρχετο', u'ἠρχόμεθα',
                u'ἤρχεσθε', u'ἤρχοντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    # FUTURE TENSE TESTS
    def test_future_ind_mid(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐλεύσομαι', u'ἐλεύσει', u'ἐλεύσεται',
                u'ἐλευσόμεθα', u'ἐλεύσεσθε', u'ἐλεύσονται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_future_opt_mid(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'ἐλευσοίμην', u'ἐλεύσοιο', u'ἐλεύσοιτο',
                u'ἐλευσοίμεθα', u'ἐλεύσοισθε', u'ἐλεύσοιντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_future_inf_mid(self):
        args = {}
        args['tense'] = 'Future'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ἐλεύσεσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['erxomai'].word.word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # AORIST TENSE TESTS
    def test_aorist_ind_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἦλθον', u'ἦλθες', u'ἦλθε', u'ἤλθομεν',
                u'ἤλθετε', u'ἦλθον']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_subj_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'ἔλθω', u'ἔλθῃς', u'ἔλθῃ', u'ἔλθωμεν',
                u'ἔλθητε', u'ἔλθωσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'ἔλθοιμι', u'ἔλθοις', u'ἔλθοι', u'ἔλθοιμεν',
                u'ἔλθοιτε', u'ἔλθοιεν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_imp_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'ἔλθε', u'ἐλθέτω', u'ἔλθετε', u'ἐλθόντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(imp_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_inf_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ἐλθεῖν'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['erxomai'].word.word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # PERFECT TENSE TESTS
    def test_perfect_ind_act(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐλήλυθα', u'ἐλήλυθας', u'ἐλήλυθε',
                u'ἐληλύθαμεν', u'ἐληλύθατε', u'ἐληλύθασι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_perfect_inf_act(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ἐληλυθέναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['erxomai'].word.word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # PLUPERFECT TENSE TESTS
    def test_pluperfect_ind_act(self):
        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐληλύθη', u'ἐληλύθης', u'ἐληλύθει',
                u'ἐληλύθεμεν', u'ἐληλύθετε', u'ἐληλύθεσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['erxomai'].word.word)
        for case, answer in zip(verb_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


all_tests = [ErxomaiTest]

# vim: et sw=4 sts=4
