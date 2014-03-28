#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os, sys
sys.path.append(os.getcwd()+'/../..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'
from language_study.drills.views.vocab import parse_definition_from_html

import unittest

class TestParser(unittest.TestCase):
    def test_parser(self):
        for test in self.tests:
            definition = parse_definition_from_html(test.text())
            for must_have in test.must_have:
                self.assertIn(must_have, definition)
            for must_not_have in test.must_not_have:
                self.assertNotIn(must_not_have, definition)


    def setUp(self):
        self.tests = [
                Test('files/sment.html',
                     [u'šment', 'devil', 'deuce'],
                     []),
                ]


class Test(object):
    def __init__(self, filename, must_have, must_not_have):
        self.filename = filename
        self.must_have = must_have
        self.must_not_have = must_not_have

    def text(self):
        return open(self.filename).read()


if __name__ == '__main__':
    unittest.main()

# vim: et sw=4 sts=4
