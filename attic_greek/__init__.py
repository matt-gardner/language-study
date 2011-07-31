#!/usr/bin/env python

from conjugation import GreekConjugation
from conjugation import AthematicConjugation
from declension import FirstDeclensionNoun
from declension import SecondDeclensionNoun
from declension import ThirdDeclensionNoun
from declension import GreekAdjectiveDeclension
from declension import ThirdDeclensionAdjective

mapping = {}
mapping['Thematic'] = GreekConjugation
mapping['Athematic'] = AthematicConjugation
mapping['First Declension'] = {'Noun': FirstDeclensionNoun,
        'Adjective': GreekAdjectiveDeclension}
mapping['Second Declension'] = {'Noun': SecondDeclensionNoun,
        'Adjective': GreekAdjectiveDeclension}
mapping['Third Declension'] = {'Noun': ThirdDeclensionNoun,
        'Adjective': ThirdDeclensionAdjective}


# vim: et sw=4 sts=4
