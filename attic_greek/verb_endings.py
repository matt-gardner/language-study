#!/usr/bin/env python
# -*- encoding: utf-8 -*-

##############
# Base Classes
##############

class VerbEndingSet(dict):
    def __init__(self):
        self['First Person'] = {'Singular': u'', 'Plural': u''}
        self['Second Person'] = {'Singular': u'', 'Plural': u''}
        self['Third Person'] = {'Singular': u'', 'Plural': u''}


class InfEndingSet(dict):
    def __init__(self):
        # The first arg is person, then number.  For an infinitive, both of
        # these are absent, represented in the database and the code with 'None'
        self['None'] = {'None': u''}


##################
# Thematic Endings
##################

# Present Tense
###############

class PresentIndAct(VerbEndingSet):
    def __init__(self):
        super(PresentIndAct, self).__init__()
        self['First Person']['Singular'] = u'ω'
        self['Second Person']['Singular'] = u'εις'
        self['Third Person']['Singular'] = u'ει'
        self['First Person']['Plural'] = u'ομεν'
        self['Second Person']['Plural'] = u'ετε'
        self['Third Person']['Plural'] = u'ουσι'


class PresentSubjAct(VerbEndingSet):
    def __init__(self):
        super(PresentSubjAct, self).__init__()
        self['First Person']['Singular'] = u'ω'
        self['Second Person']['Singular'] = u'ῃς'
        self['Third Person']['Singular'] = u'ῃ'
        self['First Person']['Plural'] = u'ωμεν'
        self['Second Person']['Plural'] = u'ητε'
        self['Third Person']['Plural'] = u'ωσι'


class PresentOptAct(VerbEndingSet):
    def __init__(self):
        super(PresentOptAct, self).__init__()
        self['First Person']['Singular'] = u'οιμι'
        self['Second Person']['Singular'] = u'οις'
        self['Third Person']['Singular'] = u'οι'
        self['First Person']['Plural'] = u'οιμεν'
        self['Second Person']['Plural'] = u'οιτε'
        self['Third Person']['Plural'] = u'οιεν'


class PresentImpAct(VerbEndingSet):
    def __init__(self):
        super(PresentImpAct, self).__init__()
        del self['First Person']
        self['Second Person']['Singular'] = u'ε'
        self['Third Person']['Singular'] = u'ετω'
        self['Second Person']['Plural'] = u'ετε'
        self['Third Person']['Plural'] = u'οντων'


class PresentInfAct(InfEndingSet):
    def __init__(self):
        super(PresentInfAct, self).__init__()
        self['None']['None'] = u'ειν'


class PresentIndMP(VerbEndingSet):
    def __init__(self):
        super(PresentIndMP, self).__init__()
        self['First Person']['Singular'] = u'ομαι'
        self['Second Person']['Singular'] = u'ει'
        self['Third Person']['Singular'] = u'εται'
        self['First Person']['Plural'] = u'ομεθα'
        self['Second Person']['Plural'] = u'εσθε'
        self['Third Person']['Plural'] = u'ονται'


class PresentSubjMP(VerbEndingSet):
    def __init__(self):
        super(PresentSubjMP, self).__init__()
        self['First Person']['Singular'] = u'ωμαι'
        self['Second Person']['Singular'] = u'ῃ'
        self['Third Person']['Singular'] = u'ηται'
        self['First Person']['Plural'] = u'ωμεθα'
        self['Second Person']['Plural'] = u'ησθε'
        self['Third Person']['Plural'] = u'ωνται'


class PresentOptMP(VerbEndingSet):
    def __init__(self):
        super(PresentOptMP, self).__init__()
        self['First Person']['Singular'] = u'οιμην'
        self['Second Person']['Singular'] = u'οιο'
        self['Third Person']['Singular'] = u'οιτο'
        self['First Person']['Plural'] = u'οιμεθα'
        self['Second Person']['Plural'] = u'οισθε'
        self['Third Person']['Plural'] = u'οιντο'


class PresentImpMP(VerbEndingSet):
    def __init__(self):
        super(PresentImpMP, self).__init__()
        del self['First Person']
        self['Second Person']['Singular'] = u'ου'
        self['Third Person']['Singular'] = u'εσθω'
        self['Second Person']['Plural'] = u'εσθε'
        self['Third Person']['Plural'] = u'εσθων'


