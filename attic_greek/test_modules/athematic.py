#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from attic_greek import conjugation
from attic_greek.conjugation import AthematicConjugation
from attic_greek.conjugation import GreekConjugation
from attic_greek.test_modules import verbs, cases, imp_cases, GreekTestCase
import unicodedata

class DidomiTest(GreekTestCase):
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
        answers = [u'δίδου', u'διδότω', u'δίδοτε', u'διδόντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word, verbs['didomi'].id)
        for case, answer in zip(imp_cases, answers):
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
        answers = [u'δίδοσο', u'διδόσθω', u'δίδοσθε', u'διδόσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
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
        answers = [u'δῶ', u'δῷς', u'δῷ', u'δῶμεν',
                u'δῶτε', u'δῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'δοίην', u'δοίης', u'δοίη', u'δοίημεν',
                u'δοίητε', u'δοίησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_imp_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'δός', u'δότω', u'δότε', u'δόντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
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
        answer = u'δοῦναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['didomi'].word)
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
        answers = [u'δῶμαι', u'δῷ', u'δῶται', u'δώμεθα',
                u'δῶσθε', u'δῶνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'δοίμην', u'δοῖο', u'δοῖτο',
                u'δοίμεθα', u'δοῖσθε', u'δοῖντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_imp_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        answers = [u'δοῦ', u'δόσθω', u'δόσθε', u'δόσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['didomi'].word, verbs['didomi'].id)
        for case, answer in zip(imp_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_inf_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'δόσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['didomi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])


class TithemiTest(GreekTestCase):
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
        answers = [u'τίθει', u'τιθέτω', u'τίθετε', u'τιθέντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word, verbs['tithemi'].id)
        for case, answer in zip(imp_cases, answers):
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
        answers = [u'τίθεσο', u'τιθέσθω', u'τίθεσθε', u'τιθέσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
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

    # AORIST TENSE TESTS
    def test_aorist_ind_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἔθηκα', u'ἔθηκας', u'ἔθηκε', u'ἔθεμεν',
                u'ἔθετε', u'ἔθεσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_subj_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'θῶ', u'θῇς', u'θῇ', u'θῶμεν',
                u'θῆτε', u'θῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'θείην', u'θείης', u'θείη', u'θείημεν',
                u'θείητε', u'θείησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_imp_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'θές', u'θέτω', u'θέτε', u'θέντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
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
        answer = u'θεῖναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['tithemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_ind_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐθέμην', u'ἔθου', u'ἔθετο',
                u'ἐθέμεθα', u'ἔθεσθε', u'ἔθεντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word, verbs['tithemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_subj_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'θῶμαι', u'θῇ', u'θῆται', u'θώμεθα',
                u'θῆσθε', u'θῶνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'θείμην', u'θεῖο', u'θεῖτο',
                u'θείμεθα', u'θεῖσθε', u'θεῖντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_imp_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        answers = [u'θοῦ', u'θέσθω', u'θέσθε', u'θέσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['tithemi'].word, verbs['tithemi'].id)
        for case, answer in zip(imp_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_inf_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'θέσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['tithemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])


class HistemiTest(GreekTestCase):
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
        answers = [u'ἵστη', u'ἱστάτω', u'ἵστατε', u'ἱστάντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
        for case, answer in zip(imp_cases, answers):
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
        answers = [u'ἵστασο', u'ἱστάσθω', u'ἵστασθε', u'ἱστάσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word)
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

    # AORIST TENSE TESTS
    def test_aorist_ind_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἔστην', u'ἔστης', u'ἔστη', u'ἔστημεν',
                u'ἔστητε', u'ἔστησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_subj_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'στῶ', u'στῇς', u'στῇ', u'στῶμεν',
                u'στῆτε', u'στῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'σταίην', u'σταίης', u'σταίη', u'σταίημεν',
                u'σταίητε', u'σταίησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_imp_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'στῆθι', u'στήτω', u'στῆτε', u'στάντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
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
        answer = u'στῆναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['histemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # PERFECT TENSE TESTS
    def test_perfect_ind_act(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἕστηκα', u'ἕστηκας', u'ἕστηκε',
                u'ἕσταμεν', u'ἕστατε', u'ἑστᾶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_perfect_inf_act(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ἑστάναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # PLUPERFECT TENSE TESTS
    def test_pluperfect_ind_act(self):
        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'εἱστήκη', u'εἱστήκης', u'εἱστήκει',
                u'ἕσταμεν', u'ἕστατε', u'ἕστασαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['histemi'].word, verbs['histemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


class DeiknumiTest(GreekTestCase):
    # PRESENT TENSE TESTS
    def test_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'δείκνυμι', u'δείκνυς', u'δείκνυσι', u'δείκνυμεν',
                u'δείκνυτε', u'δεικνύασι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['deiknumi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'δεικνύω', u'δεικνύῃς', u'δεικνύῃ', u'δεικνύωμεν',
                u'δεικνύητε', u'δεικνύωσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['deiknumi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'δεικνύοιμι', u'δεικνύοις', u'δεικνύοι', u'δεικνύοιμεν',
                u'δεικνύοιτε', u'δεικνύοιεν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['deiknumi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'δείκνυ', u'δεικνύτω', u'δείκνυτε', u'δεικνύντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['deiknumi'].word,
                verbs['deiknumi'].id)
        for case, answer in zip(imp_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_inf_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'δεικνύναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['deiknumi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_ind_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'δείκνυμαι', u'δείκνυσαι', u'δείκνυται', u'δεικνύμεθα',
                u'δείκνυσθε', u'δείκνυνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['deiknumi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'δεικνύωμαι', u'δεικνύῃ', u'δεικνύηται', u'δεικνυώμεθα',
                u'δεικνύησθε', u'δεικνύωνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['deiknumi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'δεικνυοίμην', u'δεικνύοιο', u'δεικνύοιτο', u'δεικνυοίμεθα',
                u'δεικνύοισθε', u'δεικνύοιντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['deiknumi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        answers = [u'δείκνυσο', u'δεικνύσθω', u'δείκνυσθε', u'δεικνύσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['deiknumi'].word)
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
        answer = u'δείκνυσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['deiknumi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐδείκνυν', u'ἐδείκνυς', u'ἐδείκνυ', u'ἐδείκνυμεν',
                u'ἐδείκνυτε', u'ἐδείκνυσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['deiknumi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_imperfect_ind_mid(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐδεικνύμην', u'ἐδείκνυσο', u'ἐδείκνυτο', u'ἐδεικνύμεθα',
                u'ἐδείκνυσθε', u'ἐδείκνυντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['deiknumi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


class EimiTest(GreekTestCase):
    # PRESENT TENSE TESTS
    def test_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'εἰμί', u'εἶ', u'ἐστί', u'ἐσμέν',
                u'ἐστέ', u'εἰσί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['eimi'].word, verbs['eimi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'ὦ', u'ᾖς', u'ᾖ', u'ὦμεν',
                u'ἦτε', u'ὦσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['eimi'].word, verbs['eimi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'εἴην', u'εἴης', u'εἴη', u'εἴημεν', u'εἴητε', u'εἴησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['eimi'].word, verbs['eimi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'ἴσθι', u'ἔστω', u'ἔστε', u'ἔστων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['eimi'].word, verbs['eimi'].id)
        for case, answer in zip(imp_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_inf_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'εἶναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['eimi'].word, verbs['eimi'].id)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἦν', u'ἦσθα', u'ἦν', u'ἦμεν', u'ἦτε', u'ἦσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['eimi'].word, verbs['eimi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


class PhemiTest(GreekTestCase):
    # PRESENT TENSE TESTS
    def test_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'φημί', u'φῄς', u'φησί', u'φαμέν',
                u'φατέ', u'φασί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['phemi'].word, verbs['phemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'φῶ', u'φῇς', u'φῇ', u'φῶμεν',
                u'φῆτε', u'φῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['phemi'].word, verbs['phemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'φαίην', u'φαίης', u'φαίη', u'φαίημεν', u'φαίητε',
                u'φαίησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['phemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'φάθι', u'φάτω', u'φάτε', u'φάντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['phemi'].word)
        for case, answer in zip(imp_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_inf_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'φάναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['phemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἔφην', u'ἔφης', u'ἔφη', u'ἔφαμεν', u'ἔφατε', u'ἔφασαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['phemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


class EgnonTest(GreekTestCase):
    # AORIST TENSE TESTS
    def test_aorist_ind_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἔγνων', u'ἔγνως', u'ἔγνω', u'ἔγνωμεν',
                u'ἔγνωτε', u'ἔγνωσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['gignosko'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_subj_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'γνῶ', u'γνῷς', u'γνῷ', u'γνῶμεν',
                u'γνῶτε', u'γνῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['gignosko'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'γνοίην', u'γνοίης', u'γνοίη', u'γνοίημεν',
                u'γνοίητε', u'γνοίησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['gignosko'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_imp_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'γνῶθι', u'γνώτω', u'γνῶτε', u'γνόντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['gignosko'].word, verbs['gignosko'].id)
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
        answer = u'γνῶναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['gignosko'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])


class Eimi2Test(GreekTestCase):
    # PRESENT TENSE TESTS
    def test_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'εἶμι', u'εἶ', u'εἶσι', u'ἴμεν',
                u'ἴτε', u'ἴασι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['eimi2'].word, verbs['eimi2'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'ἴω', u'ἴῃς', u'ἴῃ', u'ἴωμεν', u'ἴητε', u'ἴωσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['eimi2'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'ἴοιμι', u'ἴοις', u'ἴοι', u'ἴοιμεν', u'ἴοιτε', u'ἴοιεν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['eimi2'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'ἴθι', u'ἴτω', u'ἴτε', u'ἰόντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['eimi2'].word, verbs['eimi2'].id)
        for case, answer in zip(imp_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_inf_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ἰέναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['eimi2'].word, verbs['eimi2'].id)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ᾔειν', u'ᾔεις', u'ᾔει', u'ᾖμεν', u'ᾖτε', u'ᾖσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['eimi2'].word, verbs['eimi2'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


class HiemiTest(GreekTestCase):
    # PRESENT TENSE TESTS
    def test_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἵημι', u'ἵης', u'ἵησι', u'ἵεμεν',
                u'ἵετε', u'ἱᾶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word, verbs['hiemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'ἱῶ', u'ἱῇς', u'ἱῇ', u'ἱῶμεν',
                u'ἱῆτε', u'ἱῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'ἱείην', u'ἱείης', u'ἱείη', u'ἱείημεν',
                u'ἱείητε', u'ἱείησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'ἵει', u'ἱέτω', u'ἵετε', u'ἱέντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word, verbs['hiemi'].id)
        for case, answer in zip(imp_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_inf_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ἱέναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['hiemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_ind_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἵεμαι', u'ἵεσαι', u'ἵεται', u'ἱέμεθα',
                u'ἵεσθε', u'ἵενται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_subj_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'ἱῶμαι', u'ἱῇ', u'ἱῆται', u'ἱώμεθα',
                u'ἱῆσθε', u'ἱῶνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'ἱείμην', u'ἱεῖο', u'ἱεῖτο', u'ἱείμεθα',
                u'ἱεῖσθε', u'ἱεῖντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_present_imp_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        answers = [u'ἵεσο', u'ἱέσθω', u'ἵεσθε', u'ἱέσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
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
        answer = u'ἵεσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['hiemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἵην', u'ἵεις', u'ἵει', u'ἵεμεν',
                u'ἵετε', u'ἵεσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word, verbs['hiemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_imperfect_ind_mid(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἱέμην', u'ἵεσο', u'ἵετο', u'ἱέμεθα',
                u'ἵεσθε', u'ἵεντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    # AORIST TENSE TESTS
    def test_aorist_ind_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἧκα', u'ἧκας', u'ἧκε', u'εἷμεν',
                u'εἷτε', u'εἷσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word, verbs['hiemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_subj_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'ὧ', u'ᾗς', u'ᾗ', u'ὧμεν',
                u'ἧτε', u'ὧσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'εἵην', u'εἵης', u'εἵη', u'εἵημεν',
                u'εἵητε', u'εἵησαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_imp_act(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        answers = [u'ἕς', u'ἕτω', u'ἕτε', u'ἕντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
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
        answer = u'εἷναι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['hiemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_ind_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'εἵμην', u'εἷσο', u'εἷτο',
                u'εἵμεθα', u'εἷσθε', u'εἷντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word, verbs['hiemi'].id)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_subj_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'ὧμαι', u'ᾗ', u'ἧται', u'ὥμεθα',
                u'ἧσθε', u'ὧνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_opt_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'εἵμην', u'εἷο', u'εἷτο',
                u'εἵμεθα', u'εἷσθε', u'εἷντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_imp_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        answers = [u'οὗ', u'ἕσθω', u'ἕσθε', u'ἕσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = AthematicConjugation(verbs['hiemi'].word, verbs['hiemi'].id)
        for case, answer in zip(imp_cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aorist_inf_mid(self):
        args = {}
        args['tense'] = 'Aorist'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ἕσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = AthematicConjugation(verbs['hiemi'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])


all_tests = [DidomiTest, TithemiTest, HistemiTest, DeiknumiTest, EimiTest,
        PhemiTest, EgnonTest, Eimi2Test, HiemiTest]

# vim: et sw=4 sts=4
