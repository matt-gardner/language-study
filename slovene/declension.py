#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from language_study.drills.models import DeclinableWord
from language_study.slovene.models import *

from noun_endings import *
from util.base import log_if_verbose

verbose = False

# TODO: this belongs somewhere else
class Declension(object):
    def __init__(self):
        pass

    def decline(self, **kwargs):
        raise NotImplementedError()


class SloveneDeclension(Declension):
    # Common methods
    def __init__(self, dictionary_entry, word_id=-1):
        self.dictionary_entry = dictionary_entry
        self.word_id = word_id
        self.cache_database_stuff()
        self.process_dictionary_entry()
        self.set_gender()
        self.set_endings()

    def process_dictionary_entry(self):
        pass

    def cache_database_stuff(self):
        self.fleeting_vowel = False
        self.animate = False
        self.irregular_forms = dict()
        if self.word_id == -1:
            return
        word = DeclinableWord.objects.get(pk=self.word_id)
        irregular_forms = word.irregulardeclinableform_set.all()
        for irreg in irregular_forms:
            g = irreg.gender.name
            n = irreg.number.name
            c = irreg.case.name
            form = unicodedata.normalize('NFKD', irreg.form)
            self.irregular_forms[(g, n, c)] = form
        try:
            word.animate
            self.animate = True
        except Animate.DoesNotExist:
            pass
        try:
            word.fleetingvowel
            self.fleeting_vowel = True
        except FleetingVowel.DoesNotExist:
            pass

    def check_kwargs(self, kwargs):
        if 'case' not in kwargs:
            raise ValueError("Case must be specified")
        case = kwargs['case']
        if 'number' not in kwargs:
            raise ValueError("Number must be specified")
        number = kwargs['number']
        if self.gender:
            gender = self.gender
            if 'gender' in kwargs and kwargs['gender'] != self.gender:
                raise ValueError("Incorrect gender given")
        else:
            if 'gender' not in kwargs:
                raise ValueError("Gender must be specified")
            gender = kwargs['gender']
        return gender, number, case

    def decline(self, **kwargs):
        gender, number, case = self.check_kwargs(kwargs)
        if (gender, number, case) in self.irregular_forms:
            return self.irregular_forms[(gender, number, case)]
        stem = self.get_stem(gender, number, case)
        ending = self.get_ending(gender, number, case)
        return self.combine_parts(stem, ending)

    def combine_parts(self, stem, ending):
        if self.fleeting_vowel and ending:
            stem = self.remove_fleeting_vowel(stem)
        return stem + ending

    def remove_fleeting_vowel(self, stem):
        # We assume that the fleeting vowel is always the second to last
        # character, and only a single character.  It's possible that this
        # could be wrong in some corner cases.
        return stem[:-2] + stem[-1]

    # Methods to be overridden
    def set_gender(self):
        raise NotImplementedError()

    def set_endings(self):
        raise NotImplementedError()

    def get_stem(self, gender, number, case):
        raise NotImplementedError()

    def get_ending(self, gender, number, case):
        raise NotImplementedError()


class SloveneNounDeclension(SloveneDeclension):
    def get_stem(self, gender, number, case):
        ending = self.endings['Nominative']['Singular']
        if ending:
            stem = self.dictionary_entry[:-len(ending)]
        else:
            stem = self.dictionary_entry
        return stem

    def get_ending(self, gender, number, case):
        return self.endings[case][number]


class FirstDeclensionNoun(SloveneNounDeclension):
    def set_gender(self):
        self.gender = 'Masculine'

    def set_endings(self):
        if self.dictionary_entry[-1] in [u'c', u'č', u'š', u'ž', u'j']:
            self.endings = FirstDeclensionNounEndingsE()
        else:
            self.endings = FirstDeclensionNounEndingsO()
        if self.animate:
            self.endings['Accusative']['Singular'] = \
                    self.endings['Genitive']['Singular']


class SecondDeclensionNoun(SloveneNounDeclension):
    def set_gender(self):
        self.gender = 'Feminine'

    def set_endings(self):
        self.endings = SecondDeclensionNounEndings()


class ThirdDeclensionNoun(SloveneNounDeclension):
    pass


class FourthDeclensionNoun(SloveneNounDeclension):
    pass


# vim: et sw=4 sts=4