class PresentInfMP(InfEndingSet):
    def __init__(self):
        super(PresentInfMP, self).__init__()
        self['None']['None'] = u'εσθαι'



# Imperfect Tense
#################

class ImperfectIndAct(VerbEndingSet):
    def __init__(self):
        super(ImperfectIndAct, self).__init__()
        self['First Person']['Singular'] = u'ον'
        self['Second Person']['Singular'] = u'ες'
        self['Third Person']['Singular'] = u'ε'
        self['First Person']['Plural'] = u'ομεν'
        self['Second Person']['Plural'] = u'ετε'
        self['Third Person']['Plural'] = u'ον'


class ImperfectIndMP(VerbEndingSet):
    def __init__(self):
        super(ImperfectIndMP, self).__init__()
        self['First Person']['Singular'] = u'ομην'
        self['Second Person']['Singular'] = u'ου'
        self['Third Person']['Singular'] = u'ετο'
        self['First Person']['Plural'] = u'ομεθα'
        self['Second Person']['Plural'] = u'εσθε'
        self['Third Person']['Plural'] = u'οντο'


# Future Tense
##############


# Aorist Tense
##############

class AoristIndAct(VerbEndingSet):
    def __init__(self):
        super(AoristIndAct, self).__init__()
        self['First Person']['Singular'] = u'α'
        self['Second Person']['Singular'] = u'ας'
        self['Third Person']['Singular'] = u'ε'
        self['First Person']['Plural'] = u'αμεν'
        self['Second Person']['Plural'] = u'ατε'
        self['Third Person']['Plural'] = u'αν'


# Aorist Subjunctive Active uses present endings

class AoristOptAct(VerbEndingSet):
    def __init__(self):
        super(AoristOptAct, self).__init__()
        self['First Person']['Singular'] = u'αιμι'
        self['Second Person']['Singular'] = u'αις'
        self['Third Person']['Singular'] = u'αι'
        self['First Person']['Plural'] = u'αιμεν'
        self['Second Person']['Plural'] = u'αιτε'
        self['Third Person']['Plural'] = u'αιεν'


class AoristImpAct(VerbEndingSet):
    def __init__(self):
        super(AoristImpAct, self).__init__()
        del self['First Person']
        self['Second Person']['Singular'] = u'ον'
        self['Third Person']['Singular'] = u'ατω'
        self['Second Person']['Plural'] = u'ατε'
        self['Third Person']['Plural'] = u'αντων'


class AoristInfAct(InfEndingSet):
    def __init__(self):
        super(AoristInfAct, self).__init__()
        self['None']['None'] = u'αι'


class AoristIndMid(VerbEndingSet):
    def __init__(self):
        super(AoristIndMid, self).__init__()
        self['First Person']['Singular'] = u'αμην'
        self['Second Person']['Singular'] = u'ω'
        self['Third Person']['Singular'] = u'ατο'
        self['First Person']['Plural'] = u'αμεθα'
        self['Second Person']['Plural'] = u'ασθε'
        self['Third Person']['Plural'] = u'αντο'


# Aorist Subjunctive Middle uses present endings

class AoristOptMid(VerbEndingSet):
    def __init__(self):
        super(AoristOptMid, self).__init__()
        self['First Person']['Singular'] = u'αιμην'
        self['Second Person']['Singular'] = u'αιο'
        self['Third Person']['Singular'] = u'αιτο'
        self['First Person']['Plural'] = u'αιμεθα'
        self['Second Person']['Plural'] = u'αισθε'
        self['Third Person']['Plural'] = u'αιντο'


class AoristImpMid(VerbEndingSet):
    def __init__(self):
        super(AoristImpMid, self).__init__()
        del self['First Person']
        self['Second Person']['Singular'] = u'αι'
        self['Third Person']['Singular'] = u'ασθω'
        self['Second Person']['Plural'] = u'ασθε'
        self['Third Person']['Plural'] = u'ασθων'


class AoristInfMid(InfEndingSet):
    def __init__(self):
        super(AoristInfMid, self).__init__()
        self['None']['None'] = u'ασθαι'


