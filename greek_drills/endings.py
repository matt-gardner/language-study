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


class PresentSubjAct(EndingSet):
    def __init__(self):
        super(PresentSubjAct, self).__init__()
        self['First Person']['Singular'] = u'ω'
        self['Second Person']['Singular'] = u'ῃς'
        self['Third Person']['Singular'] = u'ῃ'
        self['First Person']['Plural'] = u'ωμεν'
        self['Second Person']['Plural'] = u'ητε'
        self['Third Person']['Plural'] = u'ωσι'


# vim: et sw=4 sts=4
