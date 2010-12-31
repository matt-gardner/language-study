#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unicodedata

from collections import defaultdict
from endings import *
from greek_util import acute_accent
from greek_util import add_augment
from greek_util import add_penult_accent
from greek_util import add_recessive_accent
from greek_util import circumflex
from greek_util import contract_vowels
from greek_util import get_final_consonant
from greek_util import get_last_vowel
from greek_util import is_accented
from greek_util import remove_accents
from greek_util import remove_augment
from greek_util import remove_initial_vowel
from greek_util import short_vowels
from greek_util import split_syllables
from greek_util import vowels

class Conjugation(object):
    def __init__(self):
        pass

    def conjugate(self, **kwargs):
        """We use a dictionary here so that this can be used by a number of
        languages, not just those that have the same conjugation rules as
        Greek."""
        raise NotImplementedError()


class GreekConjugation(Conjugation):
    """Conjugates regular Greek verbs like παιδεύω into all possible forms

    Most of the alternate and irregular forms are still based off of the
    regular conjugation, so things like Athematic and Deponent conjugations are
    best implemented as subclasses of this.  This class provides the basic
    structure of how to conjugate a Greek verb, so only parts will need to be
    overridden.
    """
    def __init__(self, principle_parts):
        principle_parts = principle_parts.split(', ')
        if len(principle_parts) == 1:
            # We don't have the principle parts for the verb...  What do we do?
            pass
        if principle_parts[2] == 'etc.':
            # TODO: Take the second principle part and go from there
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
        # TODO: add prefixes here
        final_form = self.combine_parts(augment, stem, ending, tense, mood,
                voice)
        accented = self.add_accent(final_form, mood, tense, voice)
        if self.needs_contraction(tense, principle_part):
            accented = self.contract(accented, principle_part, ending)
        return accented

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
        # TODO: passive deponents are really handled correctly
        if tense in ['Present', 'Imperfect']:
            return 0
        elif tense == 'Future' and voice in ['Active', 'Middle', 'Deponent']:
            return 1
        elif tense == 'Aorist' and voice in ['Active', 'Middle', 'Deponent']:
            return 2
        elif tense in ['Perfect', 'Pluperfect'] and voice == 'Active':
            return 3
        elif tense in ['Perfect', 'Pluperfect']:
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
        # overlap to justify putting the bulk of the implementation here.
        # TODO: In order to selectively override parts of this, actually, this
        # needs to be split up into separate methods.
        if not principle_part:
            raise ValueError('This verb is defective in that principle part')
        index = self.get_principle_part_index(tense, voice)
        if index == 0 or index == 1:
            if principle_part.endswith(u'ω'):
                return remove_accents(principle_part)[:-1]
            else:
                return remove_accents(principle_part)[:-4]
        elif index == 2:
            if principle_part.endswith(u'α'):
                with_augment = remove_accents(principle_part)[:-1]
            #TODO: handle second aorist, root aorist, deponent forms
            return remove_augment(with_augment)
        elif index == 3:
            return remove_accents(principle_part)[:-1]
        elif index == 4:
            return remove_accents(principle_part)[:-3]
        elif index == 5:
            with_augment = remove_accents(principle_part)[:-2]
            no_augment = remove_augment(with_augment)
            if tense == 'Future':
                return no_augment + u'ησ'
            else:
                return no_augment
        raise NotImplementedError()

    def make_ending_set_map(self):
        """Maps tense, mood and voice combinations to sets of endings.

        When subclassing this (e.g. to make AthematicConjugation, or
        DeponentConjugation, or something) remove or change elements of the
        self.endings dictionary as needed.  For many subclasses most of the
        dictionary will stay the same.
        """
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
        self.endings['Aorist']['Middle']['Indicative'] = AoristIndMid()
        self.endings['Aorist']['Passive']['Indicative'] = AoristIndPass()
        self.endings['Aorist']['Active']['Subjunctive'] = PresentSubjAct()
        self.endings['Aorist']['Middle']['Subjunctive'] = PresentSubjMP()
        self.endings['Aorist']['Passive']['Subjunctive'] = AoristSubjPass()
        self.endings['Aorist']['Active']['Optative'] = AoristOptAct()
        self.endings['Aorist']['Middle']['Optative'] = AoristOptMid()
        self.endings['Aorist']['Passive']['Optative'] = AoristOptPass()
        self.endings['Aorist']['Active']['Imperative'] = AoristImpAct()
        self.endings['Aorist']['Middle']['Imperative'] = AoristImpMid()
        self.endings['Aorist']['Passive']['Imperative'] = AoristImpPass()
        self.endings['Aorist']['Active']['Infinitive'] = AoristInfAct()
        self.endings['Aorist']['Middle']['Infinitive'] = AoristInfMid()
        self.endings['Aorist']['Passive']['Infinitive'] = AoristInfPass()

        # Perfect Tense
        self.endings['Perfect']['Active']['Indicative'] = PerfectIndAct()
        self.endings['Perfect']['Middle']['Indicative'] = PerfectIndMP()
        self.endings['Perfect']['Passive']['Indicative'] = PerfectIndMP()
        # I'm not doing subjunctive, optative and imperative right now because
        # they are uncommon and they are tricky forms to get right, unless I do
        # it in a really ugly way
        # TODO: figure out how to do this the right way
        self.endings['Perfect']['Active']['Infinitive'] = PerfectInfAct()
        self.endings['Perfect']['Middle']['Infinitive'] = PerfectInfMP()
        self.endings['Perfect']['Passive']['Infinitive'] = PerfectInfMP()

        # Pluperfect Tense
        self.endings['Pluperfect']['Active']['Indicative'] = PluperfectIndAct()
        self.endings['Pluperfect']['Middle']['Indicative'] = PluperfectIndMP()
        self.endings['Pluperfect']['Passive']['Indicative'] = PluperfectIndMP()

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
        if tense not in ['Imperfect', 'Aorist', 'Pluperfect']:
            return False
        if mood != 'Indicative':
            return False
        return True

    def combine_parts(self, augment, stem, ending, tense, mood, voice):
        # I don't think this is different by conjugation; you just have to
        # worry about the augment.  We'll figure out the augment later.

        # TODO: add prefixes
        # TODO: fix the augment handling; we'll probably need more information
        if (tense in ['Perfect', 'Pluperfect'] and
                voice in ['Middle', 'Passive']):
            form = self.combine_consonant_stem(stem, ending)
            if augment and ' ' not in form:
                # DIRTY HACK, because I'm not handling compound forms correctly
                # TODO: fix this by doing compound forms right
                form = add_augment(form)
            return form
        if augment:
            stem = add_augment(stem)
        return stem + ending

    def combine_consonant_stem(self, stem, ending):
        if stem[-1] in vowels:
            # No consonant stem to worry about, so just do the normal thing
            return stem + ending
        if stem[-1] == u'λ':
            # With a λ, there is only one option, so convert it
            return stem[:-1] + ConsonantLambda.convert(ending)
        # If the perfect stem ends in anything else, we need to look at the
        # first principle part in order to determine what to do.
        if self.principle_parts[0]:
            last_consonant = get_final_consonant(self.principle_parts[0])
        else:
            # If there is no first principle part, we punt.
            return stem + ending
        # Now to test the cases that we have
        if stem[-1] == u'μ':
            # Perfect stem ends in μ, so we have three cases
            if last_consonant in [u'π', u'πτ', u'φ', u'β']:
                return stem[:-1] + ConsonantLabial.convert(ending)
            elif last_consonant == u'μπ':
                return stem[:-1] + ConsonantPempo.convert(ending)
            elif last_consonant == u'ν':
                return stem[:-1] + ConsonantNasal.convert(ending)
        elif stem[-1] == u'γ':
            # Perfect stem ends in γ, so we have two cases
            if last_consonant in [u'ττ', u'κ', u'χ', u'ξ']:
                return stem[:-1] + ConsonantPalatal.convert(ending)
            elif last_consonant in [u'γχ', u'γκ']:
                return stem[:-1] + ConsonantGK.convert(ending)
        elif stem[-1] == u'σ':
            # Perfect stem ends in σ, so we have two cases
            if last_consonant == u'ν':
                return stem[:-1] + ConsonantSigmaNasal.convert(ending)
            elif last_consonant == u'':
                return stem[:-1] + ConsonantAddedSigma.convert(ending)

    def add_accent(self, verb, mood, tense, voice):
        if mood == 'Optative':
            return add_recessive_accent(verb, optative=True)
        elif mood == 'Infinitive':
            if tense == 'Aorist' and voice in ['Active', 'Passive']:
                return add_penult_accent(verb)
            if tense == 'Perfect':
                return add_penult_accent(verb)
        elif tense == 'Aorist' and mood == 'Subjunctive' and voice == 'Passive':
            # Silly special case, but it was the easiest way to do this; the
            # endings already include the accent
            return unicodedata.normalize('NFKD', verb)
        elif (tense in ['Perfect', 'Pluperfect'] and
                voice in ['Middle', 'Passive'] and ' ' in verb):
            # Another silly special case... Oh well.  When I fix compound forms,
            # this should also be fixed. TODO
            return unicodedata.normalize('NFKD', verb)
        return add_recessive_accent(verb)

    def needs_contraction(self, tense, principle_part):
        if tense not in ['Present', 'Imperfect', 'Future']:
            return False
        for ending in [u'έω', u'άω', u'όω', u'ῶ', u'όομαι', u'έομαι', u'άομαι',
                u'οῦμαι']:
            if principle_part.endswith(ending):
                return True
        return False

    def contract(self, form, principle_part, ending):
        stem_to_remove = remove_initial_vowel(principle_part)
        if principle_part.endswith(u'ω'):
            stem_to_remove = stem_to_remove[:-1]
        elif principle_part.endswith(u'ομαι'):
            stem_to_remove = stem_to_remove[:-4]
        elif principle_part.endswith(u'ῶ'):
            stem_to_remove = stem_to_remove.replace(u'ῶ', u'')
        index = form.find(stem_to_remove) + len(stem_to_remove)
        beginning = form[:index]
        rest = form[index:]
        ending_to_remove = remove_initial_vowel(ending)
        vowels = rest.replace(ending_to_remove, u'')
        rest = ending_to_remove
        accented = is_accented(vowels)
        if ending == u'ειν':
            spurious = True
        else:
            spurious = False
        vowels = contract_vowels(remove_accents(vowels), spurious)
        if accented:
            last_vowel = get_last_vowel(rest)
            if not last_vowel or last_vowel in short_vowels:
                vowels += circumflex
            else:
                vowels += acute_accent
        return unicodedata.normalize('NFKD', beginning + vowels + rest)
        

class AthematicConjugation(GreekConjugation):
    def __init__(self, principle_parts):
        super(AthematicConjugation, self).__init__()
        # TODO: override self.endings


if __name__ == '__main__':
    import unicodedata
    a = unicodedata.normalize('NFKD', u'ὰ')
    print [x for x in a]
    a = unicodedata.normalize('NFKD', u'α')
    print [x for x in a]

# vim: et sw=4 sts=4
