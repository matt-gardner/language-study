
from memorizing.flashcards.models import Card, CardList

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from datetime import datetime
from random import shuffle


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

    list_name = request.session.get('cardlist-name', None)
    if list_name:
        cardlist = lists.get(name=list_name)
    elif lists:
        cardlist = lists[0]
        request.session['cardlist-name'] = cardlist.name
    else:
        cardlist = None

    if cardlist:
        context['cardlist'] = cardlist
        context['add_card_form'] = CardForm()
        cards = cardlist.card_set.all()
        request.session['cards'] = [AjaxWord(c.word, c.text) for c in cards]
        context['num_cards'] = len(cards)
        context['cards'] = cards
        if cards:
            card_number = request.session.get('card-number', 0)
            context['card'] = cards[card_number]
            context['card_number'] = card_number + 1

    return render_to_response('index.html', context)


def create_card_list(request):
    cardlist = CardList(name=request.POST['name'], user=request.user)
    cardlist.save()
    request.session['cardlist-name'] = request.POST['name']
    request.session['card-number'] = 0
    request.session['cards'] = []
    return HttpResponseRedirect('/')


def delete_card_list(request, name):
    cardlist = CardList.objects.get(name=name)
    cardlist.delete()
    del request.session['cardlist-name']
    request.session['card-number'] = 0
    return HttpResponseRedirect('/')


def randomize_card_list(request):
    shuffle(request.session['cards'])
    request.session['card-number'] = 0
    return return_card_from_session(request)


def unrandomize_card_list(request):
    cardlist_name = request.session['cardlist-name']
    cardlist = request.user.cardlist_set.get(name=cardlist_name)
    cards = cardlist.card_set.all()
    request.session['cards'] = [AjaxWord(c.word, c.text) for c in cards]
    request.session['card-number'] = 0
    return return_card_from_session(request)


def add_card_to_list(request):
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
        return HttpResponseRedirect('/')

    del request.session['errors']
    now = datetime.now()
    cardlist = CardList.objects.get(name=list_name)
    card = Card(list=cardlist, word=word, text=text, last_reviewed=now,
            date_entered=now)
    card.save()
    return HttpResponseRedirect('/')


def get_card_list(request, name):
    request.session['cardlist-name'] = name
    request.session['card-number'] = 0
    cardlist = request.user.cardlist_set.get(name=name)
    cards = cardlist.card_set.all()
    request.session['cards'] = [AjaxWord(c.word, c.text) for c in cards]
    return return_card_from_session(request)


def next_card(request, difficulty=None):
    request.session['card-number'] += 1
    return return_card_from_session(request)


def prev_card(request, difficulty=None):
    request.session['card-number'] -= 1
    return return_card_from_session(request)


def return_card_from_session(request):
    ret_val = dict()
    cards = request.session['cards']
    num_cards = len(cards)
    current_card = request.session['card-number']
    current_card %= num_cards
    request.session['card-number'] = current_card
    print cards[current_card]
    ret_val['card'] = vars(cards[current_card])
    ret_val['card_number'] = current_card + 1
    ret_val['num_cards'] = num_cards
    return HttpResponse(simplejson.dumps(ret_val))

class AjaxWord(object):
    def __init__(self, word, text):
        self.word = word
        self.text = text


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['word', 'text']

# vim: et sts=4 sw=4
