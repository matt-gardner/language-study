#!/usr/bin/env python

from django import forms
from django.http import HttpResponse

from memorizing.flashcards.models import Tag

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
                ret_val += '<tr>%s</tr>' % filter.form()
        ret_val += '<tr>%s</tr>' % self.add_filter_form()
        return ret_val


def possible_card_filters():
    possible_filters = [('None', '-------')]
    possible_filters.append(('tag', 'Tag'))
    possible_filters.append(('difficulty', 'Difficulty'))
    possible_filters.append(('startswith', 'Starts With'))
    possible_filters.append(('contains', 'Contains'))
    return possible_filters


def get_card_filter_by_name(name):
    if name == 'tag':
        return CardFilterByTag
    if name == 'difficulty':
        return CardFilterByDifficulty
    if name == 'startswith':
        return CardFilterByStartsWith
    if name == 'contains':
        return CardFilterByContains
    raise ValueError('There is no card filter with the name %s' % name)


def filter_cards(cards, filters):
    filter_form = FilterForm(possible_card_filters())
    id = 0
    for filter in filters:
        filter.id = id
        id += 1
        filter_form.add_filter(filter)
        cards = filter.apply(cards)
    return cards.all(), filter_form


def add_filter(request, name):
    filters = request.session.get('filters', [])
    filter_form = FilterForm(possible_card_filters())
    id = 0
    for filter in filters:
        filter.id = id
        filter_form.add_filter(filter)
        id += 1
    cardlist_name = request.session['cardlist-name']
    cardlist = request.user.cardlist_set.get(name=cardlist_name)
    new_filter = get_card_filter_by_name(name)(id, cardlist)
    filter_form.add_filter(new_filter)
    filters.append(new_filter)
    request.session['filters'] = filters
    return HttpResponse(filter_form.__unicode__())


def remove_filter(request, id):
    request.session['filters'].pop(int(id))
    request.session.modified = True
    filter_form = FilterForm(possible_card_filters())
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
    filter_form = FilterForm(possible_card_filters())
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
    filter_form = FilterForm(possible_card_filters())
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
    filter_form = FilterForm(possible_card_filters())
    id = 0
    for filter in request.session.get('filters', []):
        filter.id = id
        filter_form.add_filter(filter)
        id += 1
    return HttpResponse(filter_form.__unicode__())


# Filter Classes
################

class CardFilterByTag(object):
    def __init__(self, id, cardlist):
        self.id = id
        self.cardlist = cardlist
        self.current_tag = None
        self.remake_form()

    def apply(self, card_set):
        if not self.current_tag:
            return card_set
        tag = self.cardlist.tag_set.get(name=self.current_tag)
        return card_set.filter(tags=tag)

    def remake_form(self):
        if self.current_tag:
            tag = self.current_tag
        else:
            tag = 'None'
        self._form = TagFilterForm(self.id, tag, self.cardlist)

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
    # This really should be a nested class of TopicFilterByAttribute, but you
    # can't pickle nested classes...
    def __init__(self, id, tag, cardlist, *args, **kwargs):
        super(TagFilterForm, self).__init__(*args, **kwargs)
        tag_choices = [('None', 'All')]
        tags = cardlist.tag_set.all()
        for t in tags:
            tag_choices.append((t.name, t.name))
        self.fields['tag'] = forms.ChoiceField(tag_choices, label='Tag',
                initial=tag)
        self.fields['tag'].widget.attrs['onchange'] = \
                'update_tag_filter(%d)' % id


class CardFilterByDifficulty(object):
    def __init__(self, id, cardlist):
        self.id = id
        self.cardlist = cardlist
        self.current_comparator = 'gt'
        self.current_value = None
        self.remake_form()

    def apply(self, card_set):
        if not self.current_value:
            return card_set
        if self.current_comparator == 'gt':
            return card_set.filter(
                    average_difficulty__gt=self.current_value)
        if self.current_comparator == 'lt':
            return card_set.filter(
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
    # This really should be a nested class of TopicFilterByAttribute, but you
    # can't pickle nested classes...
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


class CardFilterByString(object):
    def __init__(self, id, cardlist):
        self.id = id
        self.cardlist = cardlist
        self.current_string = None
        self.name = ''

    def apply(self, card_set):
        if not self.current_string:
            return card_set
        return card_set.filter(word__startswith=self.current_string)

    def remake_form(self):
        self._form = StringFilterForm(self.id, self.current_string,
                self.cardlist)

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


class CardFilterByStartsWith(CardFilterByString):
    def __init__(self, id, cardlist):
        super(CardFilterByStartsWith, self).__init__(id, cardlist)
        self.label = 'Starts with'
        self.remake_form()

    def apply(self, card_set):
        if not self.current_string:
            return card_set
        return card_set.filter(word__startswith=self.current_string)


class CardFilterByContains(CardFilterByString):
    def __init__(self, id, cardlist):
        super(CardFilterByContains, self).__init__(id, cardlist)
        self.label = 'Contains'
        self.remake_form()

    def apply(self, card_set):
        if not self.current_string:
            return card_set
        return card_set.filter(word__contains=self.current_string)


class StringFilterForm(forms.Form):
    # This really should be a nested class of TopicFilterByAttribute, but you
    # can't pickle nested classes...
    def __init__(self, id, string, cardlist, *args, **kwargs):
        super(StringFilterForm, self).__init__(*args, **kwargs)
        self.fields['string'] = forms.CharField(initial=string)
        self.fields['string'].widget.attrs['onchange'] = \
                'update_string_filter(%d)' % id


# vim: et sw=4 sts=4
