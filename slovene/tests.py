#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unittest

from slovene.test_modules import all_tests

def suite():
    suites = []
    for test in all_tests:
        s = unittest.TestLoader().loadTestsFromTestCase(test)
        suites.append(s)
    return unittest.TestSuite(suites)

# vim: et sw=4 sts=4
