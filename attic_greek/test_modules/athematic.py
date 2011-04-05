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

    def test_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'δίδου', u'διδότω', u'δίδοτε', u'διδόντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word, verbs['didomi'].id)
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

    def test_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'διδοίμην', u'διδοῖο', u'διδοῖτο', u'διδοίμεθα',
                u'διδοῖσθε', u'διδοῖντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
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
    def test_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐδίδουν', u'ἐδίδους', u'ἐδίδου', u'ἐδίδομεν',
                u'ἐδίδοτε', u'ἐδίδοσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word, verbs['didomi'].id)
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

    # AORIST TENSE TESTS
    def test_aorist_ind_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἔδωκα', u'ἔδωκας', u'ἔδωκε', u'ἔδομεν',
                u'ἔδοτε', u'ἔδοσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_subj_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'παιδεύσω', u'παιδεύσῃς', u'παιδεύσῃ', u'παιδεύσωμεν',
                u'παιδεύσητε', u'παιδεύσωσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['paideuo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'παιδεύσαιμι', u'παιδεύσαις', u'παιδεύσαι', u'παιδεύσαιμεν',
                u'παιδεύσαιτε', u'παιδεύσαιεν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['paideuo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'παίδευσον', u'παιδευσάτω', u'παιδεύσατε', u'παιδευσάντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['paideuo'].word)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_inf_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'παιδεῦσαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['paideuo'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_ind_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐδόμην', u'ἔδου', u'ἔδοτο',
                u'ἐδόμεθα', u'ἔδοσθε', u'ἔδοντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word, verbs['didomi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_subj_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'παιδεύσωμαι', u'παιδεύσῃ', u'παιδεύσηται', u'παιδευσώμεθα',
                u'παιδεύσησθε', u'παιδεύσωνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['paideuo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'παιδευσαίμην', u'παιδεύσαιο', u'παιδεύσαιτο',
                u'παιδευσαίμεθα', u'παιδεύσαισθε', u'παιδεύσαιντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['paideuo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_imp_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'παίδευσαι', u'παιδευσάσθω', u'παιδεύσασθε',
                u'παιδευσάσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['paideuo'].word)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_inf_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'παιδεύσασθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['paideuo'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])


class TithemiTest(TestCase):
    # PRESENT TENSE TESTS
    def test_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'τίθημι', u'τίθης', u'τίθησι', u'τίθεμεν',
                u'τίθετε', u'τιθέασι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'τιθῶ', u'τιθῇς', u'τιθῇ', u'τιθῶμεν',
                u'τιθῆτε', u'τιθῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'τιθείην', u'τιθείης', u'τιθείη', u'τιθείημεν',
                u'τιθείητε', u'τιθείησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'τίθει', u'τιθέτω', u'τίθετε', u'τιθέντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word, verbs['tithemi'].id)
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
        answer = u'τιθέναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['tithemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_ind_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'τίθεμαι', u'τίθεσαι', u'τίθεται', u'τιθέμεθα',
                u'τίθεσθε', u'τίθενται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'τιθῶμαι', u'τιθῇ', u'τιθῆται', u'τιθώμεθα',
                u'τιθῆσθε', u'τιθῶνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'τιθείμην', u'τιθεῖο', u'τιθεῖτο', u'τιθείμεθα',
                u'τιθεῖσθε', u'τιθεῖντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
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
        answers = [u'τίθεσο', u'τιθέσθω', u'τίθεσθε', u'τιθέσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
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
        answer = u'τίθεσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['tithemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐτίθην', u'ἐτίθεις', u'ἐτίθει', u'ἐτίθεμεν',
                u'ἐτίθετε', u'ἐτίθεσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word, verbs['tithemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_imperfect_ind_mid(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐτιθέμην', u'ἐτίθεσο', u'ἐτίθετο', u'ἐτιθέμεθα',
                u'ἐτίθεσθε', u'ἐτίθεντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


class HistemiTest(TestCase):
    # PRESENT TENSE TESTS
    def test_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἵστημι', u'ἵστης', u'ἵστησι', u'ἵσταμεν',
                u'ἵστατε', u'ἱστᾶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'ἱστῶ', u'ἱστῇς', u'ἱστῇ', u'ἱστῶμεν',
                u'ἱστῆτε', u'ἱστῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'ἱσταίην', u'ἱσταίης', u'ἱσταίη', u'ἱσταίημεν',
                u'ἱσταίητε', u'ἱσταίησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'ἵστη', u'ἱστάτω', u'ἵστατε', u'ἱστάντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
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
        answer = u'ἱστάναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['histemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_ind_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἵσταμαι', u'ἵστασαι', u'ἵσταται', u'ἱστάμεθα',
                u'ἵστασθε', u'ἵστανται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'ἱστῶμαι', u'ἱστῇ', u'ἱστῆται', u'ἱστώμεθα',
                u'ἱστῆσθε', u'ἱστῶνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'ἱσταίμην', u'ἱσταῖο', u'ἱσταῖτο', u'ἱσταίμεθα',
                u'ἱσταῖσθε', u'ἱσταῖντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word)
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
        answers = [u'ἵστασο', u'ἱστάσθω', u'ἵστασθε', u'ἱστάσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word)
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
        answer = u'ἵστασθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['histemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἵστην', u'ἵστης', u'ἵστη', u'ἵσταμεν',
                u'ἵστατε', u'ἵστασαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_imperfect_ind_mid(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἱστάμην', u'ἵστασο', u'ἵστατο', u'ἱστάμεθα',
                u'ἵστασθε', u'ἵσταντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


all_tests = [DidomiTest, TithemiTest, HistemiTest]

# vim: et sw=4 sts=4