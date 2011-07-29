
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from language_study.drills.models import Conjugation
from language_study.drills.models import IrregularVerbAugmentedStem
from language_study.drills.models import IrregularVerbForm
from language_study.drills.models import IrregularVerbStem
from language_study.drills.models import Verb
from language_study.drills.models import VerbTenseWithNoPassive
from language_study.drills.models import Word
from language_study.drills.models import WordList
from language_study.drills.views.common import base_context
from language_study.drills.views import word_editing_util
from word_editing_util import create_irregular_augment_row
from word_editing_util import create_irregular_verb_form_row
from word_editing_util import create_irregular_stem_row
from word_editing_util import create_form_for_word
from word_editing_util import create_tense_with_no_passive_row
from word_editing_util import MockIrregularForm


# Actual views
##############

def main(request):
    context = base_context(request)
    context['nav_page'] = 'nav_home'
    if not context['logged_in']:
        context['greeting'] = 'Please log in'
        return render_to_response('lists/main.html', context)
    context['greeting'] = 'Hello %s!' % request.user.first_name
    lists = request.user.wordlist_set.all()
    context['wordlists'] = lists
    return render_to_response('lists/main.html', context)


@login_required
def single_list(request, listname):
    context = base_context(request)
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    context['nav_page'] = 'nav_wordlist'
    context['wordlist'] = wordlist
    return render_to_response('lists/single_list.html', context)


@login_required
def single_word(request, listname, word_id):
    if 'delete' in request.GET:
        wordlist = get_object_or_404(WordList, user=request.user, name=listname)
        word = get_object_or_404(Word, pk=word_id, wordlist=wordlist)
        word.delete()
        return HttpResponseRedirect('/%s' % listname)
    if request.POST:
        word = get_object_or_404(Word, pk=word_id)
        wordlist = get_object_or_404(WordList, user=request.user, name=listname)
        if word.wordlist != wordlist:
            raise Http404
        update_word_from_post(word, request.POST)
        return HttpResponseRedirect('/%s/%s?saved=true' % (listname, word_id))
    context = base_context(request)
    context['nav_page'] = 'nav_wordlist'
    word = get_object_or_404(Word, pk=word_id)
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    if word.wordlist != wordlist:
        raise Http404
    if 'saved' in request.GET and request.GET['saved'] == 'true':
        context['message'] = 'Word successfully saved'
    context['wordlist'] = wordlist
    context['header'] = 'Editing word: %s' % word.word
    context['form'] = create_form_for_word(wordlist, word)
    context['submit_label'] = 'Save word'
    return render_to_response('lists/single_word.html', context)


@login_required
def add_word_to_list(request, listname):
    if request.POST:
        wordlist = get_object_or_404(WordList, user=request.user, name=listname)
        word = Word()
        word.wordlist = wordlist
        update_word_from_post(word, request.POST)
        return HttpResponseRedirect('/%s/%s?saved=true' % (listname, word.id))
    context = base_context(request)
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    context['nav_page'] = 'nav_wordlist'
    context['wordlist'] = wordlist
    context['header'] = 'Adding word to list: %s' % wordlist.name
    context['form'] = create_form_for_word(wordlist)
    context['submit_label'] = 'Save word'
    context['adding_word'] = True
    return render_to_response('lists/single_word.html', context)


# Ajax requests
###############

# TODO: fix this
def create_word_list(request, next_url):
    wordlist = WordList(name=request.POST['name'], user=request.user)
    wordlist.save()
    return HttpResponseRedirect(next_url)


# TODO: fix this
def delete_word_list(request, name, next_url):
    wordlist = WordList.objects.get(name=name)
    wordlist.delete()
    return HttpResponseRedirect(next_url)


def add_irregular_form(request, listname, number, word_id=None):
    word = None
    if word_id:
        word = get_object_or_404(Word, pk=word_id)
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    if word and word.wordlist != wordlist:
        raise Http404
    mock_form = MockIrregularForm()
    html = create_irregular_verb_form_row(wordlist.language, mock_form,
            int(number))
    return HttpResponse(html)


