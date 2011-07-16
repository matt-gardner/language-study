#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""Contains ending sets for all declinable types (not just nouns)."""

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

    def is_long(self, case, number):
        raise NotImplementedError("If you really want to have a default, use "
                "self.default_is_long(case, number)")

    def default_is_long(self, case, number):
        if not is_short(get_vowel(self[case][number])):
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

    def is_long(self, case, number):
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


# vim: et sw=4 sts=4
