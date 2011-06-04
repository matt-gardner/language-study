#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unicodedata

from collections import defaultdict
from endings import *
from greek_util import acute_accent
from greek_util import add_final_circumflex
from greek_util import add_penult_accent
from greek_util import add_recessive_accent
from greek_util import add_athematic_optative_accent
from greek_util import breathings
from greek_util import circumflex
from greek_util import contract_vowels
from greek_util import get_final_consonant
from greek_util import get_last_vowel
from greek_util import get_matching_index
from greek_util import get_vowel
from greek_util import is_accent
from greek_util import is_accented
from greek_util import is_short
from greek_util import lengthen_vowel
from greek_util import remove_accents
from greek_util import remove_all_combining
from greek_util import remove_initial_vowel
from greek_util import shorten_vowel
from greek_util import split_syllables
from greek_util import starts_with_vowel
from greek_util import vowels
from language_study.drills.models import *

verbose = False

class Conjugation(object):
    def __init__(self):
        pass

    def conjugate(self, **kwargs):
        """Given a dictionary describing the desired form, return a list of
        acceptable forms.

        We use a dictionary here so that this can be used by a number of
        languages, not just those that have the same conjugation rules as
        Greek."""
        raise NotImplementedError()


class GreekConjugation(Conjugation):
    """Conjugates regular Greek verbs like παιδεύω into all possible forms

    Most of the alternate and irregular forms are still based off of the
    regular conjugation, so things like Athematic conjugations are best
    implemented as subclasses of this.  This class provides the basic structure
    of how to conjugate a Greek verb, so only parts will need to be overridden.
    """
    def __init__(self, principle_parts, verb_id=-1):
        self.original_word = principle_parts
        self.verb_id = verb_id
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
        stem = None
        if self.verb_id != -1:
            if self.is_irregular(person, number, tense, mood, voice):
                return [self.irregular_form(person, number, tense, mood, voice)]
            if self.is_irregular_stem(tense, mood, voice):
                stem = self.irregular_stem(tense, mood, voice)
        principle_part = self.get_principle_part(tense, voice)
        if stem == None:
            stem = self.stem_principle_part(principle_part, tense, mood, voice,
                    number)
        self.current_stem = stem
        ending = self.get_ending(tense, mood, voice, person, number,
                principle_part)
        augment = self.get_augment(tense, mood, principle_part)
        # TODO: add prefixes here
        final_form = self.combine_parts(augment, stem, ending, tense, mood,
                voice)
        accented = self.add_accent(final_form, mood, tense, voice,
                principle_part)
        if self.needs_contraction(tense, mood, voice, principle_part):
            accented = self.contract(accented, stem, ending)
        return [accented]

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
        if 'person' not in kwargs:
            raise ValueError('Person must be specified')
        person = kwargs['person']
        if 'number' not in kwargs:
            raise ValueError('Number must be specified')
        number = kwargs['number']
        return person, number, tense, mood, voice

    def is_irregular(self, person, number, tense, mood, voice):
        l = Language.objects.get(name='Attic Greek')
        p = Person.objects.get(name=person, language=l)
        n = Number.objects.get(name=number, language=l)
        t = Tense.objects.get(name=tense, language=l)
        m = Mood.objects.get(name=mood, language=l)
        v = Voice.objects.get(name=voice, language=l)
        ve = Verb.objects.get(pk=self.verb_id)
        try:
            IrregularVerbForm.objects.get(verb=ve, person=p, number=n, tense=t,
                    mood=m, voice=v)
            return True
        except IrregularVerbForm.DoesNotExist:
            return False

    def irregular_form(self, person, number, tense, mood, voice):
        l = Language.objects.get(name='Attic Greek')
        p = Person.objects.get(name=person, language=l)
        n = Number.objects.get(name=number, language=l)
        t = Tense.objects.get(name=tense, language=l)
        m = Mood.objects.get(name=mood, language=l)
        v = Voice.objects.get(name=voice, language=l)
        ve = Verb.objects.get(pk=self.verb_id)
        ivf = IrregularVerbForm.objects.get(verb=ve, person=p, number=n,
                tense=t, mood=m, voice=v)
        return unicodedata.normalize('NFKD', ivf.form)

    def is_irregular_stem(self, tense, mood, voice):
        l = Language.objects.get(name='Attic Greek')
        t = Tense.objects.get(name=tense, language=l)
        m = Mood.objects.get(name=mood, language=l)
        v = Voice.objects.get(name=voice, language=l)
        ve = Verb.objects.get(pk=self.verb_id)
        try:
            IrregularVerbStem.objects.get(verb=ve, tense=t, mood=m, voice=v)
            return True
        except IrregularVerbStem.DoesNotExist:
            return False

    def irregular_stem(self, tense, mood, voice):
        l = Language.objects.get(name='Attic Greek')
        t = Tense.objects.get(name=tense, language=l)
        m = Mood.objects.get(name=mood, language=l)
        v = Voice.objects.get(name=voice, language=l)
        ve = Verb.objects.get(pk=self.verb_id)
        ivs = IrregularVerbStem.objects.get(verb=ve, tense=t, mood=m, voice=v)
        return unicodedata.normalize('NFKD', ivs.stem)

    def is_irregular_augment(self, tense):
        l = Language.objects.get(name='Attic Greek')
        t = Tense.objects.get(name=tense, language=l)
        ve = Verb.objects.get(pk=self.verb_id)
        try:
            IrregularVerbAugmentedStem.objects.get(verb=ve, tense=t)
            return True
        except IrregularVerbAugmentedStem.DoesNotExist:
            return False

    def irregular_augment(self, tense):
        l = Language.objects.get(name='Attic Greek')
        t = Tense.objects.get(name=tense, language=l)
        ve = Verb.objects.get(pk=self.verb_id)
        ivs = IrregularVerbAugmentedStem.objects.get(verb=ve, tense=t)
        return unicodedata.normalize('NFKD', ivs.stem)

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

    def stem_principle_part(self, principle_part, tense, mood, voice, number):
        """Note that this should remove accent marks."""
        # We require tense and voice here so that we can determine which
        # principle part to use.  We also need tense so that we can tack on the
        # ησ in the future passive, as we just handle that here.
        # We need number for Athematic conjugations.  We have it here to
        # minimize the amount of code that needs to be overridden.  Athematic
        # conjugations also need the voice for the first principle part
        if not principle_part:
            raise ValueError('This verb is defective in that principle part')
        index = self.get_principle_part_index(tense, voice)
        if index == 0:
            return self.stem_first_pp(principle_part, tense, mood, voice,
                    number)
        elif index == 1:
            return self.stem_second_pp(principle_part, tense, voice)
        elif index == 2:
            return self.stem_third_pp(principle_part, tense, mood, voice,
                    number)
        elif index == 3:
            return self.stem_fourth_pp(principle_part, tense, voice)
        elif index == 4:
            return self.stem_fifth_pp(principle_part, tense, voice)
        elif index == 5:
            return self.stem_sixth_pp(principle_part, tense, voice)
        raise ValueError('Somehow get_principle_part_index returned a value '
                'outside of 0-5')

    def stem_first_pp(self, principle_part, tense, mood, voice, number):
        # We do this here because of Athematic conjugations.  The future stems
        # the same in both kinds of verbs, while the first principle part
        # changes.  If we put the thematic stemming in stem_second_pp, we can
        # override stem_first_pp in AthematicConjugation without causing
        # trouble to stemming future forms.
        return self.stem_second_pp(principle_part, tense, voice)

    def stem_second_pp(self, principle_part, tense, voice):
        if principle_part.endswith(u'ω'):
            return remove_accents(principle_part)[:-1]
        elif principle_part.endswith(u'ομαι'):
            return remove_accents(principle_part)[:-4]
        elif principle_part.endswith(u'ῶ'):
            # Here we assume an epsilon contraction, as that is the most
            # common
            return remove_accents(principle_part)[:-1] + u'ε'
        elif principle_part.endswith(u'οῦμαι'):
            # Again we assume epsilon
            return remove_accents(principle_part)[:-5] + u'ε'

    def stem_third_pp(self, principle_part, tense, mood, voice, number):
        if principle_part.endswith(u'α'):
            with_augment = remove_accents(principle_part)[:-1]
        elif principle_part.endswith(u'ον'):
            with_augment = remove_accents(principle_part)[:-2]
        elif principle_part.endswith(u'ν'):
            self.root_aorist = True
            self.long_vowel = principle_part[-2]
            self.short_vowel = get_short_vowel(self.long_vowel,
                    self.principle_parts)
            self.endings['Aorist']['Active']['Indicative'] = RootAoristIndAct()
            self.endings['Aorist']['Active']['Imperative'] = RootAoristImpAct()
            self.endings['Aorist']['Active']['Optative'] = AthPresentOptAct()
            self.endings['Aorist']['Active']['Infinitive'] = AthAoristInfAct()
            long_with_augment = remove_accents(principle_part)[:-1]
            if mood in ['Subjunctive', 'Optative']:
                with_augment = long_with_augment[:-1] + self.short_vowel
            else:
                with_augment = long_with_augment
        #TODO: handle deponent forms
        return self.remove_augment(with_augment)

    def stem_fourth_pp(self, principle_part, tense, voice):
        return remove_accents(principle_part)[:-1]

    def stem_fifth_pp(self, principle_part, tense, voice):
        return remove_accents(principle_part)[:-3]

    def stem_sixth_pp(self, principle_part, tense, voice):
        with_augment = remove_accents(principle_part)[:-2]
        no_augment = self.remove_augment(with_augment)
        if tense == 'Future':
            return no_augment + u'ησ'
        else:
            return no_augment

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
        tense, mood, voice = self.second_aorist_switch(tense, mood, voice,
                    principle_part)
        try:
            ending_set = self.endings[tense][voice][mood]
        except KeyError:
            raise ValueError('The specified combination of tense, mood and '
                    'voice (%s %s %s) does not exist' % (tense, mood, voice))
        try:
            return ending_set[person][number]
        except KeyError:
            raise ValueError('The specified person and number (%s %s) does not'
                    ' exist for the given tense, mood and voice (%s %s %s)' %
                    (person, number, tense, mood, voice))

    def second_aorist_switch(self, tense, mood, voice, principle_part):
        if tense == 'Aorist':
            if principle_part.endswith(u'ον'):
                if mood == 'Indicative':
                    return 'Imperfect', mood, voice
                else:
                    return 'Present', mood, voice
        return tense, mood, voice

    def get_augment(self, tense, mood, principle_part):
        if tense not in ['Imperfect', 'Aorist', 'Pluperfect']:
            return False
        if mood != 'Indicative':
            return False
        if tense == 'Pluperfect' and starts_with_vowel(self.principle_parts[0]):
            # I'm testing against the first principle part here; that might not
            # always work.
            return False
        return True

    def remove_augment(self, form):
        form = remove_accents(form)
        syllables = split_syllables(form)
        if syllables[0] == unicodedata.normalize('NFKD', u'ἐ'):
            # TODO: I'm sure this will break on some verbs
            return form[2:]
        else:
            vowel = get_vowel(syllables[0])
            without_augment = shorten_vowel(vowel, self.principle_parts)
            rest = remove_initial_vowel(syllables[0]) + u''.join(syllables[1:])
            for breathing in breathings:
                if breathing in syllables[0]:
                    without_augment += breathing
            return without_augment + rest
        #TODO: figure out how to handle cases with a tricky augment
        raise NotImplementedError()

    def add_augment(self, form, tense, voice):
        augmented_vowel = None
        if self.verb_id != -1 and self.is_irregular_augment(tense):
            augmented_vowel = self.irregular_augment(tense)
        if not augmented_vowel and not starts_with_vowel(form):
            return u'ἐ' + form
        #TODO: make this better.  This is a start, but it's not complete
        syllables = split_syllables(form)
        rest = remove_initial_vowel(syllables[0]) + u''.join(syllables[1:])
        if not augmented_vowel:
            vowel = get_vowel(syllables[0])
            augmented_vowel = lengthen_vowel(vowel)
        for breathing in breathings:
            if breathing in syllables[0]:
                augmented_vowel += breathing
        return unicodedata.normalize('NFKD', augmented_vowel + rest)

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
                form = self.add_augment(form, tense, voice)
            return form
        if augment:
            stem = self.add_augment(stem, tense, voice)
        if stem in breathings or stem == u'ε\u0313':
            # Silly special case, but it works...
            return stem[:-1] + ending[0] + stem[-1] + ending[1:]
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
        print stem, last_consonant
        raise ValueError("I found a consonant stem I didn't recognize")

    def add_accent(self, verb, mood, tense, voice, principle_part):
        # We need the principle part to check for second aorist and such
        # TODO: second aorist imperative second person singular is broken; it
        # needs a circumflex on the ultima.  How do we handle that?
        if mood == 'Optative':
            return add_recessive_accent(verb, optative=True)
        elif mood == 'Infinitive':
            if tense == 'Aorist':
                if principle_part.endswith(u'ον'):
                    if voice == 'Active':
                        return add_final_circumflex(verb)
                    elif voice == 'Middle':
                        return add_penult_accent(verb)
                elif voice in ['Active', 'Passive']:
                    return add_penult_accent(verb)
            elif tense == 'Perfect':
                return add_penult_accent(verb)
            elif tense == 'Present':
                if principle_part.endswith(u'μι') and voice == 'Active':
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

    def needs_contraction(self, tense, mood, voice, principle_part):
        # Mood and voice here are necessary because of athematic verbs
        if tense not in ['Present', 'Imperfect', 'Future', 'Aorist']:
            return False
        for ending in [u'έω', u'άω', u'όω', u'ῶ', u'όομαι', u'έομαι', u'άομαι',
                u'οῦμαι']:
            if principle_part.endswith(ending):
                return True
        # For root aorist
        if tense == 'Aorist' and voice != 'Passive':
            for ending in [u'ην', u'ων']:
                if principle_part.endswith(ending):
                    if mood in ['Subjunctive', 'Infinitive']:
                        return True
        return False

    def contract(self, form, stem, ending):
        # We want to remove the the front matter from the rest of stem so that
        # it's easier to find the end of it.  We just want to find the
        # pertinent vowels so that we can contract them.
        stem_to_remove = remove_initial_vowel(stem)
        stem_to_remove = remove_all_combining(stem_to_remove)
        if split_syllables(stem_to_remove)[-1][-1] in [u'α', u'ε', u'ο']:
            stem_to_remove = stem_to_remove[:-1]
        else:
            try:
                # Root aorists have a funny stem, but we still want to contract
                # the last vowel, so we take it out of stem_to_remove
                if self.root_aorist:
                    stem_to_remove = stem_to_remove[:-1]
            except AttributeError:
                pass
        # The stem doesn't have any diacritics, so we need to remove them from
        # the form.  They mess us up.
        no_diacritics = remove_all_combining(form)
        # Find the stem that we want to remove in the form
        start_index = no_diacritics.find(stem_to_remove)
        # Once we've found the start of the stem in the form, we need to look
        # for the end, starting at the starting place.  substr is the end of
        # the stem, either the last two characters, or the last character, or
        # empty, depending on how long the stem is.  If it's two characters, we
        # need to add one to end_index, because find gives us the beginning of
        # the location, not the end.
        if len(stem_to_remove) > 2:
            substr = stem_to_remove[-2:]
            add = 1
        elif len(stem_to_remove) > 0:
            substr = stem_to_remove[-1]
            add = 0
        else:
            substr = ''
            add = 0
        # After this, end_index holds the location of the end of the stem 
        # (the place we want to start getting vowels from) in no_diacritics
        end_index = no_diacritics.find(substr, start_index) + add
        # We removed diacritics from form, but we found end_index in
        # no_diacritics.  So we need to get the matching index in form.
        end_index = get_matching_index(no_diacritics, form, end_index)
        # Separate out the beginning that we're not going to modify, and hold
        # onto it for recombining when we're done
        beginning = form[:end_index]
        # rest should have the vowels we need to contract
        rest = form[end_index:]
        # but if there's a breathing or accent at the beginning of rest
        # (because end_index was 0, for instance), move it to beginning,
        # because it will mess us up
        if is_accent(rest[0], breathing=True):
            beginning += rest[0]
            rest = rest[1:]
        # The last vowel of the stem contracts with the first vowel of the
        # ending.  So remove the rest of the ending so we can isolate the
        # vowels we care about.
        ending_to_remove = remove_initial_vowel(ending)
        # Now we have the vowels we need to contract in vowels
        vowels = rest[:rest.rfind(ending_to_remove)]
        # The ending part that we removed will be tacked onto the end, so save
        # it here
        rest = ending_to_remove
        # We don't want to worry about vowels in the contraction lookup, so we
        # remove them.  But we need to know if it was accented so we can
        # reproduce the correct accent on the form.  So we save this here.
        accented = is_accented(vowels)
        # Handle spurious diphthongs (this is very likely incomplete)
        if ending == u'ειν':
            spurious = True
        else:
            spurious = False
        # This is pretty much for δίδωμι, though some other verbs do it too.
        # In those verbs, οῃ goes to ῳ instead of the usual οι.
        athematic = False
        if isinstance(self, AthematicConjugation):
            athematic = True
        # One of the other cases that does it is root verbs, like ἐγνων
        # We have this try except block instead of having every verb carry
        # around self.root_aorist.  We only set it when necessary.  Maybe
        # that's a silly way of doing it, and I should just set
        # self.root_aorist = False in __init__, but exceptions are cheap in
        # python.
        try:
            if self.root_aorist:
                athematic = True
        except AttributeError:
            pass
        # Finally, actually contract the vowels.
        vowels = contract_vowels(remove_accents(vowels), spurious, athematic)
        # Replace the accent, if necessary.  There is some logic to figure out
        # if we need a circumflex or an acute accent, but it looks
        # straightforward to me if you know the rules.
        if accented:
            num_syllables = len(split_syllables(ending_to_remove))
            last_vowel = get_last_vowel(rest)
            if (not last_vowel or is_short(last_vowel)) and num_syllables <= 1:
                vowels += circumflex
            else:
                vowels += acute_accent
        return unicodedata.normalize('NFKD', beginning + vowels + rest)


