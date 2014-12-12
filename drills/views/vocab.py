#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.utils import simplejson

import lxml.html
from datetime import datetime
from random import Random

from scrape import urlopen_with_chrome

from language_study.drills.models import Word
from language_study.drills.models import WordList
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

def get_definition(request, user, listname):
    user = get_object_or_404(User, username=user)
    wordlist = get_object_or_404(WordList, user=user, name=listname)
    word = request.GET['word']
    word = word.lower()
    response = process_word(word, user, wordlist, correct=False)
    return HttpResponse(response);


@transaction.commit_manually
def submit_as_read(request, user, listname):
    user = get_object_or_404(User, username=user)
    wordlist = get_object_or_404(WordList, user=user, name=listname)
    text = request.GET['text']
    text = remove_punctuation(text)
    for word in text.split():
        if '--' in word or '@' in word or '/' in word:
            continue
        if word == '-':
            continue
        if word.isdigit():
            continue
        word = word.lower()
        try:
            process_word(word, user, wordlist, correct=True)
        except UnicodeDecodeError:
            print 'Error processing word', word
            continue
        #except:
            #import traceback
            #tb = traceback.format_exc()
            #if 'database is locked' in tb:
                #raise
            #return HttpResponseServerError("Error!\n" + tb)
    transaction.commit()
    return HttpResponse("Success");


to_remove = ['"', ',', '.', ':', '(', ')', '?', ';', u'»', u'«', '!']
def remove_punctuation(text):
    for char in to_remove:
        text = text.replace(char, '')
    return text


def process_word(word, user, wordlist, correct, always_get_definition=False):
    from subprocess import Popen, PIPE
    proc = Popen(('flookup', 'resources/slovene.bin'), stdin=PIPE, stdout=PIPE)
    proc.stdin.write('%s\n' % word.encode('utf-8'))
    proc.stdin.close()
    analyses = []
    lemmas = set()
    # TODO: make this check for +?, try lower case
    for line in proc.stdout:
        if line.isspace(): continue
        try:
            form, analysis = line.strip().split('\t')
        except ValueError:
            print 'Bad line from stdout:', line
            continue
        analysis = analysis.decode('utf-8')
        if '+?' in analysis:
            continue
        analyses.append(analysis)
        if 'Proper' not in analysis:
            lemmas.add(analysis.split('+', 1)[0])
    proc.stdout.close()
    response = u'Word: ' + word
    response += u'<br><br>Analyses:'
    for analysis in analyses:
        response += u'<br>' + analysis
    response += '<br><br>Definitions:'
    for lemma in lemmas:
        try:
            word = wordlist.word_set.get(word=lemma)
            if always_get_definition:
                definition = get_definition_from_pons(lemma)
                response += u'<br>' + definition.replace('\n', '<br>')
            else:
                response += u'<br>' + word.definition.replace('\n', '<br>')
        except Word.DoesNotExist:
            definition = get_definition_from_pons(lemma)
            response += u'<br>' + definition.replace('\n', '<br>')
            now = datetime.now()
            word = Word(wordlist=wordlist, word=lemma, definition=definition,
                    description=definition, date_entered=now,
                    last_reviewed=now, last_wrong=now, next_review=now)
            word.save()
        word.reviewed(correct=correct)
    return response


def get_definition_from_pons(word):
    print 'Getting definition for word', word
    url = 'http://en.pons.eu/translate'
    params = {'q': word, 'l': 'ensl', 'in': '', 'lf': 'en'}
    html = urlopen_with_chrome(url, params)
    return parse_definition_from_html(html)


def parse_definition_from_html(html):
    # TODO: get more than just the definition, get the morphology too, put it
    # into a more complex object.
    # Also keep the URL, for easy access
    definition = ''
    tree = lxml.html.fromstring(html)
    # The structure of this html is as follows:
    # results
    #  - entry
    #    - rom (this corresponds to a syntactic frame, essentially
    #      - romhead (contains the pronunciation info in an h2 element)
    #      - translations (corresponds to a sense of the word)
    #      - translations
    #        - kne (this is a usage example, with a translation)
    #        - kne
    #        - kne
    #    - rom (perhaps there are several)
    #  - entry (multiple possible entries if there was no exact match for the
    #           query)
    entries = tree.find_class('entry')
    if len(entries) != 1:
        # TODO: decide what to do here; we probably shouldn't just grab all of
        # them.
        return definition
    entry = entries[0]
    for rom in entry.find_class('rom'):
        header = rom.find_class('romhead')[0]
        # TODO: this could use some improvement to collapse runs of whitespace
        # into a single space.
        definition += header.find('h2').text_content().strip() + '\n';
        for translation in rom.find_class('translations'):
            for kne in translation.find_class('kne'):
                source = kne.find_class('source')[0]
                target = kne.find_class('target')[0]
                definition += source.text_content().strip() + ' : '
                definition += target.text_content().strip() + '\n'
    print definition.strip()
    return definition.strip()


# vim: et sw=4 sts=4
