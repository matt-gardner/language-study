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
    possible_filters.append(('timesreviewed', 'Times Reviewed'))
    return possible_filters


def get_word_filter_by_name(name):
    if name == 'tag':
        return TagFilter
    if name == 'difficulty':
        return DifficultyFilter
    if name == 'startswith':
        return StartsWithFilter
    if name == 'contains':
        return ContainsFilter
    if name == 'defstartswith':
        return DefStartsWithFilter
    if name == 'defcontains':
        return DefContainsFilter
    if name == 'lastreviewed':
        return LastReviewedFilter
    if name == 'timesreviewed':
        return TimesReviewedFilter
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


def update_one_choice_filter(request, id, choice):
    filter = request.session['filters'][int(id)]
    filter.current_choice = choice
    filter.remake_form()
    request.session.modified = True
    filter_form = FilterForm(possible_word_filters())
    id = 0
    for filter in request.session.get('filters', []):
        filter.id = id
        filter_form.add_filter(filter)
        id += 1
    return HttpResponse(filter_form.__unicode__())


def update_value_comp_filter(request, id, comp, value):
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

# One Choice Filters
################

class OneChoiceFilter(object):
    def __init__(self, id, wordlist):
        self.id = id
        self.wordlist = wordlist
        self.current_choice = 'None'
        self.choices = [('None', 'All')]
        self.label = ''

    def apply(self, word_set):
        raise NotImplementedError()

    def remake_form(self):
        self._form = OneChoiceFilterForm(self.id, self.current_choice,
                self.choices, self.wordlist)

    def form(self):
        # This BoundField business is a bit of a hack to just get the part of
        # the HTML that I want.  I could build the HTML for it myself, but this
        # was a little easier.
        ret_val = '<td>%s:' % self.label
        choice = forms.forms.BoundField(self._form, self._form.fields['choice'],
                'one_choice_filter_%d' % self.id)
        ret_val += '</td><td>'
        ret_val += choice.as_widget()
        ret_val += '</td><td class="remove" '
        ret_val += 'onclick="remove_filter(%d)">X</td>' % self.id
        return ret_val


class OneChoiceFilterForm(forms.Form):
    def __init__(self, id, choice, choices, wordlist, *args, **kwargs):
        super(OneChoiceFilterForm, self).__init__(*args, **kwargs)
        self.fields['choice'] = forms.ChoiceField(choices, label='Tag',
                initial=choice)
        self.fields['choice'].widget.attrs['onchange'] = \
                'update_one_choice_filter(%d)' % id


class TagFilter(OneChoiceFilter):
    def __init__(self, id, wordlist):
        super(TagFilter, self).__init__(id, wordlist)
        self.label = 'Tag'
        tags = wordlist.tag_set.all()
        for t in tags:
            self.choices.append((t.name, t.name))
        self.remake_form()

    def apply(self, word_set):
        if self.current_choice == 'None':
            return word_set
        tag = self.wordlist.tag_set.get(name=self.current_choice)
        return word_set.filter(tags=tag)


# Value Comparator Filters
##########################

class ValueComparatorFilter(object):
    def __init__(self, id, wordlist):
        self.id = id
        self.wordlist = wordlist
        self.comparator_choices = [('gt', 'Greater than'), ('lt', 'Less than')]
        self.current_comparator = self.comparator_choices[0][0]
        self.value_choices = []
        self.current_value = None
        self.label = ''
        self.filter_arg = ''

    def apply(self, word_set):
        if not self.current_value:
            return word_set
        filter_arg = self.filter_arg + '__' + self.current_comparator
        args = {filter_arg: self.current_value}
        return word_set.filter(**args)

    def remake_form(self):
        self._form = ValueComparatorFilterForm(self.id, self.current_comparator,
                self.current_value, self.comparator_choices, self.value_choices)

    def form(self):
        # This BoundField business is a bit of a hack to just get the part of
        # the HTML that I want.  I could build the HTML for it myself, but this
        # was a little easier.
        ret_val = '<td>%s:</td><td>' % self.label
        comp = forms.forms.BoundField(self._form, self._form.fields['comp'],
                'value_comp_filter_comp_%d' % self.id)
        ret_val += comp.as_widget()
        val = forms.forms.BoundField(self._form, self._form.fields['value'],
                'value_comp_filter_value_%d' % self.id)
        ret_val += val.as_widget()
        ret_val += '</td><td class="remove" '
        ret_val += 'onclick="remove_filter(%d)">X</td>' % self.id
        return ret_val


