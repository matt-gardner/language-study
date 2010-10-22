#!/usr/bin/env python

from django import forms
from django.db.models import Avg
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.utils import simplejson

from datetime import datetime
from random import shuffle

from memorizing.flashcards.models import Card, CardList, Tag
from memorizing.flashcards.filters import filter_cards

# Card list stuff
#################

def create_card_list(request, next_url):
    cardlist = CardList(name=request.POST['name'], user=request.user)
    cardlist.save()
    request.session['cardlist-name'] = request.POST['name']
    request.session['card-number'] = 0
    request.session['cards'] = []
    return HttpResponseRedirect(next_url)


def delete_card_list(request, name, next_url):
    cardlist = CardList.objects.get(name=name)
    cardlist.delete()
    del request.session['cardlist-name']
    request.session['card-number'] = 0
    return HttpResponseRedirect(next_url)


def get_card_list(request, name):
    request.session['cardlist-name'] = name
    request.session['card-number'] = 0
    cardlist = request.user.cardlist_set.get(name=name)
    cards = cardlist.card_set.all()
    request.session['cards'] = [AjaxWord(c) for c in cards]
    return return_card_from_session(request)


def add_card_to_list(request, next_url):
    word = request.POST['word']
    request.session['errors'] = []
    if not word:
        request.session['errors'].append("You didn't enter a word!")

    text = request.POST['text']
    if not text:
        request.session['errors'].append("You didn't enter any text!")

    list_name = request.session.get('cardlist-name', None)
    if not list_name:
        request.session['errors'].append("You didn't select a card list!")

    if request.session['errors']:
        return HttpResponseRedirect(next_url)

    del request.session['errors']
    now = datetime.now()
    cardlist = CardList.objects.get(name=list_name)
    card = Card(list=cardlist, word=word, text=text, last_reviewed=now,
            date_entered=now)
    card.save()
    cardlist.save()
    return HttpResponseRedirect(next_url)


def reorder_card_list(request, ordering):
    cardlist_name = request.session['cardlist-name']
    cardlist = request.user.cardlist_set.get(name=cardlist_name)
    if ordering == 'random':
        shuffle(request.session['cards'])
        request.session['card-number'] = 0
        return return_card_from_session(request)
    filters = request.session.get('filters', [])
    cards, _ = filter_cards(cardlist.card_set, filters)
    if ordering == 'alphabetical':
        cards = cards.order_by('word')
    elif ordering == 'last_reviewed':
        cards = cards.order_by('last_reviewed')
    elif ordering == 'least_reviewed':
        cards = cards.order_by('review_count')
    elif ordering == 'date_entered':
        cards = cards.order_by('date_entered')
    elif ordering == 'difficulty':
        cards = cards.order_by('-average_difficulty')
    request.session['cards'] = [AjaxWord(c) for c in cards]
    request.session['card-number'] = 0
    return return_card_from_session(request)


# Tag stuff
###########

def add_tag(request, next_url):
    name = request.POST['name']
    request.session['errors'] = []
    list_name = request.session.get('cardlist-name', None)
    if not list_name:
        request.session['errors'].append("You didn't select a card list!")

    if request.session['errors']:
        return HttpResponseRedirect(next_url)

    del request.session['errors']
    cardlist = CardList.objects.get(name=list_name)
    tag = Tag(name=name, list=cardlist)
    tag.save()
    return HttpResponseRedirect(next_url)


def add_tag_to_card(request, tag_name):
    list_name = request.session.get('cardlist-name', None)
    cardlist = CardList.objects.get(name=list_name)
    tag = cardlist.tag_set.get(name=tag_name)
    card = cardlist.card_set.get(pk=request.session['card-id'])
    card.tags.add(tag)
    ret_val = dict()
    ret_val['tags'] = ', '.join(t.name for t in card.tags.all())
    return HttpResponse(simplejson.dumps(ret_val))


# The general "return a card" AJAX function
###########################################

def return_card_from_session(request):
    ret_val = dict()
    cards = request.session['cards']
    num_cards = len(cards)
    print num_cards
    current_card = request.session['card-number']
    current_card %= num_cards
    request.session['card-number'] = current_card
    request.session['card-id'] = cards[current_card].id
    cards[current_card].get_tags()
    ret_val['card'] = vars(cards[current_card])
    ret_val['card_number'] = current_card + 1
    ret_val['num_cards'] = num_cards
    ret_val['difficulty'] = sum([c.difficulty for c in cards])/len(cards)
    return HttpResponse(simplejson.dumps(ret_val))


# Other general methods
#######################

def review_styles():
    styles = []
    styles.append(ReviewStyle('Review All Words', '/all-words/'))
    styles.append(ReviewStyle('By Difficulty', '/difficulty/'))
    styles.append(ReviewStyle('Daily Review', '/daily/'))
    return styles


def next_card(request, difficulty=None):
    if difficulty:
        card = update_card_difficulty_from_session(request, difficulty)
        ajaxcard = request.session['cards'][request.session['card-number']]
        ajaxcard.difficulty = card.average_difficulty
        ajaxcard.review_count = card.review_count
    request.session['card-number'] += 1
    return return_card_from_session(request)


def prev_card(request):
    request.session['card-number'] -= 1
    return return_card_from_session(request)


def update_card_difficulty_from_session(request, difficulty):
    cardlist_name = request.session['cardlist-name']
    cardlist = request.user.cardlist_set.get(name=cardlist_name)
    card = cardlist.card_set.get(pk=request.session['card-id'])
    card.update_difficulty(Card.DIFFICULTY_SCORES[difficulty])
    card.reviewed()
    return card


def base_review_context(request):
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

    list_name = request.session.get('cardlist-name', '')
    if list_name:
        cardlist = lists.get(name=list_name)
    else:
        cardlist = lists[0]
        request.session['cardlist-name'] = cardlist.name

    context['cardlist'] = cardlist

    context['tags'] = cardlist.tag_set.all()
    cards = cardlist.card_set
    filters = request.session.get('filters', [])
    cards, filter_form = filter_cards(cards, filters)
    context['filter'] = filter_form
    context['num_cards'] = len(cards)
    if cards:
        ave_difficulty = cards.aggregate(ave=Avg('average_difficulty'))['ave']
        context['average_difficulty'] = ave_difficulty
    return context, cards


# Classes that help out with things
###################################

class ReviewStyle(object):
    def __init__(self, name, link):
        self.name = name
        self.link = link


class AjaxWord(object):
    def __init__(self, card):
        self.word = card.word
        self.text = card.text
        self.difficulty = card.average_difficulty
        self.review_count = card.review_count
        self.id = card.id
        self.tags = None

    def get_tags(self):
        card = Card.objects.get(pk=self.id)
        self.tags = ', '.join(t.name for t in card.tags.all())
        if not self.tags:
            self.tags = 'This card has no tags'


# vim: et sts=4 sw=4
