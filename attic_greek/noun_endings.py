#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""Contains ending sets for all declinable types (not just nouns)."""

from util.base import split_syllables
from util.vowels import get_vowel
from util.vowels import is_short

##############
# Base Classes
##############

class DeclensionEndingSet(dict):
    def __init__(self):
        self['Nominative'] = {'Singular': u'', 'Plural': u''}
        self['Genitive'] = {'Singular': u'', 'Plural': u''}
        self['Dative'] = {'Singular': u'', 'Plural': u''}
        self['Accusative'] = {'Singular': u'', 'Plural': u''}
        self['Vocative'] = {'Singular': u'', 'Plural': u''}

    def is_long(self, number, case):
        raise NotImplementedError("If you really want to have a default, use "
                "self.default_is_long(number, case)")

    def default_is_long(self, number, case):
        syllables = split_syllables(self[case][number])
        if not is_short(get_vowel(syllables[-1])):
            return True
        else:
            return False


##########################
# First Declension Endings
##########################

class FirstDeclensionFeminineEta(DeclensionEndingSet):
    def __init__(self):
        super(FirstDeclensionFeminineEta, self).__init__()
        self['Nominative']['Singular'] = u'η'
        self['Genitive']['Singular'] = u'ης'
        self['Dative']['Singular'] = u'ῃ'
        self['Accusative']['Singular'] = u'ην'
        self['Vocative']['Singular'] = u'η'
        self['Nominative']['Plural'] = u'αι'
        self['Genitive']['Plural'] = u'ων'
        self['Dative']['Plural'] = u'αις'
        self['Accusative']['Plural'] = u'ας'
        self['Vocative']['Plural'] = u'αι'

    def is_long(self, number, case):
        if number == 'Plural':
            if case in ['Nominative', 'Vocative']:
                return False
        return True

    def short_alpha_is_long(self, number, case):
        if number == 'Singular':
            if case in ['Nominative', 'Accusative', 'Vocative']:
                return False
        if number == 'Plural':
            if case in ['Nominative', 'Vocative']:
                return False
        return True

    def masculine_is_long(self, number, case):
        if number == 'Singular':
            if case in ['Vocative']:
                return False
        if number == 'Plural':
            if case in ['Nominative', 'Vocative']:
                return False
        return True


class FirstDeclensionFeminineAlpha(FirstDeclensionFeminineEta):
    def __init__(self):
        super(FirstDeclensionFeminineAlpha, self).__init__()
        self['Nominative']['Singular'] = u'α'
        self['Genitive']['Singular'] = u'ας'
        self['Dative']['Singular'] = u'ᾳ'
        self['Accusative']['Singular'] = u'αν'
        self['Vocative']['Singular'] = u'α'


###########################
# Second Declension Endings
###########################

class SecondDeclensionMF(DeclensionEndingSet):
    def __init__(self):
        super(SecondDeclensionMF, self).__init__()
        self['Nominative']['Singular'] = u'ος'
        self['Genitive']['Singular'] = u'ου'
        self['Dative']['Singular'] = u'ῳ'
        self['Accusative']['Singular'] = u'ον'
        self['Vocative']['Singular'] = u'ε'
        self['Nominative']['Plural'] = u'οι'
        self['Genitive']['Plural'] = u'ων'
        self['Dative']['Plural'] = u'οις'
        self['Accusative']['Plural'] = u'ους'
        self['Vocative']['Plural'] = u'οι'

    def is_long(self, number, case):
        return self.default_is_long(number, case)


class SecondDeclensionNeuter(SecondDeclensionMF):
    def __init__(self):
        super(SecondDeclensionNeuter, self).__init__()
        self['Nominative']['Singular'] = u'ον'
        self['Vocative']['Singular'] = u'ον'
        self['Nominative']['Plural'] = u'α'
        self['Accusative']['Plural'] = u'α'
        self['Vocative']['Plural'] = u'α'


##########################
# Third Declension Endings
##########################

class ThirdDeclensionMF(DeclensionEndingSet):
    def __init__(self):
        super(ThirdDeclensionMF, self).__init__()
        self['Nominative']['Singular'] = u''
        self['Genitive']['Singular'] = u'ος'
        self['Dative']['Singular'] = u'ι'
        self['Accusative']['Singular'] = u'α'
        self['Vocative']['Singular'] = u''
        self['Nominative']['Plural'] = u'ες'
        self['Genitive']['Plural'] = u'ων'
        self['Dative']['Plural'] = u'σι'
        self['Accusative']['Plural'] = u'ας'
        self['Vocative']['Plural'] = u'ες'

    def is_long(self, number, case):
        if number == 'Singular' and case in ['Nominative', 'Vocative']:
            return False
        return self.default_is_long(number, case)


class ThirdDeclensionNeuter(ThirdDeclensionMF):
    def __init__(self):
        super(ThirdDeclensionNeuter, self).__init__()
        self['Accusative']['Singular'] = u''
        self['Nominative']['Plural'] = u'α'
        self['Accusative']['Plural'] = u'α'
        self['Vocative']['Plural'] = u'α'


class PolisEndings(DeclensionEndingSet):
    def __init__(self):
        super(PolisEndings, self).__init__()
        self['Nominative']['Singular'] = u'ις'
        self['Genitive']['Singular'] = u'εως'
        self['Dative']['Singular'] = u'ει'
        self['Accusative']['Singular'] = u'ιν'
        self['Vocative']['Singular'] = u'ι'
        self['Nominative']['Plural'] = u'εις'
        self['Genitive']['Plural'] = u'εων'
        self['Dative']['Plural'] = u'εσι'
        self['Accusative']['Plural'] = u'εις'
        self['Vocative']['Plural'] = u'εις'

    def is_long(self, number, case):
        return self.default_is_long(number, case)


class BasileusEndings(DeclensionEndingSet):
    def __init__(self):
        super(BasileusEndings, self).__init__()
        self['Nominative']['Singular'] = u'εύς'
        self['Genitive']['Singular'] = u'έως'
        self['Dative']['Singular'] = u'εῖ'
        self['Accusative']['Singular'] = u'έα'
        self['Vocative']['Singular'] = u'εῦ'
        self['Nominative']['Plural'] = u'εῖς'
        self['Genitive']['Plural'] = u'έων'
        self['Dative']['Plural'] = u'εῦσι'
        self['Accusative']['Plural'] = u'έας'
        self['Vocative']['Plural'] = u'εῖς'

    def is_long(self, number, case):
        raise ValueError("this shouldn't need to be called")


class GenosEndings(DeclensionEndingSet):
    def __init__(self):
        super(GenosEndings, self).__init__()
        self['Nominative']['Singular'] = u'ος'
        self['Genitive']['Singular'] = u'ους'
        self['Dative']['Singular'] = u'ει'
        self['Accusative']['Singular'] = u'ος'
        self['Vocative']['Singular'] = u'ος'
        self['Nominative']['Plural'] = u'η'
        self['Genitive']['Plural'] = u'ων'
        self['Dative']['Plural'] = u'εσι'
        self['Accusative']['Plural'] = u'η'
        self['Vocative']['Plural'] = u'η'

    def is_long(self, number, case):
        return self.default_is_long(number, case)


# vim: et sw=4 sts=4
