#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unicodedata

vowels = [u'α', u'ε', u'η', u'ι', u'ο', u'υ', u'ω']
diphthongs = [u'αι', u'αυ', u'ει', u'ευ', u'ηυ', u'οι', u'ου', u'ωυ']
short_vowels = [u'α', u'ε', u'ι', u'ο', u'υ', u'αι', u'οι']
acute_accent = u'\u0301'
circumflex = u'\u0302'


# Methods intended to be public
###############################

def add_recessive_accent(word, long_ending_vowel=False):
    """long_ending_vowel is for ambigious cases, like α, ι, υ, αι, and οι.
    As we are adding accents here, we assume that there are no diacritics in
    the word already.
    """
    syllables = split_syllables(word)
    last_vowel = get_vowel(syllables[-1])
    if len(syllables) >= 3:
        if last_vowel in short_vowels and not long_ending_vowel:
            syllables[-3] += acute_accent
        else:
            syllables[-2] += acute_accent
    elif len(syllables) == 2:
        if last_vowel in short_vowels and not long_ending_vowel:
            syllables[0] += circumflex
        else:
            syllables[0] += acute_accent
    else:
        # Verbs that have only one syllable should probably be special-cased.
        pass
    word = u''.join(syllables)
    word = unicodedata.normalize('NFKD', word)
    return word


def remove_accents(word):
    # TODO: This should only remove accents, not the diaeresis
    normalized = unicodedata.normalize('NFKD', unicode(word))
    return u''.join([c for c in normalized if not unicodedata.combining(c)])


# Methods that are intended to be private
#########################################
# These methods might be useful in other places, so I'm not munging them with
# a preceding _, but generally they are just helper methods for the public
# methods above

def split_syllables(word):
    """Diacritics cannot have been removed for this method, because they affect
    the number of syllables in a diphthong, among other things.

    I don't deal properly with the diaeresis yet, and I suppose that's the
    only diacritic that really affects this, actually...
    """
    word = unicodedata.normalize('NFKD', word)
    syllables = [u'']
    for i, c in enumerate(word):
        last_char = last_non_combining_character(syllables[-1])
        if unicodedata.combining(c):
            syllables[-1] = syllables[-1] + c
            continue
        if c not in vowels:
            if i != 0 and last_char in vowels:
                syllables.append(u'')
            syllables[-1] = syllables[-1] + c
            continue
        #print 'last char:', last_char
        #print 'last two chars:', last_char + c
        if last_char not in vowels:
            syllables[-1] = syllables[-1] + c
            continue
        if last_char + c in diphthongs:
            syllables[-1] = syllables[-1] + c
        else:
            syllables.append(c)
    if last_non_combining_character(syllables[-1]) not in vowels:
        last = syllables.pop()
        syllables[-1] = syllables[-1] + last
    return syllables


def past_augment(word):
    """Woefully inadequate right now, but it's a start"""
    return u'ἐ' + word


def last_non_combining_character(word):
    if not word:
        return u''
    return remove_accents(word)[-1]


def get_vowel(syllable):
    """This assumes that syllable is output from split_syllables, so all vowels
    are contiguous, and consonants only appear at the beginning and at the end
    of the syllable.  Thus all we need to do is strip consonants and combining
    characters.
    """
    syllable = remove_accents(syllable)
    return u''.join([c for c in syllable if c in vowels])


# For testing things
####################

def main():
    words = [u'παιδεύω', u'παιδεύομαι', u'βιβλίου', u'δώρου', u'θεός', u'οἰκία']
    for word in words:
        print word, remove_accents(word),
        syllables = split_syllables(word)
        print '-'.join(syllables),
        print add_recessive_accent(remove_accents(word))


if __name__ == '__main__':
    main()

# vim: et sw=4 sts=4
