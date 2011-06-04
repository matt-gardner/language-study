#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unicodedata

vowels = [u'α', u'ε', u'η', u'ι', u'ο', u'υ', u'ω']
diphthongs = [u'αι', u'αυ', u'ει', u'ευ', u'ηυ', u'οι', u'ου', u'ωυ']
short_vowels = [u'α', u'ε', u'ι', u'ο', u'υ', u'αι', u'οι']
ambiguous = [u'α', u'ι', u'υ']
long_optative = [u'οι', u'αι']
acute_accent = u'\u0301'
grave_accent = u'\u0300'
circumflex = u'\u0342'
smooth_breathing = u'\u0313'
rough_breathing = u'\u0314'
accents = set([acute_accent, grave_accent, circumflex])
breathings = set([smooth_breathing, rough_breathing])
acc_plus_breath = accents.union(breathings)


# Methods intended to be public
###############################

def add_recessive_accent(word, optative=False, long_ending_vowel=False):
    """long_ending_vowel is for ambigious cases, like α, ι, υ, αι, and οι.
    optative is so that the conjugation code doesn't have to check to see if
    the person and number asked for ends in οι.
    As we are adding accents here, we assume that there are no accents in
    the word already.
    """
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
    syllables = split_syllables(word)
    last_vowel = get_vowel(syllables[-1])
    index = word.find(last_vowel) + len(last_vowel)
    word = word[:index] + circumflex + word[index:]
    return unicodedata.normalize('NFKD', word)


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


def remove_accents(word, breathing=False):
    # This removes accents and breathing marks while leaving the diaeresis and
    # subscript iota
    normalized = unicodedata.normalize('NFKD', unicode(word))
    return u''.join([c for c in normalized if not is_accent(c, breathing)])


def remove_all_combining(word):
    normalized = unicodedata.normalize('NFKD', unicode(word))
    return u''.join([c for c in normalized if not unicodedata.combining(c)])


def is_accented(word):
    for c in word:
        if is_accent(c):
            return True
    return False


def get_breathing(word):
    if smooth_breathing in word:
        return smooth_breathing
    if rough_breathing in word:
        return rough_breathing
    return None


def starts_with_vowel(word):
    if len(word) == 0:
        return False
    normalized = unicodedata.normalize('NFKD', word)
    word = u''.join([c for c in normalized if not unicodedata.combining(c)])
    return word[0] in vowels


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


def lengthen_vowel(vowel):
    if vowel == u'ει':
        return u'ῃ'
    elif vowel == u'ε':
        return u'η'
    elif vowel == u'η':
        return u'η'
    elif vowel == u'α':
        return u'η'
    elif vowel == u'ι':
        return u'ι'


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


# Methods that are intended to be private
#########################################
# These methods might be useful in other places, so I'm not munging them with
# a preceding _, but generally they are just helper methods for the public
# methods above

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
    if len(syllables) == 1:
        return syllables
    if last_non_combining_character(syllables[-1]) not in vowels:
        last = syllables.pop()
        syllables[-1] = syllables[-1] + last
    return syllables


def last_non_combining_character(word):
    if not word:
        return u''
    final = u''.join([c for c in word if not unicodedata.combining(c)])
    if final:
        return final[-1]
    else:
        return u''


def get_vowel(syllable):
    """This assumes that syllable is output from split_syllables, so all vowels
    are contiguous, and consonants only appear at the beginning and at the end
    of the syllable.  Thus all we need to do is strip consonants and combining
    characters.
    """
    syllable = remove_accents(syllable)
    return u''.join([c for c in syllable if c in vowels])


def get_last_vowel(word):
    """This does not assume that the word has been split into syllables.  Just
    look at the last vowel and tell me if it's long.
    """
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


def get_final_consonant(word):
    """This assumes that we are looking at the first principle part.

    The purpose of this method is as an aid to determining how to deal with
    consonant stems in the perfect tenses, so we just care about the first
    principle part.
    """
    word = remove_accents(word)
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


# For testing things
####################

def main():
    words = [u'παιδεύω', u'παιδεύῃς', u'βιβλίου', u'δώρου', u'θεός', u'οἰκία']
    for word in words:
        print word, remove_accents(word),
        syllables = split_syllables(word)
        print '-'.join(syllables),
        print add_recessive_accent(remove_accents(word))


if __name__ == '__main__':
    main()

# vim: et sw=4 sts=4
