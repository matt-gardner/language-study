#!/usr/bin/env python

from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render_to_response

from language_study.drills.views import common
from common import AjaxWord
from common import base_review_context
from common import render_tags
from common import update_word_difficulty_from_session
from language_study.drills.views.filters import filter_words
from language_study.drills.models import Word
from language_study.drills.models import Tag

import random
import simplejson

@login_required
def main(request):
    context, words = base_review_context(request)
    if words:
        word, ave_difficulty = get_word_by_difficulty(words)
        request.session['word-id'] = word.id
        context['word'] = word
        context['num_words'] = words.count()
        request.session['words-reviewed'] = 0
        context['words_reviewed'] = 0
    context['word_tags'] = render_tags(context['word'].tags.all())

    return render_to_response('vocab/difficulty.html', context)


def create_word_list(request):
    return common.create_word_list(request, '/difficulty/')


def add_tag(request):
    return common.add_tag(request, '/difficulty/')


def delete_word_list(request, name):
    return common.delete_word_list(request, name, '/difficulty/')


def add_word_to_list(request):
    return common.add_word_to_list(request, '/difficulty/')


def get_word_by_difficulty(words):
    ave_difficulty = words.aggregate(ave=Avg('average_difficulty'))['ave']
    stopping_difficulty = random.uniform(0, words.count() * ave_difficulty)
    difficulty_so_far = 0
    for word in words.all():
        difficulty_so_far += word.average_difficulty
        if difficulty_so_far > stopping_difficulty:
            break
    return word, ave_difficulty


def next_word(request, difficulty=None):
    if difficulty:
        update_word_difficulty_from_session(request, difficulty)
        request.session['words-reviewed'] += 1

    wordlist_name = request.session['wordlist-name']
    wordlist = request.user.wordlist_set.get(name=wordlist_name)

    filters = request.session.get('filters', [])
    words = wordlist.word_set
    words, filter_form = filter_words(words, filters)
    word, ave_difficulty = get_word_by_difficulty(words)

    request.session['word-id'] = word.id

    ret_val = dict()
    word = AjaxWord(word)
    word.get_tags()
    ret_val['word'] = vars(word)
    ret_val['num_words'] = words.count()
    ret_val['word_number'] = request.session['words-reviewed']
    ret_val['difficulty'] = ave_difficulty
    return HttpResponse(simplejson.dumps(ret_val))


# vim: et sw=4 sts=4
