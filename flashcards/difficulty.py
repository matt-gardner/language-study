#!/usr/bin/env python

from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from memorizing.flashcards import common
from memorizing.flashcards.common import AjaxWord
from memorizing.flashcards.common import CardForm
from memorizing.flashcards.common import review_styles
from memorizing.flashcards.common import update_card_difficulty_from_session
from memorizing.flashcards.models import Card

import random
import simplejson

@login_required
def index(request):
    context = RequestContext(request)

    errors = request.session.get('errors', None)
    if errors:
        if isinstance(errors, list):
            context['errors'] = errors
        else:
            context['errors'] = [errors]
        del request.session['errors']

    context['greeting'] = 'Hello %s!' % request.user.first_name

    lists = request.user.cardlist_set.all()
    context['cardlists'] = lists

    context['review_styles'] = review_styles()
    context['review_style'] = '/difficulty/'

    list_name = request.session.get('cardlist-name', '')
    if list_name:
        cardlist = lists.get(name=list_name)
    else:
        cardlist = lists[0]
        request.session['cardlist-name'] = cardlist.name

    context['cardlist'] = cardlist
    context['add_card_form'] = CardForm()
    cards = cardlist.card_set.all()
    if cards:
        card, ave_difficulty = get_card_by_difficulty(cards)
        request.session['card-id'] = card.id
        context['card'] = card
        context['num_cards'] = cards.count()
        request.session['cards-reviewed'] = 0
        context['cards_reviewed'] = 0
        context['average_difficulty'] = ave_difficulty

    return render_to_response('difficulty.html', context)


def create_card_list(request):
    return common.create_card_list(request, '/difficulty/')


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
    request.session['cards-reviewed'] += 1

    cardlist_name = request.session['cardlist-name']
    cardlist = request.user.cardlist_set.get(name=cardlist_name)

    cards = cardlist.card_set.all()
    card, ave_difficulty = get_card_by_difficulty(cards)

    request.session['card-id'] = card.id
    request.session['cards-reviewed'] += 1

    ret_val = dict()
    ret_val['card'] = vars(AjaxWord(card))
    ret_val['num_cards'] = cardlist.card_set.count()
    ret_val['card_number'] = request.session['cards-reviewed']
    ret_val['difficulty'] = ave_difficulty
    return HttpResponse(simplejson.dumps(ret_val))


# vim: et sw=4 sts=4
