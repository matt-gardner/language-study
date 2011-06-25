
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from language_study.drills.models import Conjugation
from language_study.drills.models import IrregularVerbForm
from language_study.drills.models import Verb
from language_study.drills.models import Word
from language_study.drills.models import WordList
from language_study.drills.views.common import base_context


# Actual views
##############

def main(request):
    context = base_context(request)
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
    context['wordlist'] = wordlist
    return render_to_response('lists/single_list.html', context)


@login_required
def single_word(request, listname, word_id):
    if 'delete' in request.GET:
        word = get_object_or_404(Word, pk=word_id)
        wordlist = get_object_or_404(WordList, user=request.user, name=listname)
        if word.wordlist != wordlist:
            raise Http404
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
    context['wordlist'] = wordlist
    context['header'] = 'Adding word to list: %s' % wordlist.name
    context['form'] = create_form_for_word(wordlist)
    context['submit_label'] = 'Save word'
    context['adding_word'] = True
    return render_to_response('lists/single_word.html', context)


# Ajax requests
###############

def add_irregular_form(request, listname, number, word_id=None):
    word = None
    if word_id:
        word = get_object_or_404(Word, pk=word_id)
    wordlist = get_object_or_404(WordList, user=request.user, name=listname)
    if word and word.wordlist != wordlist:
        raise Http404
    mock_form = MockIrregularVerbForm()
    html = create_irregular_form_row(wordlist.language, mock_form, int(number))
    return HttpResponse(html)


# Important helper methods
##########################

def update_word_from_post(word, POST):
    # This is the only field we need to actually set for new words that we
    # don't for editing words, because the other required fields have good
    # defaults
    word.last_reviewed = POST['last_reviewed']
    word.word = POST['word']
    word.definition = POST['definition']
    word.save()

    # Handle verb stuff - sadly, we have a bunch of cases...
    if POST.get('verb', None):
        try:
            # Need to update the verb object with other options
            verb = word.verb
        except Verb.DoesNotExist:
            # Need to create a verb object for this word
            conj = Conjugation.objects.get(pk=POST['conjugation'])
            verb = Verb(word=word, conjugation=conj)
            verb.save()
    else:
        try:
            # Need to delete the verb object
            verb = word.verb
            verb.delete()
        except Verb.DoesNotExist:
            # Word wasn't a verb and still isn't a verb, so do nothing
            pass


# Form building methods and classes
###################################

# I wanted to do more complicated things than Django's built-in form
# functionality would let me do, so I have a lot that I'm writing here, and
# some javascript to go with it.

def create_form_for_word(wordlist, word=None):
    word_form = WordForm(wordlist, word).as_table()
    verb_form = ''
    verb_form += irregular_forms_form(word)
    return word_form + verb_form


def irregular_forms_form(word):
    if_form = '\n\n<tr><th><label>Irregular Forms:</label></th>\n'
    if_form += '<td>\n<table class=verb-option>\n'
    irregular_forms = []
    if word:
        language = word.wordlist.language
        try:
            irregular_forms =  word.verb.irregularverbform_set.all()
        except Verb.DoesNotExist:
            pass
    for i, form in enumerate(irregular_forms):
        if_form += create_irregular_form_row(language, form, i)
    if_form += '<tr><td><span class=add_irregular_form>Add</span></td></tr>\n'
    if_form += '</table></td></tr>'
    return if_form


def create_irregular_form_row(language, form, i):
    html = '<tr>\n'
    html += '<td>'
    html += make_select(language.person_set.all(),
            'irregular_form_%d_person' % i, form.person)
    html += '</td>\n'
    html += '<td>'
    html += make_select(language.number_set.all(),
            'irregular_form_%d_number' % i, form.number)
    html += '</td>\n'
    html += '<td>'
    html += make_select(language.tense_set.all(),
            'irregular_form_%d_tense' % i, form.tense)
    html += '</td>\n'
    html += '<td>'
    html += make_select(language.mood_set.all(),
            'irregular_form_%d_mood' % i, form.mood)
    html += '</td>\n'
    html += '<td>'
    html += make_select(language.voice_set.all(),
            'irregular_form_%d_voice' % i, form.voice)
    html += '</td>\n'
    html += '<td><input type=text name="irregular_form_%d_form"' % i
    html += 'value="' + form.form + '" /></td>\n'
    html += '<td><span class="delete_irregular_form">X</span>'
    html += '<input type="hidden" name="irregular_form_%d_action" ' % i
    if isinstance(form, MockIrregularVerbForm):
        html += 'value="add" /></td>\n'
    else:
        html += 'value="save" /></td>\n'
    html += '</tr>\n\n'
    return html


def make_select(options, name, selected=None):
    select = '<select name="' + name + '">\n'
    for option in options:
        select += '<option value="%d"' % option.id
        if option == selected:
            select += ' selected="selected"'
        select += '>' + option.name + '</option>\n'
    select += '</select>\n'
    return select


class MockIrregularVerbForm(object):
    def __init__(self):
        self.person = None
        self.number = None
        self.tense = None
        self.mood = None
        self.voice = None
        self.form = ''


class WordForm(forms.Form):
    wordlist_name = forms.CharField(label='Wordlist',
            widget=forms.TextInput({'readonly': True, 'size': 50}))
    word = forms.CharField(
            widget=forms.TextInput({'size': 100}))
    definition = forms.CharField(
            widget=forms.TextInput({'size': 100}))
    date_entered = forms.CharField(
            widget=forms.TextInput({'readonly': True, 'size': 50}))
    last_reviewed = forms.CharField(
            widget=forms.TextInput({'readonly': True, 'size': 50}))
    average_difficulty = forms.CharField(
            widget=forms.TextInput({'readonly': True, 'size': 5}))
    review_count = forms.CharField(
            widget=forms.TextInput({'readonly': True, 'size': 5}))
    verb = forms.BooleanField()
    conjugation = forms.ModelChoiceField(None, empty_label=None,
            widget=forms.Select({'class': 'verb-option'}))
    
    def __init__(self, wordlist, word=None, *args, **kwds):
        super(WordForm, self).__init__(*args, **kwds)
        self.fields['wordlist_name'].initial = wordlist.name
        language = wordlist.language
        self.fields['conjugation'].queryset = language.conjugation_set.all()
        if word:
            self.init_from_word(word)
        else:
            self.default_init()

    def init_from_word(self, word):
        self.fields['word'].initial = word.word
        self.fields['definition'].initial = word.definition
        self.fields['date_entered'].initial = word.date_entered
        self.fields['last_reviewed'].initial = word.last_reviewed
        self.fields['average_difficulty'].initial = word.average_difficulty
        self.fields['review_count'].initial = word.review_count
        try:
            verb = word.verb
            self.fields['verb'].initial = True
            self.fields['conjugation'].initial = verb.conjugation
        except Verb.DoesNotExist:
            pass

    def default_init(self):
        now = datetime.now()
        hard = Word.DIFFICULTY_SCORES['hard']
        self.fields['date_entered'].initial = now
        self.fields['last_reviewed'].initial = now
        self.fields['average_difficulty'].initial = hard
        self.fields['review_count'].initial = 0


# vim: et sw=4 sts=4
