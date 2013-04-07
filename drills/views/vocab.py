#!/usr/bin/env python

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

from datetime import datetime
from random import Random

from language_study.drills.views.common import AjaxWord
from language_study.drills.views.common import base_context

# Main vocab views
##################

@login_required
def main(request, listname):
    context = base_context(request)
    context['nav_page'] = 'nav_vocab'

    wordlist = request.user.wordlist_set.get(name=listname)
    context['wordlist'] = wordlist

    word, num_to_review, total = get_next_word(request, listname)
    context['first_number'] = num_to_review
    context['second_number'] = total
    context['word'] = word

    return render_to_response('vocab/review.html', context)


# Ajax requests
###############

def next_word(request, listname, correct):
    set_reviewed_from_session(request, listname, correct)
    word, num_to_review, total = get_next_word(request, listname)
    ret_val = dict()
    ret_val['word'] = vars(word)
    ret_val['first_number'] = num_to_review
    ret_val['second_number'] = total
    return HttpResponse(simplejson.dumps(ret_val))


# Helper methods
################

def get_next_word(request, listname):
    now = datetime.now()
    wordlist = request.user.wordlist_set.get(name=listname)
    words = wordlist.word_set
    needing_review = words.filter(next_review__lte=now).order_by('-next_review')
    num_needing_review = needing_review.count()
    if num_needing_review == 0:
        request.session['word-id'] = -1
        # To fix the crash when review the last word, make the None into some
        # reasonable "no more words" message - it crashes on the
        # ret_val['word'] = vars(word) line above.
        return None, num_needing_review, words.count()
    word_num = 0
    r = Random()
    while True:
        if r.random() < .3:
            break
        word_num += 1
        if word_num == num_needing_review:
            word_num = 0
    word = needing_review[word_num]
    request.session['word-id'] = word.id
    return AjaxWord(word), num_needing_review, words.count()


def set_reviewed_from_session(request, listname, correct):
    wordlist = request.user.wordlist_set.get(name=listname)
    word = wordlist.word_set.get(pk=request.session['word-id'])
    if correct == 'correct': correct = True
    if correct == 'wrong': correct = False
    if correct == 'neither': correct = None
    word.reviewed(correct)
    return word


# Extension requests
####################

def get_definition(request):
    return HttpResponse("<b>Success!</b><br>Word: " + request.GET['word']);

# vim: et sw=4 sts=4