def add_irregular_stem(request, listname, number, word_id=None):
    word = None
    if word_id:
        word = get_object_or_404(Word, pk=word_id)
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    if word and word.wordlist != wordlist:
        raise Http404
    mock_form = MockIrregularForm()
    html = create_irregular_stem_row(wordlist.language, mock_form, int(number))
    return HttpResponse(html)


def add_irregular_augment(request, listname, number, word_id=None):
    word = None
    if word_id:
        word = get_object_or_404(Word, pk=word_id)
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    if word and word.wordlist != wordlist:
        raise Http404
    mock_form = MockIrregularForm()
    number = int(number)
    html = create_irregular_augment_row(wordlist.language, mock_form, number)
    return HttpResponse(html)


def add_tense_with_no_passive(request, listname, number, word_id=None):
    word = None
    if word_id:
        word = get_object_or_404(Word, pk=word_id)
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    if word and word.wordlist != wordlist:
        raise Http404
    mock_form = MockIrregularForm()
    number = int(number)
    html = create_tense_with_no_passive_row(wordlist.language, mock_form,
            number)
    return HttpResponse(html)


# Important helper methods
##########################

# TODO: make this a managed transaction, to speed things up; it's slow
def update_word_from_post(word, POST):
    # This is the only field we need to actually set for new words that we
    # don't for editing words, because the other required fields have good
    # defaults
    word.last_reviewed = POST['last_reviewed']
    word.word = POST['word']
    word.definition = POST['definition']
    word.save()

    language = word.wordlist.language
    # Handle verb stuff - sadly, we have a bunch of cases...
    if POST.get('verb', None):
        try:
            # Need to update the verb object with other options
            verb = word.verb
            conj = Conjugation.objects.get(pk=POST['conjugation'])
            verb.conjugation = conj
            verb.no_passive = POST.get('no_passive', False)
            verb.save()
        except Verb.DoesNotExist:
            # Need to create a verb object for this word
            conj = Conjugation.objects.get(pk=POST['conjugation'])
            no_passive = POST.get('no_passive', False)
            verb = Verb(word=word, conjugation=conj, no_passive=no_passive)
            verb.save()
        irregular_forms = []
        irregular_stems = []
        irregular_augments = []
        tenses_with_no_passive = []
        for key in POST:
            if key.startswith("irregular_form_") and key.endswith("_action"):
                irregular_forms.append(key)
            if key.startswith("irregular_stem_") and key.endswith("_action"):
                irregular_stems.append(key)
            if key.startswith("irregular_augment_") and key.endswith("_action"):
                irregular_augments.append(key)
            if key.startswith("no_passive_tense_") and key.endswith("_action"):
                tenses_with_no_passive.append(key)
        save_irregular_forms(language, verb, irregular_forms, POST)
        save_irregular_stems(language, verb, irregular_stems, POST)
        save_irregular_augments(language, verb, irregular_augments, POST)
        save_tenses_with_no_passive(language, verb, tenses_with_no_passive,
                POST)
    else:
        try:
            # Need to delete the verb object
            verb = word.verb
            verb.delete()
        except Verb.DoesNotExist:
            # Word wasn't a verb and still isn't a verb, so do nothing
            pass


