from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

choice = '(?P<choice>[^/]*)'
comp = '(?P<comp>[^/]*)'
day = '(?P<day>[^/]*)'
difficulty = '(?P<difficulty>[^/]*)'
id = '(?P<id>[^/]*)'
month = '(?P<month>[^/]*)'
mood = '(?P<mood>[^/]*)'
name = '(?P<name>[^/]*)'
number = '(?P<number>[^/]*)'
ordering = '(?P<ordering>[^/]*)'
person = '(?P<person>[^/]*)'
string = '(?P<string>[^/]*)'
tag = '(?P<tag>[^/]*)'
tense = '(?P<tense>[^/]*)'
value = '(?P<value>[^/]*)'
voice = '(?P<voice>[^/]*)'
year = '(?P<year>[^/]*)'

urlpatterns = patterns('',
    # Main index page
    (r'^$',
        'drills.main.index'),

    # Common urls
    (r'^add-tag-to-word/'+tag+'$',
        'drills.common.add_tag_to_word'),
    (r'^remove-tag-from-word/'+tag+'$',
        'drills.common.remove_tag_from_word'),
    (r'^set-by-definition/'+value+'$',
        'drills.common.set_by_definition'),

    # Filters
    (r'^new-filter/'+name+'$',
        'drills.filters.add_filter'),
    (r'^remove-filter/'+id+'$',
        'drills.filters.remove_filter'),
    (r'^update-one-choice-filter/'+id+'/'+choice+'$',
        'drills.filters.update_one_choice_filter'),
    (r'^update-value-comp-filter/'+id+'/'+comp+'/'+value+'$',
        'drills.filters.update_value_comp_filter'),
    (r'^update-string-filter/'+id+'/'+string+'$',
        'drills.filters.update_string_filter'),
    (r'^update-date-filter/'+id+'/'+comp+'/'+year+'/'+month+'/'+day+'$',
        'drills.filters.update_date_filter'),

    # All words urls
    (r'^all-words/$',
        'drills.all_words.index'),
    (r'^all-words/create-word-list$',
        'drills.all_words.create_word_list'),
    (r'^all-words/add-tag$',
        'drills.all_words.add_tag'),
    (r'^all-words/delete-word-list/'+name+'$',
        'drills.all_words.delete_word_list'),
    (r'^all-words/add-word-to-list$',
        'drills.all_words.add_word_to_list'),
    (r'^all-words/next-word/'+difficulty+'$',
        'drills.common.next_word'),
    (r'^all-words/prev-word/$',
        'drills.common.prev_word'),
    (r'^all-words/get-word-list/'+name+'$',
        'drills.common.get_word_list'),
    (r'^all-words/reorder-word-list/'+ordering+'$',
        'drills.common.reorder_word_list'),

    # Difficulty urls
    (r'^difficulty/$',
        'drills.difficulty.index'),
    (r'^difficulty/create-word-list$',
        'drills.difficulty.create_word_list'),
    (r'^difficulty/add-tag$',
        'drills.difficulty.add_tag'),
    (r'^difficulty/delete-word-list/'+name+'$',
        'drills.difficulty.delete_word_list'),
    (r'^difficulty/add-word-to-list$',
        'drills.difficulty.add_word_to_list'),
    (r'^difficulty/next-word/'+difficulty+'$',
        'drills.difficulty.next_word'),
    (r'^difficulty/get-word-list/'+name+'$',
        'drills.common.get_word_list'),

    # Form drilling urls
    (r'^forms/$',
        'drills.forms.index'),
    (r'^view-forms/$',
        'drills.forms.view_forms'),
    (r'^inflect-form/'+person+'/'+number+'/'+tense+'/'+mood+'/'+voice+'$',
        'drills.forms.inflect_form'),
    (r'^guess-form/'+person+'/'+number+'/'+tense+'/'+mood+'/'+voice+'$',
        'drills.forms.guess_form'),
    (r'^get-new-verb/'+id+'$',
        'drills.forms.get_new_verb'),
    (r'^get-new-random-form/$',
        'drills.forms.get_new_random_form'),

    # Site media
    (r'^site-media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # Login stuff
    (r'accounts/login/$', 'django.contrib.auth.views.login', {'template_name':
        'login.html'}),
)
