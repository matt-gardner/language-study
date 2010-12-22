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


# Perfect Tense
###############


# Pluperfect Tense
##################



# vim: et sw=4 sts=4
