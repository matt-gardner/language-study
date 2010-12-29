#!/usr/bin/env python

from django import forms, template

register = template.Library()

@register.filter
def variablize(value):
    return unicode(value).lower().replace(' ', '_')


# vim: et sw=4 sts=4
