#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class EndingSet(dict):
    def __init__(self):
        self['First Person'] = {'Singular': u'', 'Plural': u''}
        self['Second Person'] = {'Singular': u'', 'Plural': u''}
        self['Third Person'] = {'Singular': u'', 'Plural': u''}


class PresentIndAct(EndingSet):
    def __init__(self):
        super(PresentIndAct, self).__init__()
        self['First Person']['Singular'] = u'ω'
        self['Second Person']['Singular'] = u'εις'
        self['Third Person']['Singular'] = u'ει'
        self['First Person']['Plural'] = u'ομεν'
        self['Second Person']['Plural'] = u'ετε'
        self['Third Person']['Plural'] = u'ουσι'


class ImperfectIndAct(EndingSet):
    def __init__(self):
        super(ImperfectIndAct, self).__init__()
        self['First Person']['Singular'] = u'ον'
        self['Second Person']['Singular'] = u'ες'
        self['Third Person']['Singular'] = u'ε'
        self['First Person']['Plural'] = u'ομεν'
        self['Second Person']['Plural'] = u'ετε'
        self['Third Person']['Plural'] = u'ον'


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


# vim: et sw=4 sts=4
