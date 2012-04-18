#!/usr/bin/env python

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

from random import shuffle

from language_study.drills.views import common
from language_study.drills.views.common import AjaxWord
from language_study.drills.views.common import base_context
from language_study.drills.views.common import filter_words
from language_study.drills.views.common import render_tags
from language_study.drills.views.vocab import set_reviewed_from_session
from language_study.drills.models import Word

@login_required
def main(request, listname):
    context = base_context(request)
    context['nav_page'] = 'nav_vocab'

    wordlist = request.user.wordlist_set.get(name=listname)
    context['wordlist'] = wordlist

    context['tags'] = wordlist.tag_set.all()
    words = wordlist.word_set
    filters = request.session.get('filters', [])
    words, filter_form = filter_words(words, filters)
    context['filter'] = filter_form

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

    return render_to_response('vocab/manual.html', context)



# Ajax requests
###############

def add_tag(request, listname):
    return common.add_tag(request, listname, '/' + listname + '/vocab/')


def reorder_word_list(request, listname, ordering):
    request.session['ordering'] = ordering
    reorder_words_in_session(request, listname)
    return return_word_from_session(request)


def next_word(request, listname, correct=None):
    if correct:
        word = set_reviewed_from_session(request, listname, correct)
        ajaxword = request.session['words'][request.session['word-number']]
        ajaxword.time_in_memory = Word.REVIEW_PERIODS[word.memory_index][0]
        ajaxword.review_count = word.review_count
    request.session['word-number'] += 1
    return return_word_from_session(request)


def prev_word(request, listname):
    request.session['word-number'] -= 1
    return return_word_from_session(request)


def set_by_definition(request, listname, value):
    if value == 'true':
        request.session['by-definition'] = True
    else:
        request.session['by-definition'] = False
    return return_word_from_session(request)


# The general "return a word" AJAX function
###########################################

def return_word_from_session(request):
    return HttpResponse(simplejson.dumps(get_word_info_from_session(request)))


def get_word_info_from_session(request):
    ret_val = dict()
    words = request.session['words']
    num_words = len(words)
    current_word = request.session['word-number']
    current_word %= num_words
    request.session['word-number'] = current_word
    request.session['word-id'] = words[current_word].id
    words[current_word].get_tags()
    ret_val['by_definition'] = request.session.get('by-definition', False)
    ret_val['word'] = vars(words[current_word])
    ret_val['first_number'] = current_word + 1
    ret_val['second_number'] = num_words
    return ret_val


# Helper methods
################

def valid_orderings():
    orderings = []
    orderings.append({'db_name': 'random', 'name': 'Randomize'})
    orderings.append({'db_name': 'next_review', 'name': 'Next Needing Review'})
    orderings.append({'db_name': 'date_entered', 'name': 'Date Entered'})
    orderings.append({'db_name': 'alphabetical', 'name': 'Alphabetical'})
    orderings.append({'db_name': 'last_reviewed', 'name': 'Last Reviewed'})
    orderings.append({'db_name': 'last_wrong', 'name': 'Last Wrong'})
    orderings.append({'db_name': 'least_reviewed', 'name': 'Least Reviewed'})
    return orderings


def reorder_words_in_session(request, listname, word_number=0):
    ordering = request.session.get('ordering', 'date_entered')
    if ordering == 'random':
        shuffle(request.session['words'])
        request.session['word-number'] = 0
        return
    filters = request.session.get('filters', [])
    wordlist = request.user.wordlist_set.get(name=listname)
    words, _ = filter_words(wordlist.word_set, filters)
    if ordering == 'alphabetical':
        words = words.order_by('word')
    elif ordering == 'next_review':
        words = words.order_by('next_review')
    elif ordering == 'last_reviewed':
        words = words.order_by('last_reviewed')
    elif ordering == 'last_wrong':
        words = words.order_by('-last_wrong')
    elif ordering == 'least_reviewed':
        words = words.order_by('review_count')
    elif ordering == 'date_entered':
        words = words.order_by('date_entered')
    request.session['words'] = [AjaxWord(c) for c in words]
    request.session['word-number'] = word_number


# vim: et sw=4 sts=4
