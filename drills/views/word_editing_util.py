#!/usr/bin/env python

from datetime import datetime

from django import forms

from language_study.drills.models import Verb
from language_study.drills.models import Word

# I wanted to do more complicated things than Django's built-in form
# functionality would let me do, so I have a lot that I'm writing here, and
# some javascript to go with it.

def create_form_for_word(wordlist, word=None):
    word_form = WordForm(wordlist, word).as_table()
    verb_form = ''
    verb_form += irregular_forms_form(word)
    verb_form += irregular_stems_form(word)
    verb_form += irregular_augments_form(word)
    verb_form += tenses_with_no_passive_form(word)
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
    if isinstance(form, MockIrregularForm):
        html += 'value="add" /></td>\n'
    else:
        html += 'value="save" />\n'
        html += '<input type="hidden" name="irregular_form_%d_id" ' % i
        html += 'value="%d" />\n' % form.id
        html += '</td>\n'
    html += '</tr>\n\n'
    return html


def irregular_stems_form(word):
    is_form = '\n\n<tr><th><label>Irregular Stems:</label></th>\n'
    is_form += '<td>\n<table class=verb-option>\n'
    irregular_stems = []
    if word:
        language = word.wordlist.language
        try:
            irregular_stems =  word.verb.irregularverbstem_set.all()
        except Verb.DoesNotExist:
            pass
    for i, stem in enumerate(irregular_stems):
        is_form += create_irregular_stem_row(language, stem, i)
    is_form += '<tr><td><span class=add_irregular_stem>Add</span></td></tr>\n'
    is_form += '</table></td></tr>'
    return is_form


def create_irregular_stem_row(language, stem, i):
    html = '<tr>\n'
    html += '<td>'
    html += make_select(language.tense_set.all(),
            'irregular_stem_%d_tense' % i, stem.tense)
    html += '</td>\n'
    html += '<td>'
    html += make_select(language.mood_set.all(),
            'irregular_stem_%d_mood' % i, stem.mood)
    html += '</td>\n'
    html += '<td>'
    html += make_select(language.voice_set.all(),
            'irregular_stem_%d_voice' % i, stem.voice)
    html += '</td>\n'
    html += '<td><input type=text name="irregular_stem_%d_stem"' % i
    html += 'value="' + stem.stem + '" /></td>\n'
    html += '<td><span class="delete_irregular_form">X</span>'
    html += '<input type="hidden" name="irregular_stem_%d_action" ' % i
    if isinstance(stem, MockIrregularForm):
        html += 'value="add" /></td>\n'
    else:
        html += 'value="save" />\n'
        html += '<input type="hidden" name="irregular_stem_%d_id" ' % i
        html += 'value="%d" />\n' % stem.id
        html += '</td>\n'
    html += '</tr>\n\n'
    return html


def irregular_augments_form(word):
    ia_form = '\n\n<tr><th><label>Irregular Augments:</label></th>\n'
    ia_form += '<td>\n<table class=verb-option>\n'
    irregular_augments = []
    if word:
        language = word.wordlist.language
        try:
            irregular_augments =  word.verb.irregularverbaugmentedstem_set.all()
        except Verb.DoesNotExist:
            pass
    for i, augment in enumerate(irregular_augments):
        ia_form += create_irregular_augment_row(language, augment, i)
    ia_form += '<tr><td><span class=add_irregular_augment>Add</span></td></tr>'
    ia_form += '\n</table></td></tr>'
    return ia_form


def create_irregular_augment_row(language, augment, i):
    html = '<tr>\n'
    html += '<td>'
    html += make_select(language.tense_set.all(),
            'irregular_augment_%d_tense' % i, augment.tense)
    html += '</td>\n'
    html += '<td><input type=text name="irregular_augment_%d_stem"' % i
    html += 'value="' + augment.stem + '" /></td>\n'
    html += '<td><span class="delete_irregular_form">X</span>'
    html += '<input type="hidden" name="irregular_augment_%d_action" ' % i
    if isinstance(augment, MockIrregularForm):
        html += 'value="add" /></td>\n'
    else:
        html += 'value="save" />\n'
        html += '<input type="hidden" name="irregular_augment_%d_id" ' % i
        html += 'value="%d" />\n' % augment.id
        html += '</td>\n'
    html += '</tr>\n\n'
    return html


def tenses_with_no_passive_form(word):
    tnp_form = '\n\n<tr><th><label>Tenses with no Passive:</label></th>\n'
    tnp_form += '<td>\n<table class=verb-option>\n'
    tenses_with_no_passive = []
    if word:
        language = word.wordlist.language
        try:
            tenses_with_no_passive =  word.verb.verbtensewithnopassive_set.all()
        except Verb.DoesNotExist:
            pass
    for i, tense in enumerate(tenses_with_no_passive):
        tnp_form += create_tense_with_no_passive_row(language, tense, i)
    tnp_form += '<tr><td><span class=add_tense_with_no_passive>Add</span></td>'
    tnp_form += '</tr>\n</table></td></tr>'
    return tnp_form


def create_tense_with_no_passive_row(language, tense, i):
    html = '<tr>\n'
    html += '<td>'
    html += make_select(language.tense_set.all(),
            'no_passive_tense_%d_tense' % i, tense.tense)
    html += '</td>\n'
    html += '<td><span class="delete_irregular_form">X</span>'
    html += '<input type="hidden" name="no_passive_tense_%d_action" ' % i
    if isinstance(tense, MockIrregularForm):
        html += 'value="add" /></td>\n'
    else:
        html += 'value="save" />\n'
        html += '<input type="hidden" name="no_passive_tense_%d_id" ' % i
        html += 'value="%d" />\n' % tense.id
        html += '</td>\n'
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


class MockIrregularForm(object):
    def __init__(self):
        self.person = None
        self.number = None
        self.tense = None
        self.mood = None
        self.voice = None
        self.form = ''
        self.stem = ''


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
