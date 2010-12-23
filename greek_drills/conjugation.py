#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from collections import defaultdict
from endings import *
from greek_util import add_recessive_accent, remove_accents, split_syllables

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
        self.make_ending_set_map()

    def conjugate(self, **kwargs):
        person, number, tense, mood, voice = self.check_kwargs(kwargs)
        principle_part = self.get_principle_part(tense, voice)
        stem = self.stem_principle_part(principle_part, tense, voice)
        ending = self.get_ending(tense, mood, voice, person, number,
                principle_part)
        augment = self.get_augment(tense, mood, principle_part)
        final_form = self.combine_parts(augment, stem, ending)
        if mood == 'Optative':
            return add_recessive_accent(final_form, optative=True)
        else:
            return add_recessive_accent(final_form)

    def check_kwargs(self, kwargs):
        if 'tense' not in kwargs:
            raise ValueError('Tense must be specified')
        tense = kwargs['tense']
        if 'mood' not in kwargs:
            raise ValueError('Mood must be specified')
        mood = kwargs['mood']
        if 'voice' not in kwargs:
            raise ValueError('Voice must be specified')
        voice = kwargs['voice']
        if 'person' not in kwargs and kwargs['mood'] != 'Infinitive':
            raise ValueError('Person must be specified')
        person = kwargs['person'] if 'person' in kwargs else None
        if 'number' not in kwargs and kwargs['mood'] != 'Infinitive':
            raise ValueError('Number must be specified')
        number = kwargs['number'] if 'number' in kwargs else None
        return person, number, tense, mood, voice

    def get_principle_part(self, tense, voice):
        return self.principle_parts[self.get_principle_part_index(tense, voice)]

    def get_principle_part_index(self, tense, voice):
        if tense in ['Present', 'Imperfect']:
            return 0
        elif tense == 'Future' and voice in ['Active', 'Middle', 'Deponent']:
            return 1
        elif tense == 'Aorist' and voice in ['Active', 'Middle', 'Deponent']:
            return 2
        elif tense in ['Perfect', 'Pluperfect'] and voice == 'Active':
            return 3
        elif tense in ['Perfect', 'Pluperfect'] and voice in ['Middle',
                'Passive', 'Deponent']:
            return 4
        elif tense == 'Aorist' and voice == 'Passive':
            return 5
        elif tense == 'Future' and voice == 'Passive':
            return 5
        raise ValueError("Something must have gone wrong, because I don't know "
                "what principle part to use...")

    def stem_principle_part(self, principle_part, tense, voice):
        """Note that this should remove accent marks."""
        # This will need to be selectively overridden, but there is enough
        # overlap to justify putting the bulk of the implementation here
        index = self.get_principle_part_index(tense, voice)
        if index == 0 or index == 1:
            if principle_part.endswith(u'ω'):
                return remove_accents(principle_part)[:-1]
            else:
                return remove_accents(principle_part)[:-4]
        if index == 2:
            if principle_part.endswith(u'α'):
                with_augment = remove_accents(principle_part)[:-1]
            #TODO: handle second aorist, root aorist, deponent forms
            if split_syllables(with_augment)[0] == u'ε':
                return with_augment[1:]
            #TODO: figure out how to handle cases with a tricky augment
        # TODO: the rest of the principle parts
        raise NotImplementedError()

    def make_ending_set_map(self):
        self.endings = defaultdict(dict)
        for tense in ['Present', 'Imperfect', 'Future', 'Aorist', 'Perfect',
                'Pluperfect']:
            self.endings[tense]['Active'] = dict()
            self.endings[tense]['Middle'] = dict()
            self.endings[tense]['Passive'] = dict()

        # Present Tense
        self.endings['Present']['Active']['Indicative'] = PresentIndAct()
        self.endings['Present']['Middle']['Indicative'] = PresentIndMP()
        self.endings['Present']['Passive']['Indicative'] = PresentIndMP()
        self.endings['Present']['Active']['Subjunctive'] = PresentSubjAct()
        self.endings['Present']['Middle']['Subjunctive'] = PresentSubjMP()
        self.endings['Present']['Passive']['Subjunctive'] = PresentSubjMP()
        self.endings['Present']['Active']['Optative'] = PresentOptAct()
        self.endings['Present']['Middle']['Optative'] = PresentOptMP()
        self.endings['Present']['Passive']['Optative'] = PresentOptMP()
        self.endings['Present']['Active']['Imperative'] = PresentImpAct()
        self.endings['Present']['Middle']['Imperative'] = PresentImpMP()
        self.endings['Present']['Passive']['Imperative'] = PresentImpMP()
        self.endings['Present']['Active']['Infinitive'] = PresentInfAct()
        self.endings['Present']['Middle']['Infinitive'] = PresentInfMP()
        self.endings['Present']['Passive']['Infinitive'] = PresentInfMP()

        # Imperfect Tense
        self.endings['Imperfect']['Active']['Indicative'] = ImperfectIndAct()
        self.endings['Imperfect']['Middle']['Indicative'] = ImperfectIndMP()
        self.endings['Imperfect']['Passive']['Indicative'] = ImperfectIndMP()

        # Future Tense
        self.endings['Future']['Active']['Indicative'] = PresentIndAct()
        self.endings['Future']['Middle']['Indicative'] = PresentIndMP()
        self.endings['Future']['Passive']['Indicative'] = PresentIndMP()
        self.endings['Future']['Active']['Optative'] = PresentOptAct()
        self.endings['Future']['Middle']['Optative'] = PresentOptMP()
        self.endings['Future']['Passive']['Optative'] = PresentOptMP()
        self.endings['Future']['Active']['Infinitive'] = PresentInfAct()
        self.endings['Future']['Middle']['Infinitive'] = PresentInfMP()
        self.endings['Future']['Passive']['Infinitive'] = PresentInfMP()

        # Aorist Tense
        self.endings['Aorist']['Active']['Indicative'] = AoristIndAct()
        #self.endings['Aorist']['Middle']['Indicative'] = AoristIndMP()
        #self.endings['Aorist']['Passive']['Indicative'] = AoristIndMP()
        #self.endings['Aorist']['Active']['Subjunctive'] = AoristSubjAct()
        #self.endings['Aorist']['Middle']['Subjunctive'] = AoristSubjMP()
        #self.endings['Aorist']['Passive']['Subjunctive'] = AoristSubjMP()
        #self.endings['Aorist']['Active']['Optative'] = AoristOptAct()
        #self.endings['Aorist']['Middle']['Optative'] = AoristOptMP()
        #self.endings['Aorist']['Passive']['Optative'] = AoristOptMP()
        #self.endings['Aorist']['Active']['Imperative'] = AoristImpAct()
        #self.endings['Aorist']['Middle']['Imperative'] = AoristImpMP()
        #self.endings['Aorist']['Passive']['Imperative'] = AoristImpMP()
        #self.endings['Aorist']['Active']['Infinitive'] = AoristInfAct()
        #self.endings['Aorist']['Middle']['Infinitive'] = AoristInfMP()
        #self.endings['Aorist']['Passive']['Infinitive'] = AoristInfMP()

        # Perfect Tense
        # Pluperfect Tense

    def get_ending(self, tense, mood, voice, person, number, principle_part):
        """We need the principle part to account for second aorist, root
        aorist, and other such things."""
        try:
            # TODO: add special cases here to check for second aorist and so on
            ending_set = self.endings[tense][voice][mood]
        except KeyError:
            raise ValueError('The specified combination of tense, mood and '
                    'voice (%s %s %s) either is not implemented yet or does '
                    'not exist' % (tense, mood, voice))
        try:
            return ending_set[person][number]
        except KeyError:
            raise ValueError('The specified person and number (%s %s) does not'
                    ' exist for the given tense, mood and voice (%s %s %s)' %
                    (person, number, tense, mood, voice))

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
