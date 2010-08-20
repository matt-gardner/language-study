
from memorizing.flashcards.models import Card, CardList

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def index(request):
    context = RequestContext(request)
    context['greeting'] = 'Hello %s!' % request.user.first_name
    context['cardlists'] = request.user.cardlist_set.all()
    return render_to_response('index.html', context)

def create_card_list(request):
    context = RequestContext(request)
    if request.POST:
        form = CardListForm(request.POST)
        cardlist = form.save(commit=False)
        cardlist.user = request.user
        cardlist.save()
        return HttpResponseRedirect('/')
    context['form'] = CardListForm()
    context['submit_label'] = "Create list"
    return render_to_response('add_form.html', context)

class CardListForm(forms.ModelForm):
    class Meta:
        model = CardList
        exclude = ['user']

# vim: et sts=4 sw=4
