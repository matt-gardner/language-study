#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unicodedata

from language_study.drills.models import DeclinableWord
from language_study.drills.models import LongPenult
from noun_endings import *
from util.accents import *
from util.base import *

verbose = False

# TODO: this belongs somewhere else
class Declension(object):
    def __init__(self):
        pass

    def decline(self, **kwargs):
        raise NotImplementedError()


class GreekDeclension(Declension):
    def __init__(self, dictionary_entry, word_id=-1):
        self.dictionary_entry = dictionary_entry
        self.word_id = word_id
        self.gender = None
        self.process_dictionary_entry(dictionary_entry)
        self.cache_database_stuff()
        self.set_endings()

    def process_dictionary_entry(dictionary_entry):
        raise NotImplementedError()

    def cache_database_stuff(self):
        self.irregular_forms = dict()
        self.long_penult = False
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
            word.longpenult
            self.long_penult = True
        except LongPenult.DoesNotExist:
            pass

    def set_endings(self):
        raise NotImplementedError()

    def decline(self, **kwargs):
        gender, number, case = self.check_kwargs(kwargs)
        if (gender, number, case) in self.irregular_forms:
            return self.irregular_forms[(gender, number, case)]
        self.accented_ending = False
        stem = self.get_stem(gender)
        ending = self.get_ending(gender, number, case)
        unchecked = self.combine_parts(stem, ending, number, case)
        final_form = self.check_accent(unchecked, gender, number, case)
        return unicodedata.normalize('NFKD', final_form)

    def check_kwargs(self, kwargs):
        if 'case' not in kwargs:
            raise ValueError("Case must be specified")
        case = kwargs['case']
        if 'number' not in kwargs:
            raise ValueError("Number must be specified")
        number = kwargs['number']
        if self.gender:
            gender = self.gender
        else:
            if 'gender' not in kwargs:
                raise ValueError("Gender must be specified")
            gender = kwargs['gender']
        return gender, number, case

    def get_stem(self, gender):
        raise NotImplementedError()

    def get_ending(self, gender, number, case):
        raise NotImplementedError()

    def is_long_ending(self, gender, number, case):
        raise NotImplementedError()

    def combine_parts(self, stem, ending, number, case):
        combined = stem + ending
        if self.accented_ending:
            if case in ['Genitive', 'Dative']:
                combined = add_final_circumflex(combined)
            else:
                combined = add_final_acute(combined)
        return combined

    def check_accent(self, form, gender, number, case):
        form = fix_persistent_accent(form, self.long_penult,
                self.is_long_ending(gender, number, case))
        return form


class GreekAdjectiveDeclension(GreekDeclension):
    def process_dictionary_entry(self, dictionary_entry):
        entry_parts = dictionary_entry.split(', ')
        if len(entry_parts) == 2:
            self.masculine, self.neuter = entry_parts
            self.feminine = self.masculine
        elif len(entry_parts) == 3:
            self.masculine, self.feminine, self.neuter = entry_parts
        else:
            raise ValueError("I don't know how to handle the dictionary entry "
                    "you gave me")
        self.nominative = {}
        self.nominative['Masculine'] = self.masculine
        self.nominative['Feminine'] = self.feminine
        self.nominative['Neuter'] = self.neuter

    def set_endings(self):
        self.endings = {}
        self.endings['Masculine'] = SecondDeclensionMF()
        if self.masculine == self.feminine:
            self.endings['Feminine'] = SecondDeclensionMF()
        elif remove_accents(self.feminine).endswith(u'η'):
            self.endings['Feminine'] = FirstDeclensionFeminineEta()
        elif remove_accents(self.feminine).endswith(u'α'):
            self.endings['Feminine'] = FirstDeclensionFeminineAlpha()
        self.endings['Neuter'] = SecondDeclensionNeuter()

    def get_stem(self, gender):
        ending = self.endings['Neuter']['Nominative']['Singular']
        nominative_ending = self.nominative['Neuter'][-len(ending):]
        if is_accented(nominative_ending):
            self.accented_ending = True
        return self.nominative['Neuter'][:-len(ending)]

    def get_ending(self, gender, number, case):
        return self.endings[gender][case][number]

    def is_long_ending(self, gender, number, case):
        return self.endings[gender].is_long(number, case)


