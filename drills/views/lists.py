
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from language_study.drills.models import WordList

@login_required
def main(request):
    context = RequestContext(request)
    context['greeting'] = 'Hello %s!' % request.user.first_name
    lists = request.user.wordlist_set.all()
    context['wordlists'] = lists
    return render_to_response('lists/main.html', context)


def single_list(request, listname):
    context = RequestContext(request)
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    context['wordlist'] = wordlist
    return render_to_response('lists/single_list.html', context)


# vim: et sw=4 sts=4
