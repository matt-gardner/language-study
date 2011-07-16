#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from attic_greek.declension import GreekDeclension
from attic_greek.test_modules import nouns, decl_cases, GreekTestCase
import unicodedata

class RegularFirstDeclensionTest(GreekTestCase):
    def test_techne(self):
        args = {}
        answers = [u'τέχνη', u'τέχνης', u'τέχνῃ', u'τέχνην', u'τέχνη',
                u'τέχναι', u'τεχνῶν', u'τέχναις', u'τέχνας', u'τέχναι']
        answers = [unicodedata.normalize('NFKD', word) for word in answers]
        noun = GreekDeclension(nouns['techne'].word.word)
        for case, answer in zip(decl_cases, answers):
            args.update(case)
            print answer, noun.decline(**args)
            self.failUnlessEqual(noun.decline(**args), answer)

all_tests = [RegularFirstDeclensionTest]

# vim: et sw=4 sts=4