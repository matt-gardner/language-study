#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from attic_greek import declension
from attic_greek.declension import FirstDeclensionNoun
from attic_greek.declension import SecondDeclensionNoun
from attic_greek.test_modules import nouns, decl_cases, GreekTestCase
import unicodedata

class RegularFirstDeclensionTest(GreekTestCase):
    # FEMININE TESTS
    def test_techne(self):
        args = {}
        answers = [u'τέχνη', u'τέχνης', u'τέχνῃ', u'τέχνην', u'τέχνη',
                u'τέχναι', u'τεχνῶν', u'τέχναις', u'τέχνας', u'τέχναι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['techne'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_chora(self):
        args = {}
        answers = [u'χώρα', u'χώρας', u'χώρᾳ', u'χώραν', u'χώρα',
                u'χῶραι', u'χωρῶν', u'χώραις', u'χώρας', u'χῶραι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['chora'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_psuche(self):
        args = {}
        answers = [u'ψυχή', u'ψυχῆς', u'ψυχῇ', u'ψυχήν', u'ψυχή',
                u'ψυχαί', u'ψυχῶν', u'ψυχαῖς', u'ψυχάς', u'ψυχαί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['psuche'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_agora(self):
        args = {}
        answers = [u'ἀγορά', u'ἀγορᾶς', u'ἀγορᾷ', u'ἀγοράν', u'ἀγορά',
                u'ἀγοραί', u'ἀγορῶν', u'ἀγοραῖς', u'ἀγοράς', u'ἀγοραί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['agora'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    # SHORT ALPHA TESTS
    def test_thalatta(self):
        args = {}
        answers = [u'θάλαττα', u'θαλάττης', u'θαλάττῃ', u'θάλατταν', u'θάλαττα',
                u'θάλατται', u'θαλαττῶν', u'θαλάτταις', u'θαλάττας',
                u'θάλατται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['thalatta'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_mousa(self):
        args = {}
        answers = [u'μοῦσα', u'μούσης', u'μούσῃ', u'μοῦσαν', u'μοῦσα',
                u'μοῦσαι', u'μουσῶν', u'μούσαις', u'μούσας', u'μοῦσαι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['mousa'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_gephura(self):
        args = {}
        answers = [u'γέφυρα', u'γεφύρας', u'γεφύρᾳ', u'γέφυραν', u'γέφυρα',
                u'γέφυραι', u'γεφυρῶν', u'γεφύραις', u'γεφύρας', u'γέφυραι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['gephura'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_moira(self):
        args = {}
        answers = [u'μοῖρα', u'μοίρας', u'μοίρᾳ', u'μοῖραν', u'μοῖρα',
                u'μοῖραι', u'μοιρῶν', u'μοίραις', u'μοίρας', u'μοῖραι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['moira'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    # MASCULINE TESTS
    def test_polites(self):
        args = {}
        answers = [u'πολίτης', u'πολίτου', u'πολίτῃ', u'πολίτην', u'πολῖτα',
                u'πολῖται', u'πολιτῶν', u'πολίταις', u'πολίτας', u'πολῖται']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['polites'].word.word,
                nouns['polites'].id)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_poietes(self):
        args = {}
        answers = [u'ποιητής', u'ποιητοῦ', u'ποιητῇ', u'ποιητήν', u'ποιητά',
                u'ποιηταί', u'ποιητῶν', u'ποιηταῖς', u'ποιητάς', u'ποιηταί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['poietes'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_neanias(self):
        args = {}
        answers = [u'νεανίας', u'νεανίου', u'νεανίᾳ', u'νεανίαν', u'νεανία',
                u'νεανίαι', u'νεανιῶν', u'νεανίαις', u'νεανίας', u'νεανίαι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = FirstDeclensionNoun(nouns['neanias'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)


class RegularSecondDeclensionTest(GreekTestCase):
    def test_logos(self):
        args = {}
        answers = [u'λόγος', u'λόγου', u'λόγῳ', u'λόγον', u'λόγε',
                u'λόγοι', u'λόγων', u'λόγοις', u'λόγους', u'λόγοι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = SecondDeclensionNoun(nouns['logos'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_ergon(self):
        args = {}
        answers = [u'ἔργον', u'ἔργου', u'ἔργῳ', u'ἔργον', u'ἔργον',
                u'ἔργα', u'ἔργων', u'ἔργοις', u'ἔργα', u'ἔργα']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = SecondDeclensionNoun(nouns['ergon'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_anthropos(self):
        args = {}
        answers = [u'ἄνθρωπος', u'ἀνθρώπου', u'ἀνθρώπῳ', u'ἄνθρωπον',
                u'ἄνθρωπε', u'ἄνθρωποι', u'ἀνθρώπων', u'ἀνθρώποις',
                u'ἀνθρώπους', u'ἄνθρωποι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = SecondDeclensionNoun(nouns['anthropos'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_adelphos(self):
        args = {}
        answers = [u'ἀδελφός', u'ἀδελφοῦ', u'ἀδελφῷ', u'ἀδελφόν', u'ἄδελφε',
                u'ἀδελφοί', u'ἀδελφῶν', u'ἀδελφοῖς', u'ἀδελφούς', u'ἀδελφοί']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = SecondDeclensionNoun(nouns['adelphos'].word.word,
                nouns['adelphos'].id)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_nesos(self):
        args = {}
        answers = [u'νῆσος', u'νήσου', u'νήσῳ', u'νῆσον', u'νῆσε',
                u'νῆσοι', u'νήσων', u'νήσοις', u'νήσους', u'νῆσοι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = SecondDeclensionNoun(nouns['nesos'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_doron(self):
        args = {}
        answers = [u'δῶρον', u'δώρου', u'δώρῳ', u'δῶρον', u'δῶρον',
                u'δῶρα', u'δώρων', u'δώροις', u'δῶρα', u'δῶρα']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = SecondDeclensionNoun(nouns['doron'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)


all_tests = [RegularFirstDeclensionTest, RegularSecondDeclensionTest]

# vim: et sw=4 sts=4