class ValueComparatorFilterForm(forms.Form):
    def __init__(self, id, comparator, value, comparator_choices,
            value_choices, *args, **kwargs):
        super(ValueComparatorFilterForm, self).__init__(*args, **kwargs)
        self.fields['comp'] = forms.ChoiceField(comparator_choices,
                label='', initial=comparator)
        self.fields['comp'].widget.attrs['onchange'] = \
                'update_value_comp_filter(%d)' % id
        self.fields['value'] = forms.ChoiceField(value_choices, label='',
                initial=value)
        self.fields['value'].widget.attrs['onchange'] = \
                'update_value_comp_filter(%d)' % id


class DifficultyFilter(ValueComparatorFilter):
    def __init__(self, id, wordlist):
        super(DifficultyFilter, self).__init__(id, wordlist)
        self.label = 'Difficulty'
        self.filter_arg = 'average_difficulty'
        self.value_choices = [(i*5, i*5) for i in range(9)]
        self.current_value = self.value_choices[0][0]
        self.remake_form()


class TimesReviewedFilter(ValueComparatorFilter):
    def __init__(self, id, wordlist):
        super(TimesReviewedFilter, self).__init__(id, wordlist)
        self.label = 'Times Reviewed'
        self.filter_arg = 'review_count'
        self.value_choices = [(i, i) for i in range(15)]
        self.current_value = self.value_choices[0][0]
        self.remake_form()


# String Filters
################

class StringFilter(object):
    def __init__(self, id, wordlist):
        self.id = id
        self.wordlist = wordlist
        self.current_string = None
        self.label = ''
        self.filter_arg = ''

    def apply(self, word_set):
        if not self.current_string:
            return word_set
        args = {self.filter_arg: self.current_string}
        return word_set.filter(**args)

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


class StringFilterForm(forms.Form):
    def __init__(self, id, string, wordlist, *args, **kwargs):
        super(StringFilterForm, self).__init__(*args, **kwargs)
        self.fields['string'] = forms.CharField(initial=string)
        self.fields['string'].widget.attrs['onchange'] = \
                'update_string_filter(%d)' % id


class StartsWithFilter(StringFilter):
    def __init__(self, id, wordlist):
        super(StartsWithFilter, self).__init__(id, wordlist)
        self.label = 'Word starts with'
        self.filter_arg = 'word__startswith'
        self.remake_form()


class ContainsFilter(StringFilter):
    def __init__(self, id, wordlist):
        super(ContainsFilter, self).__init__(id, wordlist)
        self.label = 'Word contains'
        self.filter_arg = 'word__contains'
        self.remake_form()


class DefStartsWithFilter(StringFilter):
    def __init__(self, id, wordlist):
        super(DefStartsWithFilter, self).__init__(id, wordlist)
        self.label = 'Text starts with'
        self.filter_arg = 'definition__startswith'
        self.remake_form()


class DefContainsFilter(StringFilter):
    def __init__(self, id, wordlist):
        super(DefContainsFilter, self).__init__(id, wordlist)
        self.label = 'Text contains'
        self.filter_arg = 'definition__contains'
        self.remake_form()


# Date Filters
################

class DateFilter(object):
    def __init__(self, id, wordlist):
        self.id = id
        self.wordlist = wordlist
        now = datetime.now()
        self.current_day = now.day
        self.current_month = now.month
        self.current_year = now.year
        self.comparator = 'lt'
        self.label = ''
        self.filter_arg = ''

    def apply(self, word_set):
        d = date(self.current_year, self.current_month, self.current_day)
        if self.comparator == 'eq':
            d2 = date(self.current_year, self.current_month, self.current_day+1)
            filter_arg = self.filter_arg + '__range'
            args = {filter_arg: (d, d2)}
        else:
            filter_arg = self.filter_arg + '__' + self.comparator
            args = {filter_arg: d}
        return word_set.filter(**args)

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


class LastReviewedFilter(DateFilter):
    def __init__(self, id, wordlist):
        super(LastReviewedFilter, self).__init__(id, wordlist)
        self.label = 'Last Reviewed'
        self.filter_arg = 'last_reviewed'
        self.remake_form()


# vim: et sw=4 sts=4
