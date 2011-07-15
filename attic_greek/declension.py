#!/usr/bin/env python
# -*- encoding: utf-8 -*-

verbose = False

from greek_util import remove_all_combining
from noun_endings import *

# TODO: this belongs somewhere else
class Declension(object):
    def __init__(self):
        pass

    def decline(self, **kwargs):
        raise NotImplementedError()


class FirstDeclensionNoun(Declension):
    def __init__(self, dictionary_entry, word_id=-1):
        self.dictionary_entry = dictionary_entry
        self.word_id = word_id
        entry_parts = dictionary_entry.split(', ')
        if len(entry_parts) == 1:
            # TODO: try to handle this case?
            pass
        elif len(entry_parts) == 2:
            # TODO: try to handle this case?
            pass
        elif len(entry_parts) == 3:
            self.nominative, self.genitive, article = entry_parts
            if remove_all_combining(article) == u'ο':
                self.gender = 'Masculine'
            if remove_all_combining(article) == u'η':
                self.gender = 'Feminine'
            if remove_all_combining(article) == u'το':
                self.gender = 'Neuter'
        else:
            raise ValueError("I don't know how to handle the dictionary entry "
                    "you gave me")
        self.cache_database_stuff()
        self.set_endings()

    def cache_database_stuff(self):
        pass

    def set_endings(self):
        if self.genitive.endswith(u'ης'):
            self.endings = FirstDeclensionFeminineEta()
        elif self.genitive.endswith(u'ας'):
            self.endings = FirstDeclensionFeminineAlpha()
        else:
            raise ValueError("I don't know what set of endings to use for this "
                    "word")

    def decline(self, **kwargs):
        case, number = self.check_kwargs(kwargs)
        if case == 'Nominative' and number == 'Singular':
            return self.nominative
        if case == 'Genitive' and number == 'Singular':
            return self.genitive
        stem = self.get_stem()
        ending = self.endings[case][number]
        final_form = self.combine_parts(stem, ending)
        return final_form

    def check_kwargs(self, kwargs):
        if 'case' not in kwargs:
            raise ValueError("Case must be specified")
        case = kwargs['case']
        if 'number' not in kwargs:
            raise ValueError("Number must be specified")
        number = kwargs['number']
        return case, number

    def get_stem(self):
        ending = self.endings['Genitive']['Singular']
        return self.genitive[:-len(ending)]

    def combine_parts(self, stem, ending):
        return stem + ending

if __name__ == '__main__':
    # Some very simple testing, as I'm developing stuff.  More complicated
    # tests to come, and go in the test_modules directoy.
    texne = u'τέχνη, τέχνης, ἡ'
    d = FirstDeclensionNoun(texne)
    cases = ['Nominative', 'Genitive', 'Dative', 'Accusative', 'Vocative']
    numbers = ['Singular', 'Plural']
    for number in numbers:
        for case in cases:
            print case, number
            print d.decline(case=case, number=number)

# vim: et sw=4 sts=4
