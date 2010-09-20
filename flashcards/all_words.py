#!/usr/bin/env python

from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import render_to_response
from django.template import RequestContext

from memorizing.flashcards import common
from memorizing.flashcards.common import AjaxWord
from memorizing.flashcards.common import CardForm
from memorizing.flashcards.common import review_styles
from memorizing.flashcards.models import Tag

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
    context['review_style'] = '/all-words/'

    list_name = request.session.get('cardlist-name', '')
    if list_name:
        cardlist = lists.get(name=list_name)
    else:
        cardlist = lists[0]
        request.session['cardlist-name'] = cardlist.name

    context['cardlist'] = cardlist
    context['tags'] = cardlist.tag_set.all()
    context['add_card_form'] = CardForm()
    cards = cardlist.card_set.all()
    request.session['cards'] = [AjaxWord(c) for c in cards]
    context['num_cards'] = len(cards)
    context['cards'] = cards
    if cards:
        card_number = request.session.get('card-number', 0)
        context['card'] = cards[card_number]
        request.session['card-id'] = cards[card_number].id
        request.session['card-number'] = card_number
        context['card_number'] = card_number + 1
        ave_difficulty = cards.aggregate(ave=Avg('average_difficulty'))['ave']
        context['average_difficulty'] = ave_difficulty

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