class GreekNounDeclension(GreekDeclension):
    def process_dictionary_entry(self, dictionary_entry):
        entry_parts = dictionary_entry.split(', ')
        if len(entry_parts) == 3:
            self.nominative, self.genitive, article = entry_parts
            if remove_all_combining(article) == u'ο':
                self.gender = 'Masculine'
            elif remove_all_combining(article) == u'η':
                self.gender = 'Feminine'
            elif remove_all_combining(article) == u'το':
                self.gender = 'Neuter'
            else:
                raise ValueError("Unexpected format of dictionary entry...")
        else:
            raise ValueError("I don't know how to handle the dictionary entry "
                    "you gave me")

    def set_endings(self):
        raise NotImplementedError()

    def get_stem(self, gender):
        # I think only the third declension really need to go from the genitive
        # singular.  Because of that, we get the right persistent accent easier
        # if we go from the nominative here.  The third declension will
        # override this.
        ending = self.endings['Nominative']['Singular']
        nominative_ending = self.nominative[-len(ending):]
        if is_accented(nominative_ending):
            self.accented_ending = True
        return self.nominative[:-len(ending)]

    def get_ending(self, gender, number, case):
        return self.endings[case][number]

    def is_long_ending(self, gender, number, case):
        return self.endings.is_long(number, case)


class FirstDeclensionNoun(GreekNounDeclension):
    def set_endings(self):
        if remove_accents(self.genitive).endswith(u'ης'):
            self.endings = FirstDeclensionFeminineEta()
            if remove_accents(self.nominative).endswith(u'α'):
                self.endings.is_long = self.endings.short_alpha_is_long
                self.endings['Nominative']['Singular'] = u'α'
                self.endings['Accusative']['Singular'] = u'αν'
                self.endings['Vocative']['Singular'] = u'α'
        elif remove_accents(self.genitive).endswith(u'ας'):
            self.endings = FirstDeclensionFeminineAlpha()
            is_short_alpha = False
            syllables = split_syllables(self.nominative)
            syllables.reverse()
            if len(syllables) > 2 and is_accented(syllables[2]):
                is_short_alpha = True
            if (len(syllables) > 1 and is_accented(syllables[1]) and
                    get_accent(syllables[1]) == circumflex):
                is_short_alpha = True
            if is_short_alpha:
                self.endings.is_long = self.endings.short_alpha_is_long
        elif remove_accents(self.nominative).endswith(u'ας'):
            # I didn't think I had to actually worry about putting the
            # irregular forms in here, because we get the nominative and
            # genitive singular for free anyway, and those are the forms that
            # are different.  But it turns out that we do need to set what the
            # ending is, because we need to strip it off to do the rest of the
            # forms right.
            self.endings = FirstDeclensionFeminineAlpha()
            self.endings['Nominative']['Singular'] = u'ας'
            self.endings['Genitive']['Singular'] = u'ου'
        elif remove_accents(self.nominative).endswith(u'ης'):
            self.endings = FirstDeclensionFeminineEta()
            self.endings.is_long = self.endings.masculine_is_long
            self.endings['Nominative']['Singular'] = u'ης'
            self.endings['Genitive']['Singular'] = u'ου'
            self.endings['Vocative']['Singular'] = u'α'
        else:
            raise ValueError("I don't know what set of endings to use for this "
                    "word")

    def combine_parts(self, stem, ending, number, case):
        if number == 'Plural' and case == 'Genitive':
            return add_final_circumflex(remove_accents(stem + ending))
        else:
            return super(FirstDeclensionNoun, self).combine_parts(stem, ending,
                    number, case)


class SecondDeclensionNoun(GreekNounDeclension):
    def set_endings(self):
        if remove_accents(self.nominative).endswith(u'ος'):
            self.endings = SecondDeclensionMF()
        elif remove_accents(self.nominative).endswith(u'ον'):
            self.endings = SecondDeclensionNeuter()
        else:
            raise ValueError("I don't know what set of endings to use for this "
                    "word")


# vim: et sw=4 sts=4
