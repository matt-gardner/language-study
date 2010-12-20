#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from greek_util import add_recessive_accent, remove_accents
from endings import *

class Conjugation(object):
    def __init__(self):
        pass

    def conjugate(self, **kwargs):
        """We use a dictionary here so that this can be used by a number of
        languages, not just those that have the same conjugation rules as
        Greek."""
        raise NotImplementedError()


class GreekConjugation(Conjugation):
    def __init__(self, principle_parts):
        principle_parts = principle_parts.split(', ')
        if len(principle_parts) == 1:
            # We don't have the principle parts for the verb...  What do we do?
            pass
        if principle_parts[2] == 'etc.':
            # Take the second principle part and go from there
            pass
        self.principle_parts = []
        for part in principle_parts:
            if part == '_':
                self.principle_parts.append(None)
            else:
                self.principle_parts.append(part)

    def conjugate(self, **kwargs):
        person, number, tense, mood, voice = self.check_kwargs(kwargs)
        principle_part = self.get_principle_part(tense, voice)
        stem = self.stem_principle_part(principle_part, tense, voice)
        ending_set = self.get_ending_set(tense, mood, voice, principle_part)
        ending = ending_set[person][number]
        augment = self.get_augment(tense, mood, principle_part)
        final_form = self.combine_parts(augment, stem, ending)
        return add_recessive_accent(final_form)

    def check_kwargs(self, kwargs):
        if 'tense' not in kwargs:
            raise ValueError('Tense must be specified')
        if 'mood' not in kwargs:
            raise ValueError('Mood must be specified')
        if 'voice' not in kwargs:
            raise ValueError('Voice must be specified')
        if 'person' not in kwargs and kwargs['mood'] != 'Infinitive':
            raise ValueError('Person must be specified')
        if 'number' not in kwargs and kwargs['mood'] != 'Infinitive':
            raise ValueError('Number must be specified')
        return (kwargs['person'], kwargs['number'], kwargs['tense'],
                kwargs['mood'], kwargs['voice'])

    def get_principle_part(self, tense, voice):
        index = self.get_principle_part_index(tense, voice)
        return self.principle_parts[self.get_principle_part_index(tense, voice)]

    def get_principle_part_index(self, tense, voice):
        if tense in ['Present', 'Imperfect']:
            return 0
        if tense == 'Future' and voice in ['Active', 'Deponent']:
            return 1
        if tense == 'Aorist' and voice in ['Active', 'Middle', 'Deponent']:
            return 2
        if tense == 'Perfect' and voice == 'Active':
            return 3
        if tense == 'Perfect' and voice in ['Middle', 'Passive', 'Deponent']:
            return 4
        if tense == 'Aorist' and voice == 'Passive':
            return 5
        raise ValueError("Something must have gone wrong, because I don't know "
                "what principle part to use...")

    def stem_principle_part(self, principle_part, tense, voice):
        """Note that this should remove accent marks."""
        # This will need to be selectively overridden, but there is enough
        # overlap to justify putting the bulk of the implementation here
        index = self.get_principle_part_index(tense, voice)
        if index == 0 or index == 1:
            if voice == 'Active':
                return remove_accents(principle_part)[:-1]
            else:
                return remove_accents(principle_part)[:-4]
        # TODO: the rest of the principle parts


    def get_ending_set(self, tense, mood, voice, principle_part):
        """We need the principle part to account for second aorist, root
        aorist, and other such things."""
        index = self.get_principle_part_index(tense, voice)
        if index == 0 or index == 1:
            if voice == 'Active' and mood == 'Indicative':
                return PresentIndAct()
            if voice == 'Active' and mood == 'Subjunctive':
                if index == 1:
                    raise ValueError("Future subjunctive doesn't exist!")
                return PresentSubjAct()
        raise NotImplementedError()

    def get_augment(self, tense, mood, principle_part):
        if tense not in ['Imperfect', 'Aorist']:
            return ''
        if mood != 'Indicative':
            return ''
        # This is woefully inadequate, but it will work for now
        # Or maybe I should just return True and False, and let combine_parts()
        # take care of it...
        return u'ἐ'

    def combine_parts(self, augment, stem, ending):
        # I don't think this is different by conjugation; you just have to
        # worry about the augment.  We'll figure out the augment later.

        # Really bad right now, but it'll get better
        return augment + stem + ending


class ThematicConjugation(GreekConjugation):
    def get_ending_set(self, tense, mood, voice, principle_part):
        pass


if __name__ == '__main__':
    import unicodedata
    a = unicodedata.normalize('NFKD', u'ὰ')
    print [x for x in a]
    a = unicodedata.normalize('NFKD', u'α')
    print [x for x in a]

# vim: et sw=4 sts=4
