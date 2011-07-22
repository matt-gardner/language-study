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
        stem = self.get_stem(gender, number, case)
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

    def get_stem(self, gender, number, case):
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

    def get_stem(self, gender, number, case):
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

    def get_stem(self, gender, number, case):
        # I think only the third declension really needs to go from the
        # genitive singular.  Because of that, we get the right persistent
        # accent easier if we go from the nominative here.  The third
        # declension will override this.
        ending = self.endings['Nominative']['Singular']
        # I think this only works because self.nominative is not normalized.
        # Otherwise we would have to be a little more tricky in case the ending
        # was accented.  As it is, we can just check the same number of
        # characters and get the accent with it.  So it works.
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


class ThirdDeclensionNoun(GreekNounDeclension):
    def __init__(self, dictionary_entry, word_id=-1):
        self.special = None
        super(ThirdDeclensionNoun, self).__init__(dictionary_entry, word_id)

    def set_endings(self):
        if self.nominative[-2:] == u'ις' and self.genitive[-3:] == u'εως':
            self.endings = PolisEndings()
            self.special = 'polis'
        elif (self.nominative.endswith(u'εύς') and
                self.genitive.endswith(u'έως')):
            self.endings = BasileusEndings()
            self.special = 'basileus'
        elif self.nominative[-2:] == u'ος' and self.genitive[-3:] == u'ους':
            self.endings = GenosEndings()
            self.special = 'genos'
        elif self.gender in ['Masculine', 'Feminine']:
            self.endings = ThirdDeclensionMF()
        elif self.gender == 'Neuter':
            self.endings = ThirdDeclensionNeuter()
        else:
            raise ValueError("I don't know what set of endings to use for this "
                    "word")
        if self.genitive.endswith(u'τρός'):
            self.special = 'meter'
        elif self.genitive.endswith(u'δρός'):
            self.special = 'aner'

    def decline(self, **kwargs):
        gender, number, case = self.check_kwargs(kwargs)
        if (gender == 'Neuter' and number == 'Singular' and
                case in ['Nominative', 'Accusative', 'Vocative']):
            return unicodedata.normalize('NFKD', self.nominative)
        if number == 'Singular' and case == 'Nominative':
            return unicodedata.normalize('NFKD', self.nominative)
        if number == 'Singular' and case == 'Vocative' and not self.special:
            if self.nominative[-1] in [u'ξ', u'ψ']:
                return unicodedata.normalize('NFKD', self.nominative)
            elif self.nominative[-1] in [u'ν', u'ρ']:
                syllables = split_syllables(self.nominative)
                if is_accented(syllables[-1]):
                    return unicodedata.normalize('NFKD', self.nominative)
        # We do this check again on purpose, to easily catch any vocatives that
        # weren't caught in the special cases above.
        if number == 'Singular' and case == 'Vocative' and not self.special:
            stem = self.get_stem(gender, number, case)
            if stem[-1] in dentals:
                stem = stem[:-1]
            return unicodedata.normalize('NFKD', stem)
        return super(ThirdDeclensionNoun, self).decline(**kwargs)

    def get_stem(self, gender, number, case):
        ending = self.endings['Genitive']['Singular']
        # I think this only works because self.genitive is not normalized.  See
        # above.
        genitive_ending = self.genitive[-len(ending):]
        if is_accented(genitive_ending):
            self.accented_ending = True
        stem = self.genitive[:-len(ending)]
        if self.special == 'meter':
            if number == 'Singular':
                if case == 'Accusative':
                    stem = stem[:-1] + u'έρ'
                    self.accented_ending = False
                elif case == 'Vocative':
                    stem = stem[:-3] + u'ῆτερ'
                    self.accented_ending = False
            elif number == 'Plural':
                if case in ['Nominative', 'Genitive', 'Vocative', 'Accusative']:
                    stem = stem[:-1] + u'έρ'
                    self.accented_ending = False
                elif case == 'Dative':
                    stem += u'ά'
                    self.accented_ending = False
        elif self.special == 'aner':
            if number == 'Singular' and case == 'Vocative':
                stem = stem[:-2] + u'ερ'
            elif number == 'Plural' and case == 'Dative':
                stem += u'ά'
                self.accented_ending = False
        return stem

    def combine_parts(self, stem, ending, number, case):
        if self.special == 'polis':
            if case == 'Genitive' and number in ['Singular', 'Plural']:
                combined = stem + ending
                accented = add_antepenult_accent(remove_accents(combined))
                return unicodedata.normalize('NFKD', accented)
            else:
                return super(ThirdDeclensionNoun, self).combine_parts(stem,
                        ending, number, case)
        elif self.special == 'basileus':
            return unicodedata.normalize('NFKD', stem + ending)
        if number == 'Plural' and case == 'Dative' and not self.special:
            stem, ending = combine_consonants(stem, ending)
        if number == 'Singular' and case == 'Accusative':
            if stem[-2:] in [u'ιτ', u'ιδ', u'ιθ']:
                stem = stem[:-1]
                ending = u'ν'
        syllables = split_syllables(stem)
        if len(syllables) == 1:
            if case not in ['Genitive', 'Dative']:
                return add_penult_accent(remove_accents(stem) + ending)
        return super(ThirdDeclensionNoun, self).combine_parts(stem, ending,
                number, case)

    def check_accent(self, form, gender, number, case):
        if self.special == 'polis':
            if case == 'Genitive' and number in ['Singular', 'Plural']:
                return form
        elif self.special == 'basileus':
            return form
        elif self.special == 'genos':
            if case == 'Genitive' and number == 'Plural':
                return unicodedata.normalize('NFKD',
                        add_final_circumflex(remove_accents(form)))
        elif self.special == 'aner':
            if number == 'Singular':
                if case in ['Accustaive', 'Vocative']:
                    log_if_verbose({'form': form})
                    return unicodedata.normalize('NFKD',
                            add_penult_accent(remove_accents(form)))
            elif number == 'Plural':
                if case in ['Nominative', 'Accustaive', 'Vocative']:
                    return unicodedata.normalize('NFKD',
                            add_penult_accent(remove_accents(form)))
        return super(ThirdDeclensionNoun, self).check_accent(form, gender,
                number, case)


# vim: et sw=4 sts=4