class AoristIndPass(VerbEndingSet):
    def __init__(self):
        super(AoristIndPass, self).__init__()
        self['First Person']['Singular'] = u'ην'
        self['Second Person']['Singular'] = u'ης'
        self['Third Person']['Singular'] = u'η'
        self['First Person']['Plural'] = u'ημεν'
        self['Second Person']['Plural'] = u'ητε'
        self['Third Person']['Plural'] = u'ησαν'


class AoristSubjPass(VerbEndingSet):
    def __init__(self):
        super(AoristSubjPass, self).__init__()
        self['First Person']['Singular'] = u'ῶ'
        self['Second Person']['Singular'] = u'ῇς'
        self['Third Person']['Singular'] = u'ῇ'
        self['First Person']['Plural'] = u'ῶμεν'
        self['Second Person']['Plural'] = u'ῆτε'
        self['Third Person']['Plural'] = u'ῶσι'


class AoristOptPass(VerbEndingSet):
    def __init__(self):
        super(AoristOptPass, self).__init__()
        self['First Person']['Singular'] = u'ειην'
        self['Second Person']['Singular'] = u'ειης'
        self['Third Person']['Singular'] = u'ειη'
        self['First Person']['Plural'] = u'ειημεν'
        self['Second Person']['Plural'] = u'ειητε'
        self['Third Person']['Plural'] = u'ειησαν'


class AoristImpPass(VerbEndingSet):
    def __init__(self):
        super(AoristImpPass, self).__init__()
        del self['First Person']
        #TODO: the form ηθι needs to be worried about...
        self['Second Person']['Singular'] = u'ητι'
        self['Third Person']['Singular'] = u'ητω'
        self['Second Person']['Plural'] = u'ητε'
        self['Third Person']['Plural'] = u'εντων'


class AoristInfPass(InfEndingSet):
    def __init__(self):
        super(AoristInfPass, self).__init__()
        self['None']['None'] = u'ηναι'


# Perfect Tense
###############

class PerfectIndAct(VerbEndingSet):
    def __init__(self):
        super(PerfectIndAct, self).__init__()
        self['First Person']['Singular'] = u'α'
        self['Second Person']['Singular'] = u'ας'
        self['Third Person']['Singular'] = u'ε'
        self['First Person']['Plural'] = u'αμεν'
        self['Second Person']['Plural'] = u'ατε'
        self['Third Person']['Plural'] = u'ασι'

# No subjunctive, optative and imperative yet, because they are uncommon and
# tricky

class PerfectInfAct(InfEndingSet):
    def __init__(self):
        super(PerfectInfAct, self).__init__()
        self['None']['None'] = u'εναι'


class PerfectIndMP(VerbEndingSet):
    def __init__(self):
        super(PerfectIndMP, self).__init__()
        self['First Person']['Singular'] = u'μαι'
        self['Second Person']['Singular'] = u'σαι'
        self['Third Person']['Singular'] = u'ται'
        self['First Person']['Plural'] = u'μεθα'
        self['Second Person']['Plural'] = u'σθε'
        self['Third Person']['Plural'] = u'νται'


class PerfectInfMP(InfEndingSet):
    def __init__(self):
        super(PerfectInfMP, self).__init__()
        self['None']['None'] = u'σθαι'


# Pluperfect Tense
##################

class PluperfectIndAct(VerbEndingSet):
    def __init__(self):
        super(PluperfectIndAct, self).__init__()
        self['First Person']['Singular'] = u'η'
        self['Second Person']['Singular'] = u'ης'
        self['Third Person']['Singular'] = u'ει'
        self['First Person']['Plural'] = u'εμεν'
        self['Second Person']['Plural'] = u'ετε'
        self['Third Person']['Plural'] = u'εσαν'


class PluperfectIndMP(VerbEndingSet):
    def __init__(self):
        super(PluperfectIndMP, self).__init__()
        self['First Person']['Singular'] = u'μην'
        self['Second Person']['Singular'] = u'σο'
        self['Third Person']['Singular'] = u'το'
        self['First Person']['Plural'] = u'μεθα'
        self['Second Person']['Plural'] = u'σθε'
        self['Third Person']['Plural'] = u'ντο'


