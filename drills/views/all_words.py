#!/usr/bin/env python

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from language_study.drills.views import common
from common import AjaxWord
from common import base_review_context
from common import get_word_info_from_session
from common import render_tags
from common import reorder_words_in_session
from common import review_styles
from language_study.drills.models import Tag

@login_required
def main(request, listname):
    context, words = base_review_context(request, listname)
    context['nav_page'] = 'nav_vocab'
    context['review_style'] = '/all-words/'
    if words:
        word_number = request.session.get('word-number', 0)
        if word_number >= len(words):
            word_number = 0
        request.session['word-id'] = words[word_number].id
        request.session['word-number'] = word_number
        request.session['words'] = [AjaxWord(c) for c in words]
        reorder_words_in_session(request, listname, word_number)
        word_info = get_word_info_from_session(request)
        context.update(word_info)
        context['words'] = request.session['words']
        context['word_tags'] = context['word']['tags']
    context['orderings'] = valid_orderings()
    context['ordering'] = request.session.get('ordering', 'date_entered')

    return render_to_response('vocab/all_words.html', context)


def valid_orderings():
    orderings = []
    orderings.append({'db_name': 'date_entered', 'name': 'Date Entered'})
    orderings.append({'db_name': 'alphabetical', 'name': 'Alphabetical'})
    orderings.append({'db_name': 'random', 'name': 'Randomize'})
    orderings.append({'db_name': 'last_reviewed', 'name': 'Last Reviewed'})
    orderings.append({'db_name': 'least_reviewed', 'name': 'Least Reviewed'})
    orderings.append({'db_name': 'difficulty', 'name': 'Difficulty'})
    return orderings


def add_tag(request):
    return common.add_tag(request, '/all-words/')


# vim: et sw=4 sts=4