def save_irregular_forms(language, verb, irregular_forms, POST):
    for irregular_form in irregular_forms:
        form_number = int(irregular_form.split('_')[-2])
        if POST[irregular_form] == 'delete':
            id = POST['irregular_form_%d_id' % form_number]
            i_form = get_object_or_404(IrregularVerbForm, pk=id, verb=verb)
            i_form.delete()
            continue
        person = POST['irregular_form_%d_person' % form_number]
        number = POST['irregular_form_%d_number' % form_number]
        tense = POST['irregular_form_%d_tense' % form_number]
        mood = POST['irregular_form_%d_mood' % form_number]
        voice = POST['irregular_form_%d_voice' % form_number]
        form = POST['irregular_form_%d_form' % form_number]
        if POST[irregular_form] == 'add':
            i_form = IrregularVerbForm()
        elif POST[irregular_form] == 'save':
            id = POST['irregular_form_%d_id' % form_number]
            i_form = get_object_or_404(IrregularVerbForm, pk=id, verb=verb)
        i_form.verb = verb
        i_form.person = language.person_set.get(pk=person)
        i_form.number = language.number_set.get(pk=number)
        i_form.tense = language.tense_set.get(pk=tense)
        i_form.mood = language.mood_set.get(pk=mood)
        i_form.voice = language.voice_set.get(pk=voice)
        i_form.form = form
        i_form.save()


def save_irregular_stems(language, verb, irregular_stems, POST):
    for irregular_stem in irregular_stems:
        stem_number = int(irregular_stem.split('_')[-2])
        if POST[irregular_stem] == 'delete':
            id = POST['irregular_stem_%d_id' % stem_number]
            i_stem = get_object_or_404(IrregularVerbStem, pk=id, verb=verb)
            i_stem.delete()
            continue
        tense = POST['irregular_stem_%d_tense' % stem_number]
        mood = POST['irregular_stem_%d_mood' % stem_number]
        voice = POST['irregular_stem_%d_voice' % stem_number]
        stem = POST['irregular_stem_%d_stem' % stem_number]
        if POST[irregular_stem] == 'add':
            i_stem = IrregularVerbStem()
        elif POST[irregular_stem] == 'save':
            id = POST['irregular_stem_%d_id' % stem_number]
            i_stem = get_object_or_404(IrregularVerbStem, pk=id, verb=verb)
        i_stem.verb = verb
        i_stem.tense = language.tense_set.get(pk=tense)
        i_stem.mood = language.mood_set.get(pk=mood)
        i_stem.voice = language.voice_set.get(pk=voice)
        i_stem.stem = stem
        i_stem.save()


def save_irregular_augments(language, verb, irregular_augments, POST):
    for irregular_augment in irregular_augments:
        augment_number = int(irregular_augment.split('_')[-2])
        if POST[irregular_augment] == 'delete':
            id = POST['irregular_augment_%d_id' % augment_number]
            i_augment = get_object_or_404(IrregularVerbAugmentedStem, pk=id,
                    verb=verb)
            i_augment.delete()
            continue
        tense = POST['irregular_augment_%d_tense' % augment_number]
        stem = POST['irregular_augment_%d_stem' % augment_number]
        if POST[irregular_augment] == 'add':
            i_augment = IrregularVerbAugmentedStem()
        elif POST[irregular_augment] == 'save':
            id = POST['irregular_augment_%d_id' % augment_number]
            i_augment = get_object_or_404(IrregularVerbAugmentedStem, pk=id,
                    verb=verb)
        i_augment.verb = verb
        i_augment.tense = language.tense_set.get(pk=tense)
        i_augment.stem = stem
        i_augment.save()


def save_tenses_with_no_passive(language, verb, tenses_with_no_passive, POST):
    for no_passive_tense in tenses_with_no_passive:
        tense_number = int(no_passive_tense.split('_')[-2])
        if POST[no_passive_tense] == 'delete':
            id = POST['no_passive_tense_%d_id' % tense_number]
            t = get_object_or_404(VerbTenseWithNoPassive, pk=id,
                    verb=verb)
            t.delete()
            continue
        tense = POST['no_passive_tense_%d_tense' % tense_number]
        if POST[no_passive_tense] == 'add':
            t = VerbTenseWithNoPassive()
        elif POST[no_passive_tense] == 'save':
            id = POST['no_passive_tense_%d_id' % tense_number]
            t = get_object_or_404(VerbTenseWithNoPassive, pk=id, verb=verb)
        t.verb = verb
        t.tense = language.tense_set.get(pk=tense)
        t.save()


# vim: et sw=4 sts=4
