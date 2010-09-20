#!/usr/bin/env python

from memorizing.flashcards.models import Card, CardList, Tag

from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson

from datetime import datetime
from random import shuffle

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
    elif ordering == 'alphabetical':
        cards = cardlist.card_set.order_by('word')
    elif ordering == 'last_reviewed':
        cards = cardlist.card_set.order_by('last_reviewed')
    elif ordering == 'least_reviewed':
        cards = cardlist.card_set.order_by('review_count')
    elif ordering == 'date_entered':
        cards = cardlist.card_set.order_by('date_entered')
    elif ordering == 'difficulty':
        cards = cardlist.card_set.order_by('-average_difficulty')
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
        self.tags = ', '.join(t.name for t in card.tags.all())
        if not self.tags:
            self.tags = 'This card has no tags'


class AjaxTag(object):
    def __init__(self, tag):
        self.name = tag.name


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['word', 'text']

# vim: et sts=4 sw=4
