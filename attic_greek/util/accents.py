#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unicodedata

from base import split_syllables

acute_accent = u'\u0301'
grave_accent = u'\u0300'
circumflex = u'\u0342'
smooth_breathing = u'\u0313'
rough_breathing = u'\u0314'
accents = set([acute_accent, grave_accent, circumflex])
breathings = set([smooth_breathing, rough_breathing])
acc_plus_breath = accents.union(breathings)


def remove_accents(word, breathing=False):
    # This removes accents and breathing marks while leaving the diaeresis and
    # subscript iota
    normalized = unicodedata.normalize('NFKD', unicode(word))
    return u''.join([c for c in normalized if not is_accent(c, breathing)])


def remove_all_combining(word):
    normalized = unicodedata.normalize('NFKD', unicode(word))
    return u''.join([c for c in normalized if not unicodedata.combining(c)])


def add_recessive_accent(word, optative=False, long_ending_vowel=False):
    """long_ending_vowel is for ambigious cases, like α, ι, υ, αι, and οι.
    optative is so that the conjugation code doesn't have to check to see if
    the person and number asked for ends in οι.
    As we are adding accents here, we assume that there are no accents in
    the word already.
    """
    from vowels import can_have_circumflex
    from vowels import get_vowel
    from vowels import is_short
    syllables = split_syllables(word)
    last_vowel = get_vowel(syllables[-1])
    if len(syllables) >= 3:
        if is_short(last_vowel, optative, long_ending_vowel):
            syllables[-3] += acute_accent
        else:
            syllables[-2] += acute_accent
    elif len(syllables) == 2:
        if (is_short(last_vowel, optative, long_ending_vowel) and
                can_have_circumflex(get_vowel(syllables[0]))):
            syllables[0] += circumflex
        else:
            syllables[0] += acute_accent
    else:
        # This probably will break some day, but it will do for now
        vowel = get_vowel(syllables[0])
        pos = syllables[0].find(vowel) + len(vowel)
        if unicodedata.combining(syllables[0][pos]):
            pos += 1
        if can_have_circumflex(vowel):
            accent = circumflex
        else:
            accent = acute_accent
        syllables[0] = syllables[0][:pos] + accent + syllables[0][pos:]
    word = u''.join(syllables)
    word = unicodedata.normalize('NFKD', word)
    return word


def add_persistent_accent(original, inflected):
    raise NotImplementedError()


def add_athematic_optative_accent(form):
    from vowels import get_vowel
    syllables = split_syllables(form)
    index = -1
    while get_vowel(syllables[index]) not in [u'οι', u'ει', u'αι']:
        index -= 1
    if abs(index) == 3:
        accent = acute_accent
    elif get_vowel(syllables[-1]) == u'η':
        accent = acute_accent
    else:
        accent = circumflex
    syllables.insert(index+1, accent)
    return unicodedata.normalize('NFKD', u''.join(syllables))


def add_penult_accent(word, long_ending_vowel=False, long_penult=False):
    from vowels import get_vowel
    from vowels import short_vowels
    syllables = split_syllables(word)
    last_vowel = get_vowel(syllables[-1])
    penult_vowel = get_vowel(syllables[-2])
    if last_vowel in short_vowels and penult_vowel not in short_vowels:
        # This check is inadequate, though how to fix it is tricky, unless I
        # require macrons to be on long vowels, and I don't really want to do
        # that...
        syllables[-2] += circumflex
    else:
        syllables[-2] += acute_accent
    return unicodedata.normalize('NFKD', u''.join(syllables))


def add_final_circumflex(word):
    from vowels import get_vowel
    syllables = split_syllables(word)
    last_vowel = get_vowel(syllables[-1])
    index = word.find(last_vowel) + len(last_vowel)
    word = word[:index] + circumflex + word[index:]
    return unicodedata.normalize('NFKD', word)


def is_accented(word):
    for c in word:
        if is_accent(c):
            return True
    return False


def is_accent(character, breathing=False):
    """This also includes breathing marks, but ignores subscript iotas and the
    dieresis"""
    if breathing:
        if character in acc_plus_breath:
            return True
    else:
        if character in accents:
            return True
    return False


def get_breathing(word):
    if smooth_breathing in word:
        return smooth_breathing
    if rough_breathing in word:
        return rough_breathing
    return None


# vim: et sw=4 sts=4
