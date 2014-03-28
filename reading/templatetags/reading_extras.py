#!/usr/bin/env python

from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()

from drills.views.vocab import remove_punctuation

@register.filter
@stringfilter
def click_for_definition(text):
    new_text = ''
    tag = '<span data-href="/definition/%s">%s</span> '
    for p in text.split('\n\n'):
        new_text += '<p>'
        p = p[3:-4]
        p = p.replace('<br />', ' ')
        for word in p.split():
            minus_punctuation = remove_punctuation(word).lower()
            new_text += tag % (minus_punctuation, word)
        new_text += '</p>'
    return mark_safe(new_text)


# vim: et sw=4 sts=4
