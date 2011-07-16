#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unicodedata

# This is because base isn't allowed to import anything from other files in
# util.  I was just trying to keep the dependencies clean.
vowels = [u'α', u'ε', u'η', u'ι', u'ο', u'υ', u'ω']
diphthongs = [u'αι', u'αυ', u'ει', u'ευ', u'ηυ', u'οι', u'ου', u'ωυ']


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
        if last_char not in vowels:
            syllables[-1] = syllables[-1] + c
            continue
        if last_char + c in diphthongs:
            syllables[-1] = syllables[-1] + c
        else:
            syllables.append(c)
    if len(syllables) == 1:
        return syllables
    if last_non_combining_character(syllables[-1]) not in vowels:
        last = syllables.pop()
        syllables[-1] = syllables[-1] + last
    return syllables


def get_matching_index(unaccented, accented, index):
    """Return the corresponding index from unaccented into accented.

    In other words, we know the index we want in unaccented, but we need to get
    the matching index in accented.  This method does that.
    """
    i = 0
    j = 0
    while i <= index:
        while unaccented[i] != accented[j]:
            j += 1
        i += 1
        j += 1
    return j


def last_non_combining_character(word):
    if not word:
        return u''
    final = u''.join([c for c in word if not unicodedata.combining(c)])
    if final:
        return final[-1]
    else:
        return u''


def get_final_consonant(word):
    """This assumes that we are looking at the first principle part.

    The purpose of this method is as an aid to determining how to deal with
    consonant stems in the perfect tenses, so we just care about the first
    principle part.
    """
    # These two lines are pretty much equivalent to remove_accents, but I
    # didn't want to import that here.  Sorry...
    normalized = unicodedata.normalize('NFKD', word)
    word = u''.join([c for c in normalized if not unicodedata.combining(c)])
    if word[-1] == u'ω':
        stem = word[:-1]
    else:
        stem = word[:-4]
    if stem[-1] in vowels:
        return u''
    consonant = u''
    while stem[-1] not in vowels:
        consonant = stem[-1] + consonant
        stem = stem[:-1]
    return consonant


# vim: et sw=4 sts=4
