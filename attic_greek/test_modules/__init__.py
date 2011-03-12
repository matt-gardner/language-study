#!/usr/bin/env python

from attic_greek.test_modules import consonant_stems
from attic_greek.test_modules import contracted
from attic_greek.test_modules import contracted_future
from attic_greek.test_modules import regular

all_tests = []
all_tests.extend(consonant_stems.all_tests)
all_tests.extend(contracted.all_tests)
all_tests.extend(contracted_future.all_tests)
all_tests.extend(regular.all_tests)

# vim: et sw=4 sts=4
