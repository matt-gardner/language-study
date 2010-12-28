#!/usr/bin/env python

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.http import HttpResponse

from datetime import datetime, date
from language_study.drills.models import Tag

class FilterForm(forms.Form):
    def __init__(self, possible_filters, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.filters = []
        self.fields['f'] = forms.ChoiceField(possible_filters)
        self.fields['f'].widget.attrs['onchange'] = 'add_new_filter()'

    def add_filter(self, filter):
        self.filters.append(filter)

    def add_filter_form(self):
        ret_val = '<td>Add a filter by</td>'
        f = forms.forms.BoundField(self, self.fields['f'], 'filter')
        ret_val += '<td>' + f.as_widget() + '</td>'
        return ret_val

    def __unicode__(self):
        ret_val = ''
        if self.filters:
            for filter in self.filters:
                filter.remake_form()
                ret_val += '<tr>%s</tr>' % filter.form()
        ret_val += '<tr>%s</tr>' % self.add_filter_form()
        return ret_val


def possible_word_filters():
    possible_filters = [('None', '-------')]
    possible_filters.append(('tag', 'Tag'))
    possible_filters.append(('difficulty', 'Difficulty'))
    possible_filters.append(('startswith', 'Word starts With'))
    possible_filters.append(('contains', 'Word contains'))
    possible_filters.append(('defstartswith', 'Text starts With'))
    possible_filters.append(('defcontains', 'Text contains'))
    possible_filters.append(('lastreviewed', 'Last Reviewed'))
    return possible_filters


def get_word_filter_by_name(name):
    if name == 'tag':
        return WordFilterByTag
    if name == 'difficulty':
        return WordFilterByDifficulty
    if name == 'startswith':
        return WordFilterByStartsWith
    if name == 'contains':
        return WordFilterByContains
    if name == 'defstartswith':
        return WordFilterByDefStartsWith
    if name == 'defcontains':
        return WordFilterByDefContains
    if name == 'lastreviewed':
        return WordFilterByLastReviewed
    raise ValueError('There is no word filter with the name %s' % name)


def filter_words(words, filters):
    filter_form = FilterForm(possible_word_filters())
    id = 0
    for filter in filters:
        filter.id = id
        id += 1
        filter_form.add_filter(filter)
        words = filter.apply(words)
    return words.all(), filter_form


def add_filter(request, name):
    filters = request.session.get('filters', [])
    filter_form = FilterForm(possible_word_filters())
    id = 0
    for filter in filters:
        filter.id = id
        filter_form.add_filter(filter)
        id += 1
    wordlist_name = request.session['wordlist-name']
    wordlist = request.user.wordlist_set.get(name=wordlist_name)
    new_filter = get_word_filter_by_name(name)(id, wordlist)
    filter_form.add_filter(new_filter)
    filters.append(new_filter)
    request.session['filters'] = filters
    return HttpResponse(filter_form.__unicode__())


def remove_filter(request, id):
    request.session['filters'].pop(int(id))
    request.session.modified = True
    filter_form = FilterForm(possible_word_filters())
    id = 0
    for filter in request.session.get('filters', []):
        filter.id = id
        filter_form.add_filter(filter)
        id += 1
    return HttpResponse(filter_form.__unicode__())


def update_tag_filter(request, id, tag):
    filter = request.session['filters'][int(id)]
    if tag == 'None':
        filter.current_tag = None
    else:
        filter.current_tag = tag
    filter.remake_form()
    request.session.modified = True
    filter_form = FilterForm(possible_word_filters())
    id = 0
    for filter in request.session.get('filters', []):
        filter.id = id
        filter_form.add_filter(filter)
        id += 1
    return HttpResponse(filter_form.__unicode__())


def update_difficulty_filter(request, id, comp, value):
    filter = request.session['filters'][int(id)]
    filter.current_comparator = comp
    filter.current_value = value
    filter.remake_form()
    request.session.modified = True
    filter_form = FilterForm(possible_word_filters())
    id = 0
    for filter in request.session.get('filters', []):
        filter.id = id
        filter_form.add_filter(filter)
        id += 1
    return HttpResponse(filter_form.__unicode__())


def update_string_filter(request, id, string):
    filter = request.session['filters'][int(id)]
    filter.current_string = string
    filter.remake_form()
    request.session.modified = True
    filter_form = FilterForm(possible_word_filters())
    id = 0
    for filter in request.session.get('filters', []):
        filter.id = id
        filter_form.add_filter(filter)
        id += 1
    return HttpResponse(filter_form.__unicode__())


def update_date_filter(request, id, comp, year, month, day):
    filter = request.session['filters'][int(id)]
    filter.comparator = comp
    filter.current_year = int(year)
    filter.current_month = int(month)
    filter.current_day = int(day)
    filter.remake_form()
    request.session.modified = True
    filter_form = FilterForm(possible_word_filters())
    id = 0
    for filter in request.session.get('filters', []):
        filter.id = id
        filter_form.add_filter(filter)
        id += 1
    return HttpResponse(filter_form.__unicode__())


# Filter Classes
################

#TODO(matt): make a WordFilterByValue, or something, that these subclass

# Value Filters
################

class WordFilterByTag(object):
    def __init__(self, id, wordlist):
        self.id = id
        self.wordlist = wordlist
        self.current_tag = None
        self.remake_form()

    def apply(self, word_set):
        if not self.current_tag:
            return word_set
        tag = self.wordlist.tag_set.get(name=self.current_tag)
        return word_set.filter(tags=tag)

    def remake_form(self):
        if self.current_tag:
            tag = self.current_tag
        else:
            tag = 'None'
        self._form = TagFilterForm(self.id, tag, self.wordlist)

    def form(self):
        # This BoundField business is a bit of a hack to just get the part of
        # the HTML that I want.  I could build the HTML for it myself, but this
        # was a little easier.
        ret_val = '<td>Tag:'
        tag = forms.forms.BoundField(self._form, self._form.fields['tag'],
                'tag_filter_%d' % self.id)
        ret_val += '</td><td>'
        ret_val += tag.as_widget()
        ret_val += '</td><td class="remove" '
        ret_val += 'onclick="remove_filter(%d)">X</td>' % self.id
        return ret_val


class TagFilterForm(forms.Form):
    def __init__(self, id, tag, wordlist, *args, **kwargs):
        super(TagFilterForm, self).__init__(*args, **kwargs)
        tag_choices = [('None', 'All')]
        tags = wordlist.tag_set.all()
        for t in tags:
            tag_choices.append((t.name, t.name))
        self.fields['tag'] = forms.ChoiceField(tag_choices, label='Tag',
                initial=tag)
        self.fields['tag'].widget.attrs['onchange'] = \
                'update_tag_filter(%d)' % id


class WordFilterByDifficulty(object):
    def __init__(self, id, wordlist):
        self.id = id
        self.wordlist = wordlist
        self.current_comparator = 'gt'
        self.current_value = None
        self.remake_form()

    def apply(self, word_set):
        if not self.current_value:
            return word_set
        if self.current_comparator == 'gt':
            return word_set.filter(
                    average_difficulty__gt=self.current_value)
        if self.current_comparator == 'lt':
            return word_set.filter(
                    average_difficulty__lt=self.current_value)
        raise ValueError('Current comparator is not supported: %s' %
                self.current_comparator)

    def remake_form(self):
        comparator = self.current_comparator
        if self.current_value:
            value = self.current_value
        else:
            value = 'None'
        self._form = DifficultyFilterForm(self.id, comparator, value)
        if not self.current_value:
            self.current_value = self._form.value_choices[0][0]

    def form(self):
        # This BoundField business is a bit of a hack to just get the part of
        # the HTML that I want.  I could build the HTML for it myself, but this
        # was a little easier.
        ret_val = '<td>Difficulty:</td><td>'
        comp = forms.forms.BoundField(self._form, self._form.fields['comp'],
                'difficulty_filter_comp_%d' % self.id)
        ret_val += comp.as_widget()
        val = forms.forms.BoundField(self._form, self._form.fields['value'],
                'difficulty_filter_value_%d' % self.id)
        ret_val += val.as_widget()
        ret_val += '</td><td class="remove" '
        ret_val += 'onclick="remove_filter(%d)">X</td>' % self.id
        return ret_val


class DifficultyFilterForm(forms.Form):
    def __init__(self, id, comparator, value, *args, **kwargs):
        super(DifficultyFilterForm, self).__init__(*args, **kwargs)
        comparator_choices = [('gt', 'Greater than'), ('lt', 'Less than')]
        self.fields['comp'] = forms.ChoiceField(comparator_choices,
                label='', initial=comparator)
        self.fields['comp'].widget.attrs['onchange'] = \
                'update_difficulty_filter(%d)' % id
        self.value_choices = [(i*5, i*5) for i in range(9)]
        self.fields['value'] = forms.ChoiceField(self.value_choices,
                label='', initial=value)
        self.fields['value'].widget.attrs['onchange'] = \
                'update_difficulty_filter(%d)' % id


# String Filters
################

class WordFilterByString(object):
    def __init__(self, id, wordlist):
        self.id = id
        self.wordlist = wordlist
        self.current_string = None
        self.label = ''

    def apply(self, word_set):
        raise NotImplementedError()

    def remake_form(self):
        self._form = StringFilterForm(self.id, self.current_string,
                self.wordlist)

    def form(self):
        # This BoundField business is a bit of a hack to just get the part of
        # the HTML that I want.  I could build the HTML for it myself, but this
        # was a little easier.
        ret_val = '<td>%s:' % self.label
        string = forms.forms.BoundField(self._form, self._form.fields['string'],
                'string_filter_%d' % self.id)
        ret_val += '</td><td>'
        ret_val += string.as_widget()
        ret_val += '</td><td class="remove" '
        ret_val += 'onclick="remove_filter(%d)">X</td>' % self.id
        return ret_val


class WordFilterByStartsWith(WordFilterByString):
    def __init__(self, id, wordlist):
        super(WordFilterByStartsWith, self).__init__(id, wordlist)
        self.label = 'Word starts with'
        self.remake_form()

    def apply(self, word_set):
        if not self.current_string:
            return word_set
        return word_set.filter(word__startswith=self.current_string)


class WordFilterByContains(WordFilterByString):
    def __init__(self, id, wordlist):
        super(WordFilterByContains, self).__init__(id, wordlist)
        self.label = 'Word contains'
        self.remake_form()

    def apply(self, word_set):
        if not self.current_string:
            return word_set
        return word_set.filter(word__contains=self.current_string)


class WordFilterByDefStartsWith(WordFilterByString):
    def __init__(self, id, wordlist):
        super(WordFilterByDefStartsWith, self).__init__(id, wordlist)
        self.label = 'Text starts with'
        self.remake_form()

    def apply(self, word_set):
        if not self.current_string:
            return word_set
        return word_set.filter(definition__startswith=self.current_string)


class WordFilterByDefContains(WordFilterByString):
    def __init__(self, id, wordlist):
        super(WordFilterByDefContains, self).__init__(id, wordlist)
        self.label = 'Text contains'
        self.remake_form()

    def apply(self, word_set):
        if not self.current_string:
            return word_set
        return word_set.filter(definition__contains=self.current_string)


class StringFilterForm(forms.Form):
    def __init__(self, id, string, wordlist, *args, **kwargs):
        super(StringFilterForm, self).__init__(*args, **kwargs)
        self.fields['string'] = forms.CharField(initial=string)
        self.fields['string'].widget.attrs['onchange'] = \
                'update_string_filter(%d)' % id


# Date Filters
################

class WordFilterByDate(object):
    def __init__(self, id, wordlist):
        self.id = id
        self.wordlist = wordlist
        now = datetime.now()
        self.current_day = now.day
        self.current_month = now.month
        self.current_year = now.year
        self.comparator = 'lt'
        self.label = ''

    def apply(self, word_set):
        raise NotImplementedError()

    def remake_form(self):
        self._form = DateFilterForm(self.id, self.comparator, self.current_day,
                self.current_month, self.current_year, self.wordlist)

    def form(self):
        # This BoundField business is a bit of a hack to just get the part of
        # the HTML that I want.  I could build the HTML for it myself, but this
        # was a little easier.
        ret_val = '<td>%s:' % self.label
        ret_val += '</td><td>'
        comp = forms.forms.BoundField(self._form, self._form.fields['comp'],
                'date_filter_%d' % self.id)
        ret_val += comp.as_widget()
        date = forms.forms.BoundField(self._form, self._form.fields['date'],
                'date_filter_%d' % self.id)
        ret_val += date.as_widget()
        ret_val += '</td><td class="remove" '
        ret_val += 'onclick="remove_filter(%d)">X</td>' % self.id
        return ret_val


class WordFilterByLastReviewed(WordFilterByDate):
    def __init__(self, id, wordlist):
        super(WordFilterByLastReviewed, self).__init__(id, wordlist)
        self.label = 'Last Reviewed'
        self.remake_form()

    def apply(self, word_set):
        d = date(self.current_year, self.current_month, self.current_day)
        if self.comparator == 'eq':
            d2 = date(self.current_year, self.current_month, self.current_day+1)
            return word_set.filter(last_reviewed__range=(d, d2))
        if self.comparator == 'lt':
            return word_set.filter(last_reviewed__lt=d)
        if self.comparator == 'gt':
            return word_set.filter(last_reviewed__gt=d)
        raise ValueError('Comparator is not supported: %s' % self.comparator)


class DateFilterForm(forms.Form):
    def __init__(self, id, comp, day, month, year, wordlist, *args, **kwargs):
        super(DateFilterForm, self).__init__(*args, **kwargs)
        now = datetime.now()
        d = date(year, month, day)
        years = [now.year-1, now.year]
        comparator_choices = [('lt', 'Before'), ('gt', 'After'), ('eq', 'On')]
        self.fields['comp'] = forms.ChoiceField(comparator_choices,
                label='', initial=comp)
        self.fields['comp'].widget.attrs['onchange'] = \
                'update_date_filter(%d)' % id
        self.fields['date'] = forms.DateField(initial=d,
                widget=SelectDateWidget(years=years))
        self.fields['date'].widget.attrs['onchange'] = \
                'update_date_filter(%d)' % id



# vim: et sw=4 sts=4
