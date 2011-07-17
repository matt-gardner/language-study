#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from attic_greek import declension
from attic_greek.declension import GreekAdjectiveDeclension
from attic_greek.test_modules import adjectives, decl_cases, GreekTestCase
import unicodedata

class RegularSecondDeclensionTest(GreekTestCase):
    def test_agathos_masculine(self):
        args = {'gender': 'Masculine'}
        answers = [u'ἀγαθός', u'ἀγαθοῦ', u'ἀγαθῷ', u'ἀγαθόν', u'ἀγαθέ',
                u'ἀγαθοί', u'ἀγαθῶν', u'ἀγαθοῖς', u'ἀγαθούς', u'ἀγαθοί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        adj = GreekAdjectiveDeclension(adjectives['agathos'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(adj.decline(**args), answer)

    def test_agathos_feminine(self):
        args = {'gender': 'Feminine'}
        answers = [u'ἀγαθή', u'ἀγαθῆς', u'ἀγαθῇ', u'ἀγαθήν', u'ἀγαθή',
                u'ἀγαθαί', u'ἀγαθῶν', u'ἀγαθαῖς', u'ἀγαθάς', u'ἀγαθαί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        adj = GreekAdjectiveDeclension(adjectives['agathos'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(adj.decline(**args), answer)

    def test_agathos_neuter(self):
        args = {'gender': 'Neuter'}
        answers = [u'ἀγαθόν', u'ἀγαθοῦ', u'ἀγαθῷ', u'ἀγαθόν', u'ἀγαθόν',
                u'ἀγαθά', u'ἀγαθῶν', u'ἀγαθοῖς', u'ἀγαθά', u'ἀγαθά']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        adj = GreekAdjectiveDeclension(adjectives['agathos'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(adj.decline(**args), answer)

    def test_axios_masculine(self):
        args = {'gender': 'Masculine'}
        answers = [u'ἄξιος', u'ἀξίου', u'ἀξίῳ', u'ἄξιον', u'ἄξιε',
                u'ἄξιοι', u'ἀξίων', u'ἀξίοις', u'ἀξίους', u'ἄξιοι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        adj = GreekAdjectiveDeclension(adjectives['axios'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(adj.decline(**args), answer)

    def test_axios_feminine(self):
        args = {'gender': 'Feminine'}
        answers = [u'ἀξία', u'ἀξίας', u'ἀξίᾳ', u'ἀξίαν', u'ἀξία',
                u'ἄξιαι', u'ἀξίων', u'ἀξίαις', u'ἀξίας', u'ἄξιαι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        adj = GreekAdjectiveDeclension(adjectives['axios'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(adj.decline(**args), answer)

    def test_axios_neuter(self):
        args = {'gender': 'Neuter'}
        answers = [u'ἄξιον', u'ἀξίου', u'ἀξίῳ', u'ἄξιον', u'ἄξιον',
                u'ἄξια', u'ἀξίων', u'ἀξίοις', u'ἄξια', u'ἄξια']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        adj = GreekAdjectiveDeclension(adjectives['axios'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(adj.decline(**args), answer)

    def test_adikos_masculine(self):
        args = {'gender': 'Masculine'}
        answers = [u'ἄδικος', u'ἀδίκου', u'ἀδίκῳ', u'ἄδικον', u'ἄδικε',
                u'ἄδικοι', u'ἀδίκων', u'ἀδίκοις', u'ἀδίκους', u'ἄδικοι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        adj = GreekAdjectiveDeclension(adjectives['adikos'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(adj.decline(**args), answer)

    def test_adikos_feminine(self):
        args = {'gender': 'Feminine'}
        answers = [u'ἄδικος', u'ἀδίκου', u'ἀδίκῳ', u'ἄδικον', u'ἄδικε',
                u'ἄδικοι', u'ἀδίκων', u'ἀδίκοις', u'ἀδίκους', u'ἄδικοι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        adj = GreekAdjectiveDeclension(adjectives['adikos'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(adj.decline(**args), answer)

    def test_adikos_neuter(self):
        args = {'gender': 'Neuter'}
        answers = [u'ἄδικον', u'ἀδίκου', u'ἀδίκῳ', u'ἄδικον', u'ἄδικον',
                u'ἄδικα', u'ἀδίκων', u'ἀδίκοις', u'ἄδικα', u'ἄδικα']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        adj = GreekAdjectiveDeclension(adjectives['adikos'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(adj.decline(**args), answer)


all_tests = [RegularSecondDeclensionTest]

# vim: et sw=4 sts=4