########################
# Consonant Stem Endings
########################

# These are a little different; we take an argument and return an ending,
# because that was the way it worked out best in the rest of the code

class ConsonantEndingSet(object):
    @staticmethod
    def convert(ending):
        raise NotImplementedError()


class ConsonantLambda(ConsonantEndingSet):
    @staticmethod
    def convert(ending):
        if ending == u'νται':
            return u'λμένοι εἰσί'
        elif ending == u'ντο':
            return u'λμένοι ἦσαν'
        elif ending.startswith(u'σθ'):
            return u'λ' + ending[1:]
        else:
            return u'λ' + ending


class ConsonantLabial(ConsonantEndingSet):
    @staticmethod
    def convert(ending):
        if ending == u'μαι':
            return u'μμαι'
        elif ending == u'σαι':
            return u'ψαι'
        elif ending == u'ται':
            return u'πται'
        elif ending == u'μεθα':
            return u'μμεθα'
        elif ending == u'σθε':
            return u'φθε'
        elif ending == u'νται':
            return u'μμένοι εἰσί'
        elif ending == u'μην':
            return u'μμην'
        elif ending == u'σο':
            return u'ψο'
        elif ending == u'το':
            return u'πτο'
        elif ending == u'ντο':
            return u'μμένοι ἦσαν'
        elif ending == u'σθαι':
            return u'φθαι'


class ConsonantPempo(ConsonantEndingSet):
    @staticmethod
    def convert(ending):
        if ending == u'μαι':
            return u'μμαι'
        elif ending == u'σαι':
            return u'μψαι'
        elif ending == u'ται':
            return u'μπται'
        elif ending == u'μεθα':
            return u'μμεθα'
        elif ending == u'σθε':
            return u'μφθε'
        elif ending == u'νται':
            return u'μμένοι εἰσί'
        elif ending == u'μην':
            return u'μμην'
        elif ending == u'σο':
            return u'μψο'
        elif ending == u'το':
            return u'μπτο'
        elif ending == u'ντο':
            return u'μμένοι ἦσαν'
        elif ending == u'σθαι':
            return u'μφθαι'


class ConsonantNasal(ConsonantEndingSet):
    @staticmethod
    def convert(ending):
        if ending == u'μαι':
            return u'μμαι'
        elif ending == u'σαι':
            return u'μμένος εἶ'
        elif ending == u'ται':
            return u'νται'
        elif ending == u'μεθα':
            return u'μμεθα'
        elif ending == u'σθε':
            return u'νθε'
        elif ending == u'νται':
            return u'μμένοι εἰσί'
        elif ending == u'μην':
            return u'μμην'
        elif ending == u'σο':
            return u'μμένος ἦσθα'
        elif ending == u'το':
            return u'ντο'
        elif ending == u'ντο':
            return u'μμένοι ἦσαν'
        elif ending == u'σθαι':
            return u'νθαι'


class ConsonantPalatal(ConsonantEndingSet):
    @staticmethod
    def convert(ending):
        if ending == u'μαι':
            return u'γμαι'
        elif ending == u'σαι':
            return u'ξαι'
        elif ending == u'ται':
            return u'κται'
        elif ending == u'μεθα':
            return u'γμεθα'
        elif ending == u'σθε':
            return u'χθε'
        elif ending == u'νται':
            return u'γμένοι εἰσί'
        elif ending == u'μην':
            return u'γμην'
        elif ending == u'σο':
            return u'ξο'
        elif ending == u'το':
            return u'κτο'
        elif ending == u'ντο':
            return u'γμένοι ἦσαν'
        elif ending == u'σθαι':
            return u'χθαι'


class ConsonantGK(ConsonantEndingSet):
    @staticmethod
    def convert(ending):
        if ending == u'μαι':
            return u'γμαι'
        elif ending == u'σαι':
            return u'γξαι'
        elif ending == u'ται':
            return u'γκται'
        elif ending == u'μεθα':
            return u'γμεθα'
        elif ending == u'σθε':
            return u'γχθε'
        elif ending == u'νται':
            return u'γμένοι εἰσί'
        elif ending == u'μην':
            return u'γμην'
        elif ending == u'σο':
            return u'γξο'
        elif ending == u'το':
            return u'γκτο'
        elif ending == u'ντο':
            return u'γμένοι ἦσαν'
        elif ending == u'σθαι':
            return u'γχθαι'


