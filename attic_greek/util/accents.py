#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unicodedata

# Imports from base are ok up here.  Imports from vowels must be in the method
# that requires them.
from base import split_syllables
from base import log_if_verbose

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
    """Add a recessive accent to a verb form.

    Only verbs have a recessive accent, so we only really care about verbs
    here.  Thus we have the optative option.

    long_ending_vowel is for ambigious cases, like α, ι, υ, αι, and οι.
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


def fix_persistent_accent(form, long_ending_vowel=False):
    """Look at the accent on a persistently accented form and fix if needed.

    When we say "persistenly accented form" we mean a form that has kept its
    original accent while changing its ending.  The ending could have changed
    the necessary accent, or it could still be fine.  If the accent is fine as
    it is, we leave it alone.  If fixes are needed, we follow the rules and
    make the accent comply, keeping it as close to the original position as we
    can.
    """
    from vowels import get_last_vowel
    from vowels import long_except_at_end
    form = unicodedata.normalize('NFKD', form)
    last_vowel = get_last_vowel(form)
    # This is a tricky special case - αι and οι are only short if they end the
    # word; if they are followed by ς they are not short.  Putting this check
    # in here is the easiest way to handle this problem, though I guess it
    # really should be handled a little deeper.  That would just require too
    # much change to existing code.
    if last_vowel in long_except_at_end and form[-1] == u'ς':
        long_ending_vowel = True
    result = is_accent_legal(form, long_ending_vowel)
    attempts = 0
    while result != 'ACCENT_OK':
        attempts += 1
        if attempts > 3:
            raise RuntimeError("Failure in fix_persistent_accent.  Avoiding "
                    "infinite recursion")
        print form, result
        if result == 'ACCENT_TOO_FAR_BACK':
            form = remove_accents(form)
            form = add_recessive_accent(form,
                    long_ending_vowel=long_ending_vowel)
        elif result == 'CIRCUMFLEX_ON_SHORT_VOWEL':
            form = form.replace(circumflex, acute_accent)
        elif result == 'IMPROPER_GRAVE':
            form = form.replace(grave_accent, acute_accent)
        elif result == 'PENULT_NEEDS_ACUTE':
            form = form.replace(circumflex, acute_accent)
        elif result == 'PENULT_NEEDS_CIRCUMFLEX':
            form = form.replace(acute_accent, circumflex)
        result = is_accent_legal(form, long_ending_vowel)
    return form


def is_accent_legal(form, long_ending_vowel=False):
    """Check to see if the accent on a word is allowed by the rules of accents.

    This method is intended for use by nouns or other words with persistent
    accent, becase that's the way the code is structured.  We leave the accent
    on the word, then after the form has been declined we move the accent if
    it's necessary.  This method could be used by verbs if necessary, but there
    currently aren't any places where we do.
    """
    from vowels import get_vowel
    from vowels import is_short
    from vowels import long_except_at_end
    syllables = split_syllables(form)
    syllables.reverse()
    accented = None
    accent = None
    for i, syllable in enumerate(syllables):
        if is_accented(syllable):
            accented = i
            accent = get_accent(syllable)
    if accented is None:
        print form
        raise ValueError("There is no accent on this word")
    # Accent is on the last syllable
    if accented == 0:
        # Accent is "short" - always ok
        if accent in [acute_accent, grave_accent]:
            return 'ACCENT_OK'
        # Accent is circumflex and vowel is long - ok
        elif not is_short(get_vowel(syllables[accented]),
                long_ending_vowel=long_ending_vowel):
            return 'ACCENT_OK'
        # Accent is circumflex and vowel is short - bad
        else:
            return 'CIRCUMFLEX_ON_SHORT_VOWEL'
    # Accent is not on the last syllable, but accent is grave
    elif accent == grave_accent:
        return 'IMPROPER_GRAVE'
    # Accent is on penult
    elif accented == 1:
        # Short penult
        # Another special case where is_short breaks...  I should fix it,
        # instead of having these cases to work around it...
        if (is_short(get_vowel(syllables[accented])) and
                get_vowel(syllables[accented]) not in long_except_at_end):
            # Short penult - must be acute
            if accent == acute_accent:
                return 'ACCENT_OK'
            else:
                return 'CIRCUMFLEX_ON_SHORT_VOWEL'
        # Long penult
        else:
            if is_short(get_vowel(syllables[0]),
                    long_ending_vowel=long_ending_vowel):
                # Long penult and short ultima - must be circumflex
                if accent == circumflex:
                    return 'ACCENT_OK'
                else:
                    return 'PENULT_NEEDS_CIRCUMFLEX'
            else:
                # Long penult and long ultima - must be acute
                if accent == acute_accent:
                    return 'ACCENT_OK'
                else:
                    return 'PENULT_NEEDS_ACUTE'
    # Accent is on antepenult
    elif accented == 2:
        # Acute accent on penult with a short ending vowel - ok
        if accent == acute_accent:
            if is_short(get_vowel(syllables[0]),
                    long_ending_vowel=long_ending_vowel):
                return 'ACCENT_OK'
            else:
                return 'ACCENT_TOO_FAR_BACK'
        # Antepenult cannot have circumflex
        else:
            return ANTE_PENULT_NEEDS_ACUTE
    # Accent cannot be further back than the antepenult
    else:
        return 'ACCENT_TOO_FAR_BACK'


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
    return add_final_accent(word, circumflex)


def add_final_acute(word):
    return add_final_accent(word, acute_accent)


def add_final_accent(word, accent):
    from vowels import get_vowel
    from attic_greek import declension
    word = unicodedata.normalize('NFKD', word)
    syllables = split_syllables(word)
    last_vowel = get_vowel(syllables[-1])
    index = syllables[-1].find(last_vowel) + len(last_vowel)
    for syllable in syllables[:-1]:
        index += len(syllable)
    word = word[:index] + accent + word[index:]
    return unicodedata.normalize('NFKD', word)


def is_accented(word):
    for c in unicodedata.normalize('NFKD', word):
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
    """Get the breathing (if any) that is in word.

    Note that this assumes that there is at most one breathing in the word.
    None is returned if there is no breathing."""
    if smooth_breathing in word:
        return smooth_breathing
    if rough_breathing in word:
        return rough_breathing
    return None


def get_accent(word):
    """Get the accent (if any) that is in word.

    Note that this assumes that there is at most one accent on the word.  None
    is returned if there is no accent."""
    for accent in accents:
        if accent in word:
            return accent
    return None


# vim: et sw=4 sts=4
