#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""Contains ending sets for all declinable types (not just nouns)."""

##############
# Base Classes
##############

class DeclensionEndingSet(dict):
    def __init__(self):
        self['Nominative'] = {'Singular': u'', 'Dual': u'', 'Plural': u''}
        self['Genitive'] = {'Singular': u'', 'Dual': u'', 'Plural': u''}
        self['Dative'] = {'Singular': u'', 'Dual': u'', 'Plural': u''}
        self['Accusative'] = {'Singular': u'', 'Dual': u'', 'Plural': u''}
        self['Locative'] = {'Singular': u'', 'Dual': u'', 'Plural': u''}
        self['Instrumental'] = {'Singular': u'', 'Dual': u'', 'Plural': u''}

##########################
# First Declension Endings
##########################

class FirstDeclensionNounEndingsO(DeclensionEndingSet):
    def __init__(self):
        super(FirstDeclensionNounEndingsO, self).__init__()
        self['Nominative']['Singular'] = u''
        self['Genitive']['Singular'] = u'a'
        self['Dative']['Singular'] = u'u'
        self['Accusative']['Singular'] = u'a'
        self['Locative']['Singular'] = u'u'
        self['Instrumental']['Singular'] = u'om'
        self['Nominative']['Dual'] = u'a'
        self['Genitive']['Dual'] = u'ov'
        self['Dative']['Dual'] = u'oma'
        self['Accusative']['Dual'] = u'a'
        self['Locative']['Dual'] = u'ih'
        self['Instrumental']['Dual'] = u'oma'
        self['Nominative']['Plural'] = u'i'
        self['Genitive']['Plural'] = u'ov'
        self['Dative']['Plural'] = u'om'
        self['Accusative']['Plural'] = u'e'
        self['Locative']['Plural'] = u'ih'
        self['Instrumental']['Plural'] = u'i'


class FirstDeclensionNounEndingsE(DeclensionEndingSet):
    def __init__(self):
        super(FirstDeclensionNounEndingsE, self).__init__()
        self['Nominative']['Singular'] = u''
        self['Genitive']['Singular'] = u'a'
        self['Dative']['Singular'] = u'u'
        self['Accusative']['Singular'] = u''
        self['Locative']['Singular'] = u'u'
        self['Instrumental']['Singular'] = u'em'
        self['Nominative']['Dual'] = u'a'
        self['Genitive']['Dual'] = u'ev'
        self['Dative']['Dual'] = u'ema'
        self['Accusative']['Dual'] = u'a'
        self['Locative']['Dual'] = u'ih'
        self['Instrumental']['Dual'] = u'ema'
        self['Nominative']['Plural'] = u'i'
        self['Genitive']['Plural'] = u'ev'
        self['Dative']['Plural'] = u'em'
        self['Accusative']['Plural'] = u'e'
        self['Locative']['Plural'] = u'ih'
        self['Instrumental']['Plural'] = u'i'


class SecondDeclensionNounEndings(DeclensionEndingSet):
    def __init__(self):
        super(SecondDeclensionNounEndings, self).__init__()
        self['Nominative']['Singular'] = u'a'
        self['Genitive']['Singular'] = u'e'
        self['Dative']['Singular'] = u'i'
        self['Accusative']['Singular'] = u'o'
        self['Locative']['Singular'] = u'i'
        self['Instrumental']['Singular'] = u'o'
        self['Nominative']['Dual'] = u'i'
        self['Genitive']['Dual'] = u''
        self['Dative']['Dual'] = u'ama'
        self['Accusative']['Dual'] = u'i'
        self['Locative']['Dual'] = u'ah'
        self['Instrumental']['Dual'] = u'ama'
        self['Nominative']['Plural'] = u'e'
        self['Genitive']['Plural'] = u''
        self['Dative']['Plural'] = u'am'
        self['Accusative']['Plural'] = u'e'
        self['Locative']['Plural'] = u'ah'
        self['Instrumental']['Plural'] = u'ami'


# vim: et sw=4 sts=4
