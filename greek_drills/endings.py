#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class EndingSet(dict):
    def __init__(self):
        self['First Person'] = {'Singular': u'', 'Plural': u''}
        self['Second Person'] = {'Singular': u'', 'Plural': u''}
        self['Third Person'] = {'Singular': u'', 'Plural': u''}


class InfEndingSet(dict):
    def __init__(self):
        # The first arg is person, then number.  For an infinitive, both of
        # these are absent, represented in the code with None
        self[None] = {None: u''}


# Present Tense
###############

class PresentIndAct(EndingSet):
    def __init__(self):
        super(PresentIndAct, self).__init__()
        self['First Person']['Singular'] = u'ω'
        self['Second Person']['Singular'] = u'εις'
        self['Third Person']['Singular'] = u'ει'
        self['First Person']['Plural'] = u'ομεν'
        self['Second Person']['Plural'] = u'ετε'
        self['Third Person']['Plural'] = u'ουσι'


class PresentSubjAct(EndingSet):
    def __init__(self):
        super(PresentSubjAct, self).__init__()
        self['First Person']['Singular'] = u'ω'
        self['Second Person']['Singular'] = u'ῃς'
        self['Third Person']['Singular'] = u'ῃ'
        self['First Person']['Plural'] = u'ωμεν'
        self['Second Person']['Plural'] = u'ητε'
        self['Third Person']['Plural'] = u'ωσι'


class PresentOptAct(EndingSet):
    def __init__(self):
        super(PresentOptAct, self).__init__()
        self['First Person']['Singular'] = u'οιμι'
        self['Second Person']['Singular'] = u'οις'
        self['Third Person']['Singular'] = u'οι'
        self['First Person']['Plural'] = u'οιμεν'
        self['Second Person']['Plural'] = u'οιτε'
        self['Third Person']['Plural'] = u'οιεν'


class PresentImpAct(EndingSet):
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
        self[None][None] = u'ειν'


class PresentIndMP(EndingSet):
    def __init__(self):
        super(PresentIndMP, self).__init__()
        self['First Person']['Singular'] = u'ομαι'
        self['Second Person']['Singular'] = u'ει'
        self['Third Person']['Singular'] = u'εται'
        self['First Person']['Plural'] = u'ομεθα'
        self['Second Person']['Plural'] = u'εσθε'
        self['Third Person']['Plural'] = u'ονται'


class PresentSubjMP(EndingSet):
    def __init__(self):
        super(PresentSubjMP, self).__init__()
        self['First Person']['Singular'] = u'ωμαι'
        self['Second Person']['Singular'] = u'ῃ'
        self['Third Person']['Singular'] = u'ηται'
        self['First Person']['Plural'] = u'ωμεθα'
        self['Second Person']['Plural'] = u'ησθε'
        self['Third Person']['Plural'] = u'ωνται'


class PresentOptMP(EndingSet):
    def __init__(self):
        super(PresentOptMP, self).__init__()
        self['First Person']['Singular'] = u'οιμην'
        self['Second Person']['Singular'] = u'οιο'
        self['Third Person']['Singular'] = u'οιτο'
        self['First Person']['Plural'] = u'οιμεθα'
        self['Second Person']['Plural'] = u'οισθε'
        self['Third Person']['Plural'] = u'οιντο'


class PresentImpMP(EndingSet):
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
        self[None][None] = u'εσθαι'



# Imperfect Tense
#################

class ImperfectIndAct(EndingSet):
    def __init__(self):
        super(ImperfectIndAct, self).__init__()
        self['First Person']['Singular'] = u'ον'
        self['Second Person']['Singular'] = u'ες'
        self['Third Person']['Singular'] = u'ε'
        self['First Person']['Plural'] = u'ομεν'
        self['Second Person']['Plural'] = u'ετε'
        self['Third Person']['Plural'] = u'ον'


class ImperfectIndMP(EndingSet):
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

class AoristIndAct(EndingSet):
    def __init__(self):
        super(AoristIndAct, self).__init__()
        self['First Person']['Singular'] = u'α'
        self['Second Person']['Singular'] = u'ας'
        self['Third Person']['Singular'] = u'ε'
        self['First Person']['Plural'] = u'αμεν'
        self['Second Person']['Plural'] = u'ατε'
        self['Third Person']['Plural'] = u'αν'


# Aorist Subjunctive Active uses present endings

class AoristOptAct(EndingSet):
    def __init__(self):
        super(AoristOptAct, self).__init__()
        self['First Person']['Singular'] = u'αιμι'
        self['Second Person']['Singular'] = u'αις'
        self['Third Person']['Singular'] = u'αι'
        self['First Person']['Plural'] = u'αιμεν'
        self['Second Person']['Plural'] = u'αιτε'
        self['Third Person']['Plural'] = u'αιεν'


class AoristImpAct(EndingSet):
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
        self[None][None] = u'αι'


class AoristIndMid(EndingSet):
    def __init__(self):
        super(AoristIndMid, self).__init__()
        self['First Person']['Singular'] = u'αμην'
        self['Second Person']['Singular'] = u'ω'
        self['Third Person']['Singular'] = u'ατο'
        self['First Person']['Plural'] = u'αμεθα'
        self['Second Person']['Plural'] = u'ασθε'
        self['Third Person']['Plural'] = u'αντο'


# Aorist Subjunctive Middle uses present endings

class AoristOptMid(EndingSet):
    def __init__(self):
        super(AoristOptMid, self).__init__()
        self['First Person']['Singular'] = u'αιμην'
        self['Second Person']['Singular'] = u'αιο'
        self['Third Person']['Singular'] = u'αιτο'
        self['First Person']['Plural'] = u'αιμεθα'
        self['Second Person']['Plural'] = u'αισθε'
        self['Third Person']['Plural'] = u'αιντο'


class AoristImpMid(EndingSet):
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
        self[None][None] = u'ασθαι'


class AoristIndPass(EndingSet):
    def __init__(self):
        super(AoristIndPass, self).__init__()
        self['First Person']['Singular'] = u'ην'
        self['Second Person']['Singular'] = u'ης'
        self['Third Person']['Singular'] = u'η'
        self['First Person']['Plural'] = u'ημεν'
        self['Second Person']['Plural'] = u'ητε'
        self['Third Person']['Plural'] = u'ησαν'


class AoristSubjPass(EndingSet):
    def __init__(self):
        super(AoristSubjPass, self).__init__()
        self['First Person']['Singular'] = u'ῶ'
        self['Second Person']['Singular'] = u'ῇς'
        self['Third Person']['Singular'] = u'ῇ'
        self['First Person']['Plural'] = u'ῶμεν'
        self['Second Person']['Plural'] = u'ῆτε'
        self['Third Person']['Plural'] = u'ῶσι'


class AoristOptPass(EndingSet):
    def __init__(self):
        super(AoristOptPass, self).__init__()
        self['First Person']['Singular'] = u'ειην'
        self['Second Person']['Singular'] = u'ειης'
        self['Third Person']['Singular'] = u'ειη'
        self['First Person']['Plural'] = u'ειημεν'
        self['Second Person']['Plural'] = u'ειητε'
        self['Third Person']['Plural'] = u'ειησαν'


class AoristImpPass(EndingSet):
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
        self[None][None] = u'ηναι'


# Perfect Tense
###############


class PerfectIndAct(EndingSet):
    pass

# Pluperfect Tense
##################



# vim: et sw=4 sts=4
