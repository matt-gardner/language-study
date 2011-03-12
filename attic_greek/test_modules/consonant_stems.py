#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.test import TestCase

from attic_greek.conjugation import GreekConjugation
from attic_greek.test_modules import verbs, cases
import unicodedata

class ConsonantStemsTest(TestCase):
    def test_grafo(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'γέγραμμαι', u'γέγραψαι', u'γέγραπται', u'γεγράμμεθα',
                u'γέγραφθε', u'γεγραμμένοι εἰσί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['grafo'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'γεγράφθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['grafo'])
        self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐγεγράμμην', u'ἐγέγραψο', u'ἐγέγραπτο', u'ἐγεγράμμεθα',
                u'ἐγέγραφθε', u'γεγραμμένοι ἦσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['grafo'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_pempo(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'πέπεμμαι', u'πέπεμψαι', u'πέπεμπται', u'πεπέμμεθα',
                u'πέπεμφθε', u'πεπεμμένοι εἰσί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['pempo'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'πεπέμφθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['pempo'])
        self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐπεπέμμην', u'ἐπέπεμψο', u'ἐπέπεμπτο', u'ἐπεπέμμεθα',
                u'ἐπέπεμφθε', u'πεπεμμένοι ἦσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['pempo'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aischunomai(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ᾔσχυμμαι', u'ᾐσχυμμένος εἶ', u'ᾔσχυνται', u'ᾐσχύμμεθα',
                u'ᾔσχυνθε', u'ᾐσχυμμένοι εἰσί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['aischunomai'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ᾐσχύνθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['aischunomai'])
        self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ᾐσχύμμην', u'ᾐσχυμμένος ἦσθα', u'ᾔσχυντο', u'ᾐσχύμμεθα',
                u'ᾔσχυνθε', u'ᾐσχυμμένοι ἦσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['aischunomai'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_tatto(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'τέταγμαι', u'τέταξαι', u'τέτακται', u'τετάγμεθα',
                u'τέταχθε', u'τεταγμένοι εἰσί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['tatto'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'τετάχθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['tatto'])
        self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐτετάγμην', u'ἐτέταξο', u'ἐτέτακτο', u'ἐτετάγμεθα',
                u'ἐτέταχθε', u'τεταγμένοι ἦσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['tatto'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_elegxo(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐλήλεγμαι', u'ἐλήλεγξαι', u'ἐλήλεγκται', u'ἐληλέγμεθα',
                u'ἐλήλεγχθε', u'ἐληλεγμένοι εἰσί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['elegxo'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ἐληλέγχθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['elegxo'])
        self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐληλέγμην', u'ἐλήλεγξο', u'ἐλήλεγκτο', u'ἐληλέγμεθα',
                u'ἐλήλεγχθε', u'ἐληλεγμένοι ἦσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['elegxo'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_keleuo(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'κεκέλευσμαι', u'κεκέλευσαι', u'κεκέλευσται',
                u'κεκελεύσμεθα', u'κεκέλευσθε', u'κεκελευσμένοι εἰσί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['keleuo'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'κεκελεῦσθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['keleuo'])
        self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐκεκελεύσμην', u'ἐκεκέλευσο', u'ἐκεκέλευστο',
                u'ἐκεκελεύσμεθα', u'ἐκεκέλευσθε', u'κεκελευσμένοι ἦσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['keleuo'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_faino(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'πέφασμαι', u'πεφασμένος εἶ', u'πέφανται',
                u'πεφάσμεθα', u'πέφανθε', u'πεφασμένοι εἰσί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['faino'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'πεφάνθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['faino'])
        self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἐπεφάσμην', u'πεφασμένος ἦσθα', u'ἐπέφαντο',
                u'ἐπεφάσμεθα', u'ἐπέφανθε', u'πεφασμένοι ἦσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['faino'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

    def test_aggello(self):
        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἤγγελμαι', u'ἤγγελσαι', u'ἤγγελται',
                u'ἠγγέλμεθα', u'ἤγγελθε', u'ἠγγελμένοι εἰσί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['aggello'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Perfect'
        args['mood'] = 'Infinitive'
        args['voice'] = 'Middle'
        args['person'] = 'None'
        args['number'] = 'None'
        answer = u'ἠγγέλθαι'
        answer = unicodedata.normalize('NFKD', answer)
        conj = GreekConjugation(verbs['aggello'])
        self.failUnlessEqual(conj.conjugate(**args), [answer])

        args = {}
        args['tense'] = 'Pluperfect'
        args['mood'] = 'Indicative'
        args['voice'] = 'Middle'
        answers = [u'ἠγγέλμην', u'ἤγγελσο', u'ἤγγελτο',
                u'ἠγγέλμεθα', u'ἤγγελθε', u'ἠγγελμένοι ἦσαν']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        conj = GreekConjugation(verbs['aggello'])
        for case, answer in zip(cases, answers):
            args.update(case)
            self.failUnlessEqual(conj.conjugate(**args), [answer])


all_tests = [ConsonantStemsTest]

# vim: et sw=4 sts=4