class ConsonantSigmaNasal(ConsonantEndingSet):
    @staticmethod
    def convert(ending):
        if ending == u'μαι':
            return u'σμαι'
        elif ending == u'σαι':
            return u'σμένος εἶ'
        elif ending == u'ται':
            return u'νται'
        elif ending == u'μεθα':
            return u'σμεθα'
        elif ending == u'σθε':
            return u'νθε'
        elif ending == u'νται':
            return u'σμένοι εἰσί'
        elif ending == u'μην':
            return u'σμην'
        elif ending == u'σο':
            return u'σμένος ἦσθα'
        elif ending == u'το':
            return u'ντο'
        elif ending == u'ντο':
            return u'σμένοι ἦσαν'
        elif ending == u'σθαι':
            return u'νθαι'


class ConsonantAddedSigma(ConsonantEndingSet):
    @staticmethod
    def convert(ending):
        if ending == u'μαι':
            return u'σμαι'
        elif ending == u'σαι':
            return u'σαι'
        elif ending == u'ται':
            return u'σται'
        elif ending == u'μεθα':
            return u'σμεθα'
        elif ending == u'σθε':
            return u'σθε'
        elif ending == u'νται':
            return u'σμένοι εἰσί'
        elif ending == u'μην':
            return u'σμην'
        elif ending == u'σο':
            return u'σο'
        elif ending == u'το':
            return u'στο'
        elif ending == u'ντο':
            return u'σμένοι ἦσαν'
        elif ending == u'σθαι':
            return u'σθαι'


###################
# Athematic Endings
###################

# Present Tense
###############

class AthPresentIndAct(VerbEndingSet):
    def __init__(self):
        super(AthPresentIndAct, self).__init__()
        self['First Person']['Singular'] = u'μι'
        self['Second Person']['Singular'] = u'ς'
        self['Third Person']['Singular'] = u'σι'
        self['First Person']['Plural'] = u'μεν'
        self['Second Person']['Plural'] = u'τε'
        self['Third Person']['Plural'] = u'ασι'


class AthPresentOptAct(VerbEndingSet):
    def __init__(self):
        super(AthPresentOptAct, self).__init__()
        self['First Person']['Singular'] = u'ιην'
        self['Second Person']['Singular'] = u'ιης'
        self['Third Person']['Singular'] = u'ιη'
        self['First Person']['Plural'] = u'ιημεν'
        self['Second Person']['Plural'] = u'ιητε'
        self['Third Person']['Plural'] = u'ιησαν'


class AthPresentImpAct(VerbEndingSet):
    def __init__(self):
        super(AthPresentImpAct, self).__init__()
        del self['First Person']
        self['Second Person']['Singular'] = u'θι'
        self['Third Person']['Singular'] = u'τω'
        self['Second Person']['Plural'] = u'τε'
        self['Third Person']['Plural'] = u'ντων'


class AthPresentInfAct(InfEndingSet):
    def __init__(self):
        super(AthPresentInfAct, self).__init__()
        self['None']['None'] = u'ναι'


class AthPresentIndMP(VerbEndingSet):
    def __init__(self):
        super(AthPresentIndMP, self).__init__()
        self['First Person']['Singular'] = u'μαι'
        self['Second Person']['Singular'] = u'σαι'
        self['Third Person']['Singular'] = u'ται'
        self['First Person']['Plural'] = u'μεθα'
        self['Second Person']['Plural'] = u'σθε'
        self['Third Person']['Plural'] = u'νται'


class AthPresentOptMP(VerbEndingSet):
    def __init__(self):
        super(AthPresentOptMP, self).__init__()
        self['First Person']['Singular'] = u'ιμην'
        self['Second Person']['Singular'] = u'ιο'
        self['Third Person']['Singular'] = u'ιτο'
        self['First Person']['Plural'] = u'ιμεθα'
        self['Second Person']['Plural'] = u'ισθε'
        self['Third Person']['Plural'] = u'ιντο'


