#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unicodedata

from language_study.drills.models import DeclinableWord
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
            elif remove_all_combining(article) == u'η':
                self.gender = 'Feminine'
            elif remove_all_combining(article) == u'το':
                self.gender = 'Neuter'
            else:
                self.gender = 'None'
        else:
            raise ValueError("I don't know how to handle the dictionary entry "
                    "you gave me")
        self.cache_database_stuff()
        self.set_endings()

    def cache_database_stuff(self):
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

    def set_endings(self):
        raise ValueError("I don't know what set of endings to use for this "
                    "word")

    def decline(self, **kwargs):
        case, number = self.check_kwargs(kwargs)
        if (self.gender, number, case) in self.irregular_forms:
            return self.irregular_forms[(self.gender, number, case)]
        self.accented_ending = False
        if case == 'Nominative' and number == 'Singular':
            return unicodedata.normalize('NFKD', self.nominative)
        if case == 'Genitive' and number == 'Singular':
            return unicodedata.normalize('NFKD', self.genitive)
        stem = self.get_stem()
        ending = self.endings[case][number]
        unchecked = self.combine_parts(stem, ending, case, number)
        final_form = self.check_accent(unchecked, case, number)
        return unicodedata.normalize('NFKD', final_form)

    def check_kwargs(self, kwargs):
        if 'case' not in kwargs:
            raise ValueError("Case must be specified")
        case = kwargs['case']
        if 'number' not in kwargs:
            raise ValueError("Number must be specified")
        number = kwargs['number']
        # TODO: figure out if I should check gender here, and what to do
        return case, number

    def get_stem(self):
        # I think only the third declension really need to go from the genitive
        # singular.  Because of that, we get the right persistent accent easier
        # if we go from the nominative here.  The third declension will
        # override this.
        ending = self.endings['Nominative']['Singular']
        nominative_ending = self.nominative[-len(ending):]
        if is_accented(nominative_ending):
            self.accented_ending = True
        return self.nominative[:-len(ending)]

    def combine_parts(self, stem, ending, case, number):
        combined = stem + ending
        if self.accented_ending:
            if case in ['Genitive', 'Dative']:
                combined = add_final_circumflex(combined)
            else:
                combined = add_final_acute(combined)
        return combined

    def check_accent(self, form, case, number):
        form = fix_persistent_accent(form, self.endings.is_long(case, number))
        return form


class FirstDeclensionNoun(GreekDeclension):
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
        else:
            raise ValueError("I don't know what set of endings to use for this "
                    "word")

    def combine_parts(self, stem, ending, case, number):
        if number == 'Plural' and case == 'Genitive':
            return add_final_circumflex(remove_accents(stem + ending))
        else:
            return super(FirstDeclensionNoun, self).combine_parts(stem, ending,
                    case, number)


class SecondDeclensionNoun(GreekDeclension):
    def set_endings(self):
        if remove_accents(self.nominative).endswith(u'ος'):
            self.endings = SecondDeclensionMF()
        elif remove_accents(self.nominative).endswith(u'ον'):
            self.endings = SecondDeclensionNeuter()
        else:
            raise ValueError("I don't know what set of endings to use for this "
                    "word")


# vim: et sw=4 sts=4
