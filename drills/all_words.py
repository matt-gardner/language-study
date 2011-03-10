#!/usr/bin/env python

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from language_study.drills import common
from language_study.drills.common import AjaxWord
from language_study.drills.common import base_review_context
from language_study.drills.common import get_word_info_from_session
from language_study.drills.common import render_tags
from language_study.drills.common import reorder_words_in_session
from language_study.drills.common import review_styles
from language_study.drills.models import Tag

@login_required
def index(request):
    context, words = base_review_context(request)
    if words:
        word_number = request.session.get('word-number', 0)
        if word_number >= len(words):
            word_number = 0
        request.session['word-id'] = words[word_number].id
        request.session['word-number'] = word_number
    context['review_style'] = '/all-words/'
    request.session['words'] = [AjaxWord(c) for c in words]
    reorder_words_in_session(request, word_number)
    word_info = get_word_info_from_session(request)
    context.update(word_info)
    context['words'] = request.session['words']
    context['word_tags'] = context['word']['tags']
    context['ordering'] = request.session.get('ordering', 'date_entered')

    return render_to_response('all_words.html', context)


def create_word_list(request):
    return common.create_word_list(request, '/all-words/')


def add_tag(request):
    return common.add_tag(request, '/all-words/')


def delete_word_list(request, name):
    return common.delete_word_list(request, name, '/all-words/')


def add_word_to_list(request):
    return common.add_word_to_list(request, '/all-words/')


# vim: et sw=4 sts=4
