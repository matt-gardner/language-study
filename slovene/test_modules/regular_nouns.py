#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from slovene import declension
from slovene.declension import FirstDeclensionNoun
from slovene.declension import SecondDeclensionNoun
from slovene.declension import ThirdDeclensionNoun
from slovene.declension import FourthDeclensionNoun
from slovene.test_modules import nouns, decl_cases, SloveneTestCase

class RegularFirstDeclensionTest(SloveneTestCase):
    def test_ucenec(self):
        declension.verbose = True
        args = {}
        answers = [u'učenec', u'učenca', u'učenci',
                u'učenca', u'učencev', u'učencev',
                u'učencu', u'učencema', u'učencem',
                u'učenca', u'učenca', u'učence',
                u'učencu', u'učencih', u'učencih',
                u'učencem', u'učencema', u'učenci']
        noun = FirstDeclensionNoun(nouns['ucenec'].word.word,
                nouns['ucenec'].id)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)

    def test_potnik(self):
        args = {}
        answers = [u'potnik', u'potnika', u'potniki',
                u'potnika', u'potnikov', u'potnikov',
                u'potniku', u'potnikoma', u'potnikom',
                u'potnika', u'potnika', u'potnike',
                u'potniku', u'potnikih', u'potnikih',
                u'potnikom', u'potnikoma', u'potniki']
        noun = FirstDeclensionNoun(nouns['potnik'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)


class RegularSecondDeclensionTest(SloveneTestCase):
    def test_punca(self):
        args = {}
        answers = [u'punca', u'punci', u'punce',
                u'punce', u'punc', u'punc',
                u'punci', u'puncama', u'puncam',
                u'punco', u'punci', u'punce',
                u'punci', u'puncah', u'puncah',
                u'punco', u'puncama', u'puncami']
        noun = SecondDeclensionNoun(nouns['punca'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            self.failUnlessEqual(noun.decline(**args), answer)


class RegularThirdDeclensionTest(SloveneTestCase):
    pass

class RegularFourthDeclensionTest(SloveneTestCase):
    pass

all_tests = [RegularFirstDeclensionTest, RegularSecondDeclensionTest,
        RegularThirdDeclensionTest, RegularFourthDeclensionTest]

# vim: et sw=4 sts=4
