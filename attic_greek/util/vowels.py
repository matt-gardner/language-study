#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unicodedata

from base import diphthongs
from base import vowels

short_vowels = [u'α', u'ε', u'ι', u'ο', u'υ', u'αι', u'οι']
ambiguous = [u'α', u'ι', u'υ']
long_optative = [u'οι', u'αι']
long_except_at_end = [u'οι', u'αι']


def starts_with_vowel(word):
    if len(word) == 0:
        return False
    normalized = unicodedata.normalize('NFKD', word)
    word = u''.join([c for c in normalized if not unicodedata.combining(c)])
    return word[0] in vowels


def remove_initial_vowel(word):
    if not word:
        return u''
    word = unicodedata.normalize('NFKD', word)
    removed = u''
    while word[0] in vowels or unicodedata.combining(word[0]):
        removed += word[0]
        test = u''.join([c for c in removed if not unicodedata.combining(c)])
        if test and test not in vowels and test not in diphthongs:
            return word
        if len(word) == 1:
            return u''
        word = word[1:]
    return word


def get_last_vowel(word):
    """This does not assume that the word has been split into syllables.  Just
    look at the last vowel and tell me if it's long.
    """
    from accents import remove_all_combining
    if not word:
        return u''
    word = remove_all_combining(word)
    while word[-1] not in vowels:
        if len(word) == 1:
            return u''
        word = word[:-1]
    vowel = u''
    while len(word) > 0 and word[-1] in vowels:
        temp_vowel = word[-1] + vowel
        if temp_vowel not in vowels and temp_vowel not in diphthongs:
            return vowel
        vowel = temp_vowel
        word = word[:-1]
    return vowel


def get_vowel(syllable):
    """This assumes that syllable is output from split_syllables, so all vowels
    are contiguous, and consonants only appear at the beginning and at the end
    of the syllable.  Thus all we need to do is strip consonants and combining
    characters.
    """
    from accents import remove_accents
    syllable = remove_accents(syllable)
    return u''.join([c for c in syllable if c in vowels])


def is_short(vowel, optative=False, long_ending_vowel=False):
    if vowel not in short_vowels:
        return False
    if should_be_long(vowel, optative, long_ending_vowel):
        return False
    return True


def should_be_long(vowel, optative, long_ending_vowel):
    """This assumes that vowel is in short_vowels, and that it is the last
    vowel in a word.  There are only a few simple checks, but it seemed better
    to separate it into its own method."""
    if long_ending_vowel:
        return True
    if optative and vowel in long_optative:
        return True
    return False


def can_have_circumflex(vowel):
    # TODO: This is wrong in some cases
    return vowel not in short_vowels


def lengthen_vowel(vowel):
    if vowel == u'ει':
        return u'ῃ'
    elif vowel == u'ε':
        return u'η'
    elif vowel == u'η':
        return u'η'
    elif vowel == u'α':
        return u'η'
    elif vowel == u'αι':
        return u'ῃ'
    elif vowel == u'ι':
        return u'ι'
    raise RuntimeError(u"I don't know how to lengthen these vowels: %s" % vowel)


def shorten_vowel(vowel, principle_parts):
    if vowel == u'ε':
        # This is a bit of a hack, because we shouldn't ever have to shorten ε
        # Oh well
        return u'ε'
    if vowel == u'ει':
        return u'ε'
    elif vowel == u'η':
        # TODO: look at pp's to figure out what to do with this
        return u'ε'
    elif vowel == u'α':
        return u'α'
    elif vowel == u'ι':
        return u'ι'
    elif vowel == u'ω':
        return u'ο'


def contract_vowels(vowels, spurious_diphthong=False, athematic=False):
    if vowels == u'αε':
        return u'α'
    elif vowels == u'αει':
        if spurious_diphthong:
            return u'α'
        else:
            return u'ᾳ'
    elif vowels == u'αη':
        return u'α'
    elif vowels == unicodedata.normalize('NFKD', u'αῃ'):
        return u'ᾳ'
    elif vowels == u'αο':
        return u'ω'
    elif vowels == u'αοι':
        return u'ῳ'
    elif vowels == u'αου':
        return u'ω'
    elif vowels == u'αω':
        return u'ω'
    elif vowels == u'εε':
        return u'ει'
    elif vowels == u'εει':
        return u'ει'
    elif vowels == u'εη':
        return u'η'
    elif vowels == unicodedata.normalize('NFKD', u'εῃ'):
        return u'ῃ'
    elif vowels == u'εο':
        return u'ου'
    elif vowels == u'εοι':
        return u'οι'
    elif vowels == u'εου':
        return u'ου'
    elif vowels == u'εω':
        return u'ω'
    elif vowels == u'οε':
        return u'ου'
    elif vowels == u'οει':
        if spurious_diphthong:
            return u'ου'
        else:
            return u'οι'
    elif vowels == u'οη':
        return u'ω'
    elif vowels == unicodedata.normalize('NFKD', u'οῃ'):
        if athematic:
            return u'ῳ'
        else:
            return u'οι'
    elif vowels == u'οο':
        return u'ου'
    elif vowels == u'οοι':
        return u'οι'
    elif vowels == u'οου':
        return u'ου'
    elif vowels == u'οω':
        return u'ω'
    elif vowels == u'ηε':
        return u'η'
    elif vowels == u'ωε':
        return u'ω'
    print 'Bad vowels:', vowels
    raise ValueError("I don't know how to handle these vowels")


# vim: et sw=4 sts=4