class AthPresentImpMP(VerbEndingSet):
    def __init__(self):
        super(AthPresentImpMP, self).__init__()
        del self['First Person']
        self['Second Person']['Singular'] = u'σο'
        self['Third Person']['Singular'] = u'σθω'
        self['Second Person']['Plural'] = u'σθε'
        self['Third Person']['Plural'] = u'σθων'


class AthPresentInfMP(InfEndingSet):
    def __init__(self):
        super(AthPresentInfMP, self).__init__()
        self['None']['None'] = u'σθαι'



# Imperfect Tense
#################

class AthImperfectIndAct(VerbEndingSet):
    def __init__(self):
        super(AthImperfectIndAct, self).__init__()
        self['First Person']['Singular'] = u'ν'
        self['Second Person']['Singular'] = u'ς'
        self['Third Person']['Singular'] = u''
        self['First Person']['Plural'] = u'μεν'
        self['Second Person']['Plural'] = u'τε'
        self['Third Person']['Plural'] = u'σαν'


class AthImperfectIndMP(VerbEndingSet):
    def __init__(self):
        super(AthImperfectIndMP, self).__init__()
        self['First Person']['Singular'] = u'μην'
        self['Second Person']['Singular'] = u'σο'
        self['Third Person']['Singular'] = u'το'
        self['First Person']['Plural'] = u'μεθα'
        self['Second Person']['Plural'] = u'σθε'
        self['Third Person']['Plural'] = u'ντο'


# Aorist Tense
##############

class AthAoristIndAct(VerbEndingSet):
    def __init__(self):
        super(AthAoristIndAct, self).__init__()
        self['First Person']['Singular'] = u'α'
        self['Second Person']['Singular'] = u'ας'
        self['Third Person']['Singular'] = u'ε'
        self['First Person']['Plural'] = u'μεν'
        self['Second Person']['Plural'] = u'τε'
        self['Third Person']['Plural'] = u'σαν'


class RootAoristIndAct(VerbEndingSet):
    def __init__(self):
        super(RootAoristIndAct, self).__init__()
        self['First Person']['Singular'] = u'ν'
        self['Second Person']['Singular'] = u'ς'
        self['Third Person']['Singular'] = u''
        self['First Person']['Plural'] = u'μεν'
        self['Second Person']['Plural'] = u'τε'
        self['Third Person']['Plural'] = u'σαν'


class AthAoristImpAct(VerbEndingSet):
    def __init__(self):
        super(AthAoristImpAct, self).__init__()
        del self['First Person']
        self['Second Person']['Singular'] = u'ς'
        self['Third Person']['Singular'] = u'τω'
        self['Second Person']['Plural'] = u'τε'
        self['Third Person']['Plural'] = u'ντων'


class RootAoristImpAct(VerbEndingSet):
    def __init__(self):
        super(RootAoristImpAct, self).__init__()
        del self['First Person']
        self['Second Person']['Singular'] = u'θι'
        self['Third Person']['Singular'] = u'τω'
        self['Second Person']['Plural'] = u'τε'
        self['Third Person']['Plural'] = u'ντων'


class AthAoristInfAct(InfEndingSet):
    def __init__(self):
        super(AthAoristInfAct, self).__init__()
        self['None']['None'] = u'εναι'


class AthAoristIndMid(VerbEndingSet):
    def __init__(self):
        super(AthAoristIndMid, self).__init__()
        self['First Person']['Singular'] = u'μην'
        self['Second Person']['Singular'] = u'σο'
        self['Third Person']['Singular'] = u'το'
        self['First Person']['Plural'] = u'μεθα'
        self['Second Person']['Plural'] = u'σθε'
        self['Third Person']['Plural'] = u'ντο'


class AthAoristImpMid(VerbEndingSet):
    def __init__(self):
        super(AthAoristImpMid, self).__init__()
        del self['First Person']
        self['Second Person']['Singular'] = u'ο'
        self['Third Person']['Singular'] = u'σθω'
        self['Second Person']['Plural'] = u'σθε'
        self['Third Person']['Plural'] = u'σθων'


class AthAoristInfMid(InfEndingSet):
    def __init__(self):
        super(AthAoristInfMid, self).__init__()
        self['None']['None'] = u'σθαι'

# vim: et sw=4 sts=4
