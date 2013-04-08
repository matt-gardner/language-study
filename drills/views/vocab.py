#!/usr/bin/env python

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

from BeautifulSoup import BeautifulSoup
from datetime import datetime
from random import Random

from scrape import urlopen_with_chrome

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
    from subprocess import Popen, PIPE
    word = request.GET['word']
    proc = Popen(('flookup', 'resources/slovene.bin'), stdin=PIPE, stdout=PIPE)
    proc.stdin.write('%s\n' % word.encode('utf-8'))
    proc.stdin.close()
    analyses = []
    lemmas = set()
    for line in proc.stdout:
        if line.isspace(): continue
        try:
            form, analysis = line.strip().split('\t')
        except ValueError:
            print 'Bad line from stdout:', line
        analysis = analysis.decode('utf-8')
        analyses.append(analysis)
        lemmas.add(analysis.split('+', 1)[0])
    proc.stdout.close()
    response = u'Word: ' + word
    response += u'<br><br>Analyses:'
    for analysis in analyses:
        response += u'<br>' + analysis
    response += '<br><br>Definitions:'
    for lemma in lemmas:
        definition = get_definition_from_pons(lemma)
        response += u'<br>' + definition.replace('\n', '<br>')
    return HttpResponse(response);


def get_definition_from_pons(word):
    definition = ''
    url = 'http://en.pons.eu/dict/search/results/?q=%s&l=ensl&in=&lf=en' % (
            word)
    html = urlopen_with_chrome(url.encode('utf-8'))
    soup = BeautifulSoup(html)
    senses = []
    for sense in soup.findAll('span', attrs={'class':'sense'}):
        if sense.parent.name == 'th':
            table = sense.parent.parent.parent.parent
        else:
            table = sense.parent.parent.parent
        senses.append((sense, table))
    for sense, table in senses:
        definition += ''.join(sense.parent.findAll(text=True)).strip() + '\n'
        for target in table.findAll('td', attrs={'class':'target'}):
            source = target.findPreviousSibling('td', attrs={'class': 'source'})
            definition += ''.join(source.findAll(text=True)).strip() + ' : '
            definition += ''.join(target.findAll(text=True)).strip() + '\n'
        definition += '\n'
    if not senses:
        for target in soup.findAll('td', attrs={'class':'target'}):
            source = target.findPreviousSibling('td', attrs={'class': 'source'})
            definition += ''.join(source.findAll(text=True)).strip() + ' : '
            definition += ''.join(target.findAll(text=True)).strip() + '\n'
    return definition


# vim: et sw=4 sts=4
