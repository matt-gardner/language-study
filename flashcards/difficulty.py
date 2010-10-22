#!/usr/bin/env python

from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render_to_response

from memorizing.flashcards import common
from memorizing.flashcards.common import AjaxWord
from memorizing.flashcards.common import base_review_context
from memorizing.flashcards.common import review_styles
from memorizing.flashcards.common import update_card_difficulty_from_session
from memorizing.flashcards.models import Card
from memorizing.flashcards.models import Tag

import random
import simplejson

@login_required
def index(request):
    context, cards = base_review_context(request)
    if cards:
        card, ave_difficulty = get_card_by_difficulty(cards)
        request.session['card-id'] = card.id
        context['card'] = card
        context['num_cards'] = cards.count()
        request.session['cards-reviewed'] = 0
        context['cards_reviewed'] = 0

    context['review_style'] = '/difficulty/'

    return render_to_response('difficulty.html', context)


def create_card_list(request):
    return common.create_card_list(request, '/difficulty/')


def add_tag(request):
    return common.add_tag(request, '/difficulty/')


def delete_card_list(request, name):
    return common.delete_card_list(request, name, '/difficulty/')


def add_card_to_list(request):
    return common.add_card_to_list(request, '/difficulty/')


def get_card_by_difficulty(cards):
    ave_difficulty = cards.aggregate(ave=Avg('average_difficulty'))['ave']
    stopping_difficulty = random.uniform(0, cards.count() * ave_difficulty)
    difficulty_so_far = 0
    for card in cards.all():
        difficulty_so_far += card.average_difficulty
        if difficulty_so_far > stopping_difficulty:
            break
    return card, ave_difficulty


def next_card(request, difficulty):
    update_card_difficulty_from_session(request, difficulty)

    cardlist_name = request.session['cardlist-name']
    cardlist = request.user.cardlist_set.get(name=cardlist_name)

    filters = request.session.get('filters', [])
    cards = cardlist.card_set
    cards, filter_form = filter_cards(cards, filters)
    card, ave_difficulty = get_card_by_difficulty(cards)

    request.session['card-id'] = card.id
    request.session['cards-reviewed'] += 1

    ret_val = dict()
    card = AjaxWord(card)
    card.get_tags()
    ret_val['card'] = vars(card)
    ret_val['num_cards'] = cards.count()
    ret_val['card_number'] = request.session['cards-reviewed']
    ret_val['difficulty'] = ave_difficulty
    return HttpResponse(simplejson.dumps(ret_val))


# vim: et sw=4 sts=4
