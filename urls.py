from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

choice = '(?P<choice>[^/]+)'
comp = '(?P<comp>[^/]+)'
day = '(?P<day>[^/]+)'
difficulty = '(?P<difficulty>[^/]+)'
id = '(?P<id>[^/]+)'
listname = '(?P<listname>[^/]+)'
month = '(?P<month>[^/]+)'
mood = '(?P<mood>[^/]+)'
name = '(?P<name>[^/]+)'
number = '(?P<number>[^/]+)'
ordering = '(?P<ordering>[^/]+)'
person = '(?P<person>[^/]+)'
string = '(?P<string>[^/]+)'
tag = '(?P<tag>[^/]+)'
tense = '(?P<tense>[^/]+)'
value = '(?P<value>[^/]+)'
voice = '(?P<voice>[^/]+)'
word_id = r'(?P<word_id>[\d]+)'
year = '(?P<year>[^/]+)'

urlpatterns = patterns('',
    # The main page is the main list view
    (r'^$',
        'drills.views.lists.main'),
    (r'^logout$',
        'drills.views.common.logout'),

    # Common urls
    (r'^add-tag-to-word/'+tag+'$',
        'drills.views.common.add_tag_to_word'),
    (r'^remove-tag-from-word/'+tag+'$',
        'drills.views.common.remove_tag_from_word'),
    (r'^set-by-definition/'+value+'$',
        'drills.views.common.set_by_definition'),

    # Filters
    (r'^new-filter/'+name+'$',
        'drills.views.filters.add_filter'),
    (r'^remove-filter/'+id+'$',
        'drills.views.filters.remove_filter'),
    (r'^update-one-choice-filter/'+id+'/'+choice+'$',
        'drills.views.filters.update_one_choice_filter'),
    (r'^update-value-comp-filter/'+id+'/'+comp+'/'+value+'$',
        'drills.views.filters.update_value_comp_filter'),
    (r'^update-string-filter/'+id+'/'+string+'$',
        'drills.views.filters.update_string_filter'),
    (r'^update-date-filter/'+id+'/'+comp+'/'+year+'/'+month+'/'+day+'$',
        'drills.views.filters.update_date_filter'),

    # All words urls
    (r'^'+listname+'/all-words/$',
        'drills.views.all_words.main'),
    (r'^'+listname+'/all-words/add-tag$',
        'drills.views.all_words.add_tag'),
    (r'^'+listname+'/all-words/next-word/'+difficulty+'$',
        'drills.views.common.next_word'),
    (r'^'+listname+'/all-words/prev-word/$',
        'drills.views.common.prev_word'),
    (r'^'+listname+'/all-words/reorder-word-list/'+ordering+'$',
        'drills.views.common.reorder_word_list'),

    # Difficulty urls
    (r'^'+listname+'/difficulty/$',
        'drills.views.difficulty.main'),
    (r'^'+listname+'/difficulty/add-tag$',
        'drills.views.difficulty.add_tag'),
    (r'^'+listname+'/difficulty/next-word/'+difficulty+'$',
        'drills.views.difficulty.next_word'),

    # Form drilling urls
    (r'^'+listname+'/forms/$',
        'drills.views.forms.main'),
    (r'^'+listname+'/view-forms/$',
        'drills.views.forms.view_forms'),
    (r'^inflect-form/'+person+'/'+number+'/'+tense+'/'+mood+'/'+voice+'$',
        'drills.views.forms.inflect_form'),
    (r'^guess-form/'+person+'/'+number+'/'+tense+'/'+mood+'/'+voice+'$',
        'drills.views.forms.guess_form'),
    (r'^get-new-verb/'+id+'$',
        'drills.views.forms.get_new_verb'),
    (r'^get-new-random-form/$',
        'drills.views.forms.get_new_random_form'),

    # List views
    # These are at the bottom because they tend to be matched by other things
    # that really shouldn't match.
    (r'^'+listname+'$',
        'drills.views.lists.single_list'),
    (r'^'+listname+'/add-word$',
        'drills.views.lists.add_word_to_list'),
    (r'^'+listname+'/add-word/add-irregular-form/'+number+'$',
        'drills.views.lists.add_irregular_form'),
    (r'^'+listname+'/'+word_id+'$',
        'drills.views.lists.single_word'),
    (r'^'+listname+'/'+word_id+'/add-irregular-form/'+number+'$',
        'drills.views.lists.add_irregular_form'),

    # Site media
    (r'^site-media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # Login stuff
    (r'accounts/login/$', 'django.contrib.auth.views.login', {'template_name':
        'login.html'}),
)