class AthematicConjugation(GreekConjugation):
    def __init__(self, principle_parts, verb_id=-1):
        super(AthematicConjugation, self).__init__(principle_parts, verb_id)
        base = remove_accents(self.principle_parts[0][:-2])
        self.long_vowel = get_last_vowel(base)
        self.using_long_vowel = False
        self.set_athematic_endings()
        self.special_case_endings()
        self.short_vowel = get_short_vowel(self.long_vowel,
                self.principle_parts)

    def set_athematic_endings(self):
        self.endings['Present']['Active']['Indicative'] = AthPresentIndAct()
        self.endings['Present']['Middle']['Indicative'] = AthPresentIndMP()
        self.endings['Present']['Passive']['Indicative'] = AthPresentIndMP()
        self.endings['Present']['Active']['Optative'] = AthPresentOptAct()
        self.endings['Present']['Middle']['Optative'] = AthPresentOptMP()
        self.endings['Present']['Passive']['Optative'] = AthPresentOptMP()
        self.endings['Present']['Active']['Imperative'] = AthPresentImpAct()
        self.endings['Present']['Middle']['Imperative'] = AthPresentImpMP()
        self.endings['Present']['Passive']['Imperative'] = AthPresentImpMP()
        self.endings['Present']['Active']['Infinitive'] = AthPresentInfAct()
        self.endings['Present']['Middle']['Infinitive'] = AthPresentInfMP()
        self.endings['Present']['Passive']['Infinitive'] = AthPresentInfMP()
        self.endings['Imperfect']['Active']['Indicative'] = AthImperfectIndAct()
        self.endings['Imperfect']['Middle']['Indicative'] = AthImperfectIndMP()
        self.endings['Imperfect']['Passive']['Indicative'] = AthImperfectIndMP()
        self.endings['Aorist']['Active']['Indicative'] = AthAoristIndAct()
        self.endings['Aorist']['Middle']['Indicative'] = AthAoristIndMid()
        self.endings['Aorist']['Active']['Optative'] = AthPresentOptAct()
        self.endings['Aorist']['Middle']['Optative'] = AthPresentOptMP()
        self.endings['Aorist']['Active']['Imperative'] = AthAoristImpAct()
        self.endings['Aorist']['Middle']['Imperative'] = AthAoristImpMid()
        self.endings['Aorist']['Active']['Infinitive'] = AthAoristInfAct()
        self.endings['Aorist']['Middle']['Infinitive'] = AthAoristInfMid()

    def special_case_endings(self):
        if self.principle_parts[0] in thematic_optative:
            self.endings['Present']['Active']['Optative'] = PresentOptAct()
            self.endings['Present']['Middle']['Optative'] = PresentOptMP()
            self.endings['Present']['Passive']['Optative'] = PresentOptMP()

    def conjugate(self, **kwargs):
        self.using_long_vowel = False
        return super(AthematicConjugation, self).conjugate(**kwargs)

    def stem_first_pp(self, principle_part, tense, mood, voice, number):
        if not remove_accents(principle_part).endswith(u'μι'):
            raise ValueError('Are you sure this is an athematic verb?')
        base = remove_accents(principle_part[:-2])
        last_vowel = get_last_vowel(base)
        index = base.rfind(last_vowel)
        base, rest = base[:index], base[index:]
        rest = rest.replace(last_vowel, '')
        without_vowel = base + rest
        if voice in ['Middle', 'Passive'] or mood != 'Indicative':
            vowel = self.short_vowel
        elif number == 'Singular':
            self.using_long_vowel = True
            vowel = self.long_vowel
        elif number == 'Plural':
            vowel = self.short_vowel
        else:
            raise ValueError("Something bad happened while stemming the first "
                    "principle part")
        if without_vowel in breathings:
            return vowel + without_vowel
        else:
            return without_vowel + vowel

    def stem_third_pp(self, principle_part, tense, mood, voice, number):
        if self.principle_parts[0] in stem_changers:
            long_with_augment = remove_accents(principle_part)[:-1]
            base, rest = long_with_augment[:-2], long_with_augment[-2:]
            if rest[0] in breathings:
                base_vowel = base[-1]
                base = base[:-1] + rest[0]
                rest = base_vowel + rest[1:]
            short_with_augment = base + self.short_vowel
            if (tense == 'Aorist' and mood == 'Indicative' and
                    voice == 'Active' and number == 'Singular'):
                stem = long_with_augment
            else:
                stem = short_with_augment
            return self.remove_augment(stem)
        if principle_part.endswith(u'ν'):
            self.root_aorist = True
            self.endings['Aorist']['Active']['Indicative'] = RootAoristIndAct()
            self.endings['Aorist']['Active']['Imperative'] = RootAoristImpAct()
            stem = remove_accents(principle_part)[:-1]
            return self.remove_augment(stem)
        else:
            return super(AthematicConjugation, self).stem_third_pp(
                    principle_part, tense, mood, voice, number)

    def needs_contraction(self, tense, mood, voice, principle_part):
        if super(AthematicConjugation, self).needs_contraction(tense, mood,
                voice, principle_part):
            return True
        if self.principle_parts[0] in no_subj_contract:
            return False
        if tense == 'Present' and mood == 'Subjunctive':
            return True
        if tense == 'Aorist' and mood == 'Subjunctive':
            return True
        if tense == 'Aorist' and mood == 'Infinitive' and voice == 'Active':
            return True
        return False

    def add_accent(self, verb, mood, tense, voice, principle_part):
        if (mood == 'Optative' and voice in ['Middle', 'Passive'] and
                tense in ['Present', 'Aorist']):
            if self.principle_parts[0] not in thematic_optative:
                return add_athematic_optative_accent(verb)
        if (self.long_vowel == u'υ' and mood == 'Indicative' and
                tense in ['Present', 'Imperfect']):
            if self.using_long_vowel and get_last_vowel(verb) == u'υ':
                return add_recessive_accent(verb, long_ending_vowel=True)
        return super(AthematicConjugation, self).add_accent(verb, mood, tense,
                voice, principle_part)


def get_short_vowel(long_vowel, principle_parts):
    if principle_parts[0] in hard_short_vowels:
        return hard_short_vowels[principle_parts[0]]
    elif long_vowel == u'ω':
        return u'ο'
    elif long_vowel == u'η':
        guess = remove_accents(principle_parts[5])[-4]
        if guess not in [u'α', u'ε']:
            raise ValueError("Oops, you caught me.  My hack for finding "
                    "the short vowel of μι verbs didn't work.")
        return guess
    elif long_vowel == u'υ':
        return u'υ'
    else:
        # For εἰμί, really
        return u''

stem_changers = [u'δίδωμι', u'τίθημι', u'ἵημι']
no_subj_contract = [u'δείκνυμι', u'εἰμί', u'εἶμι']
thematic_optative = [u'δείκνυμι', u'εἶμι']
hard_short_vowels = {u'φημί': u'α', u'εἶμι': u'ι', u'ἵημι': u'ε'}


if __name__ == '__main__':
    import unicodedata
    a = unicodedata.normalize('NFKD', u'ὰ')
    print [x for x in a]
    a = unicodedata.normalize('NFKD', u'α')
    print [x for x in a]

# vim: et sw=4 sts=4
