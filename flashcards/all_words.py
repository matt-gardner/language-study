#!/usr/bin/env python

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from memorizing.flashcards import common
from memorizing.flashcards.common import AjaxWord
from memorizing.flashcards.common import base_review_context
from memorizing.flashcards.common import review_styles
from memorizing.flashcards.models import Tag

@login_required
def index(request):
    context, cards = base_review_context(request)
    if cards:
        card_number = request.session.get('card-number', 0)
        if card_number >= len(cards):
            card_number = 0
        context['card'] = cards[card_number]
        request.session['card-id'] = cards[card_number].id
        request.session['card-number'] = card_number
        context['card_number'] = card_number + 1
    context['review_style'] = '/all-words/'
    request.session['cards'] = [AjaxWord(c) for c in cards]
    context['cards'] = cards

    return render_to_response('all_words.html', context)


def create_card_list(request):
    return common.create_card_list(request, '/all-words/')


def add_tag(request):
    return common.add_tag(request, '/all-words/')


def delete_card_list(request, name):
    return common.delete_card_list(request, name, '/all-words/')


def add_card_to_list(request):
    return common.add_card_to_list(request, '/all-words/')


# vim: et sw=4 sts=4
