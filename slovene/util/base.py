#!/usr/bin/env python


vowels = [u'a', u'e', u'i', u'o', u'u']

def log_if_verbose(items):
    from slovene import declension#, conjugation
    if declension.verbose:# or conjugation.verbose:
        for item in items:
            print u'%s: %s' % (item, items[item])


# vim: et sw=4 sts=4
