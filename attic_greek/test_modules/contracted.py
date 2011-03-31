#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.test import TestCase

from attic_greek.conjugation import GreekConjugation
from attic_greek.test_modules import verbs, cases
import unicodedata

class ContractedPoieoTest(TestCase):
    # PRESENT TENSE TESTS
    def test_poieo_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ποιῶ', u'ποιεῖς', u'ποιεῖ', u'ποιοῦμεν', u'ποιεῖτε',
                u'ποιοῦσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['poieo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_poieo_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'ποιῶ', u'ποιῇς', u'ποιῇ', u'ποιῶμεν', u'ποιῆτε',
                u'ποιῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['poieo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_poieo_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'ποιοῖμι', u'ποιοῖς', u'ποιοῖ', u'ποιοῖμεν', u'ποιοῖτε',
                u'ποιοῖεν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['poieo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_poieo_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'ποίει', u'ποιείτω', u'ποιεῖτε', u'ποιούντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['poieo'].word)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_poieo_present_inf_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ποιεῖν'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['poieo'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_poieo_present_ind_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ποιοῦμαι', u'ποιεῖ', u'ποιεῖται', u'ποιούμεθα',
                u'ποιεῖσθε', u'ποιοῦνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['poieo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_poieo_present_subj_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'ποιῶμαι', u'ποιῇ', u'ποιῆται', u'ποιώμεθα',
                u'ποιῆσθε', u'ποιῶνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['poieo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_poieo_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'ποιοίμην', u'ποιοῖο', u'ποιοῖτο', u'ποιοίμεθα',
                u'ποιοῖσθε', u'ποιοῖντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['poieo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_poieo_present_imp_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'ποιοῦ', u'ποιείσθω', u'ποιεῖσθε', u'ποιείσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['poieo'].word)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_poieo_present_inf_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ποιεῖσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['poieo'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_poieo_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐποίουν', u'ἐποίεις', u'ἐποίει', u'ἐποιοῦμεν',
                u'ἐποιεῖτε', u'ἐποίουν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['poieo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_poieo_imperfect_ind_mid(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐποιούμην', u'ἐποιοῦ', u'ἐποιεῖτο', u'ἐποιούμεθα',
                u'ἐποιεῖσθε', u'ἐποιοῦντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['poieo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


class ContractedNikaoTest(TestCase):
    # PRESENT TENSE TESTS
    def test_nikao_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'νικῶ', u'νικᾷς', u'νικᾷ', u'νικῶμεν', u'νικᾶτε',
                u'νικῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['nikao'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_nikao_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'νικῶ', u'νικᾷς', u'νικᾷ', u'νικῶμεν', u'νικᾶτε',
                u'νικῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['nikao'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_nikao_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'νικῷμι', u'νικῷς', u'νικῷ', u'νικῷμεν', u'νικῷτε',
                u'νικῷεν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['nikao'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_nikao_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'νίκα', u'νικάτω', u'νικᾶτε', u'νικώντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['nikao'].word)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_nikao_present_inf_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'νικᾶν'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['nikao'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_nikao_present_ind_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'νικῶμαι', u'νικᾷ', u'νικᾶται', u'νικώμεθα',
                u'νικᾶσθε', u'νικῶνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['nikao'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_nikao_present_subj_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'νικῶμαι', u'νικᾷ', u'νικᾶται', u'νικώμεθα',
                u'νικᾶσθε', u'νικῶνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['nikao'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_nikao_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'νικῴμην', u'νικῷο', u'νικῷτο', u'νικῴμεθα',
                u'νικῷσθε', u'νικῷντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['nikao'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_nikao_present_imp_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'νικῶ', u'νικάσθω', u'νικᾶσθε', u'νικάσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['nikao'].word)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_nikao_present_inf_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'νικᾶσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['nikao'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_nikao_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐνίκων', u'ἐνίκας', u'ἐνίκα', u'ἐνικῶμεν',
                u'ἐνικᾶτε', u'ἐνίκων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['nikao'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_nikao_imperfect_ind_mid(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐνικώμην', u'ἐνικῶ', u'ἐνικᾶτο', u'ἐνικώμεθα',
                u'ἐνικᾶσθε', u'ἐνικῶντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['nikao'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


class ContractedDhlooTest(TestCase):
    # PRESENT TENSE TESTS
    def test_dhloo_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'δηλῶ', u'δηλοῖς', u'δηλοῖ', u'δηλοῦμεν', u'δηλοῦτε',
                u'δηλοῦσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['dhloo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_dhloo_present_subj_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Active'
        answers = [u'δηλῶ', u'δηλοῖς', u'δηλοῖ', u'δηλῶμεν', u'δηλῶτε',
                u'δηλῶσι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['dhloo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_dhloo_present_opt_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Active'
        answers = [u'δηλοῖμι', u'δηλοῖς', u'δηλοῖ', u'δηλοῖμεν', u'δηλοῖτε',
                u'δηλοῖεν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['dhloo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_dhloo_present_imp_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Active'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'δήλου', u'δηλούτω', u'δηλοῦτε', u'δηλούντων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['dhloo'].word)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_dhloo_present_inf_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Active'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'δηλοῦν'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['dhloo'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_dhloo_present_ind_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'δηλοῦμαι', u'δηλοῖ', u'δηλοῦται', u'δηλούμεθα',
                u'δηλοῦσθε', u'δηλοῦνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['dhloo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_dhloo_present_subj_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Subjunctive'
        args['voice'] = 'Middle'
        answers = [u'δηλῶμαι', u'δηλοῖ', u'δηλῶται', u'δηλώμεθα',
                u'δηλῶσθε', u'δηλῶνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['dhloo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_dhloo_present_opt_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Optative'
        args['voice'] = 'Middle'
        answers = [u'δηλοίμην', u'δηλοῖο', u'δηλοῖτο', u'δηλοίμεθα',
                u'δηλοῖσθε', u'δηλοῖντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['dhloo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_dhloo_present_imp_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Imperative'
        args['voice'] = 'Middle'
        test_dicts = [{'person': 'Second Person', 'number': 'Singular'}]
        test_dicts.append({'person': 'Third Person', 'number': 'Singular'})
        test_dicts.append({'person': 'Second Person', 'number': 'Plural'})
        test_dicts.append({'person': 'Third Person', 'number': 'Plural'})
        answers = [u'δηλοῦ', u'δηλούσθω', u'δηλοῦσθε', u'δηλούσθων']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['dhloo'].word)
        for case, answer in zip(test_dicts, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_dhloo_present_inf_mid(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'δηλοῦσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['dhloo'].word)
        self.failUnlessEqual(conj.conjugate(**args), [answer])

    # IMPERFECT TENSE TESTS
    def test_dhloo_imperfect_ind_act(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Active'
        answers = [u'ἐδήλουν', u'ἐδήλους', u'ἐδήλου', u'ἐδηλοῦμεν',
                u'ἐδηλοῦτε', u'ἐδήλουν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['dhloo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_dhloo_imperfect_ind_mid(self):
        args = {}
        args['tense'] = 'Imperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐδηλούμην', u'ἐδηλοῦ', u'ἐδηλοῦτο', u'ἐδηλούμεθα',
                u'ἐδηλοῦσθε', u'ἐδηλοῦντο']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['dhloo'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


class ContractedFobeomaiTest(TestCase):
    """This is just a quick test to be sure deponent contractions work.
    """
    # PRESENT TENSE TESTS
    def test_fobeomai_present_ind_act(self):
        args = {}
        args['tense'] = 'Present'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle' # TODO: Should be deponent...
        answers = [u'φοβοῦμαι', u'φοβεῖ', u'φοβεῖται', u'φοβούμεθα',
                u'φοβεῖσθε', u'φοβοῦνται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['fobeomai'].word)
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


all_tests = [ContractedPoieoTest, ContractedNikaoTest, ContractedDhlooTest,
        ContractedFobeomaiTest]

# vim: et sw=4 sts=4
