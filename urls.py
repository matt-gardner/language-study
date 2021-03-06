from django.conf.urls import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

book_id = '(?P<book_id>[^/]+)'
case = '(?P<case>[^/]+)'
choice = '(?P<choice>[^/]+)'
comp = '(?P<comp>[^/]+)'
correct = '(?P<correct>[^/]+)'
day = '(?P<day>[^/]+)'
gender = '(?P<gender>[^/]+)'
id = '(?P<id>[^/]+)'
listname = '(?P<listname>[^/]+)'
month = '(?P<month>[^/]+)'
mood = '(?P<mood>[^/]+)'
name = '(?P<name>[^/]+)'
number = '(?P<number>[^/]+)'
ordering = '(?P<ordering>[^/]+)'
page_id = '(?P<page_id>[\d]+)'
page_num = '(?P<page_num>[^/]+)'
person = '(?P<person>[^/]+)'
review_style = '(?P<review_style>[^/]+)'
string = '(?P<string>[^/]+)'
tag = '(?P<tag>[^/]+)'
tense = '(?P<tense>[^/]+)'
user = '(?P<user>[^/]+)'
value = '(?P<value>[^/]+)'
verb_id = '(?P<verb_id>[^/]+)'
voice = '(?P<voice>[^/]+)'
word = '(?P<word>[^/]+)'
word_id = r'(?P<word_id>[\d]+)'
year = '(?P<year>[^/]+)'

urlpatterns = patterns('',
    # The main page is the main list view
    (r'^$',
        'drills.views.lists.main'),
    (r'^logout$',
        'drills.views.common.logout'),

    # Reading urls
    (r'^book/'+book_id+'/$',
        'reading.views.book'),
    (r'^book/'+book_id+'/page/'+page_num+'/$',
        'reading.views.page'),
    (r'^book/'+book_id+'/page/'+page_num+'/edit-chapter$',
        'reading.views.edit_page_chapter'),
    (r'^book/'+book_id+'/page/'+page_num+'/edit-text$',
        'reading.views.edit_page_text'),
    (r'^page-image/'+page_id+'$',
        'reading.views.page_image'),
    (r'^definition/'+word+'$',
        'reading.views.definition'),

    # Extension urls
    (r'^extension/definition/' + user + '/' + listname + '$',
        'drills.views.vocab.get_definition'),
    (r'^extension/read/' + user + '/' + listname + '$',
        'drills.views.vocab.submit_as_read'),

    # Vocab urls
    (r'^'+listname+'/vocab/$',
        'drills.views.vocab.main'),
    (r'^'+listname+'/vocab/next-word/'+correct+'$',
        'drills.views.vocab.next_word'),

    # Vocab (manual) urls
    (r'^'+listname+'/vocab/manual/$',
        'drills.views.vocab_manual.main'),
    (r'^'+listname+'/vocab/manual/add-tag$',
        'drills.views.vocab_manual.add_tag'),
    (r'^'+listname+'/vocab/manual/next-word/$',
        'drills.views.vocab_manual.next_word'),
    (r'^'+listname+'/vocab/manual/next-word/'+correct+'$',
        'drills.views.vocab_manual.next_word'),
    (r'^'+listname+'/vocab/manual/prev-word/$',
        'drills.views.vocab_manual.prev_word'),
    (r'^'+listname+'/vocab/manual/reorder-word-list/'+ordering+'$',
        'drills.views.vocab_manual.reorder_word_list'),
    (r'^'+listname+'/vocab/manual/set-by-definition/'+value+'$',
        'drills.views.vocab_manual.set_by_definition'),

    # Filters and tags
    (r'^'+listname+'/new-filter/'+name+'$',
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
    (r'^'+listname+'/add-tag-to-word/'+tag+'$',
        'drills.views.common.add_tag_to_word'),
    (r'^'+listname+'/remove-tag-from-word/'+tag+'$',
        'drills.views.common.remove_tag_from_word'),

    # Form drilling urls
    (r'^'+listname+'/forms/$',
        'drills.views.forms.drill_conjugations'),
    (r'^'+listname+'/forms/conjugations$',
        'drills.views.forms.drill_conjugations'),
    (r'^'+listname+'/forms/declensions$',
        'drills.views.forms.drill_declensions'),
    (r'^'+listname+'/get-new-random-form/$',
        'drills.views.forms.get_new_random_form'),
    (r'^'+listname+'/inflect-form/'+person+'/'+number+'/'+tense+'/'+mood+
            '/'+voice+'$',
        'drills.views.forms.inflect_form'),
    (r'^'+listname+'/guess-verb-form/'+person+'/'+number+'/'+tense+'/'+mood+
            '/'+voice+'$',
        'drills.views.forms.guess_verb_form'),
    (r'^'+listname+'/guess-noun-form/'+gender+'/'+number+'/'+case+'$',
        'drills.views.forms.guess_noun_form'),
    (r'^'+listname+'/get-new-verb/'+id+'$',
        'drills.views.forms.get_new_verb'),

    # Form viewing urls
    (r'^'+listname+'/view-forms/$',
        'drills.views.forms.view_forms'),
    (r'^'+listname+'/view-table/'+verb_id+'$',
        'drills.views.forms.view_table'),
    (r'^'+listname+'/view-table/'+verb_id+
            '/update-table/'+person+'/'+number+'$',
        'drills.views.forms.update_table'),

    # List views
    # These are at the bottom because they tend to be matched by other things
    # that really shouldn't match.
    (r'^'+listname+'$',
        'drills.views.lists.single_list'),
    (r'^'+listname+'/add-word$',
        'drills.views.lists.add_word_to_list'),
    (r'^'+listname+'/add-word/add-irregular-noun-form/'+number+'$',
        'drills.views.lists.add_irregular_noun_form'),
    (r'^'+listname+'/add-word/add-irregular-adj-form/'+number+'$',
        'drills.views.lists.add_irregular_adj_form'),
    (r'^'+listname+'/add-word/add-irregular-verb-form/'+number+'$',
        'drills.views.lists.add_irregular_verb_form'),
    (r'^'+listname+'/add-word/add-irregular-stem/'+number+'$',
        'drills.views.lists.add_irregular_stem'),
    (r'^'+listname+'/add-word/add-irregular-augment/'+number+'$',
        'drills.views.lists.add_irregular_augment'),
    (r'^'+listname+'/add-word/add-no-passive-tense/'+number+'$',
        'drills.views.lists.add_tense_with_no_passive'),
    (r'^'+listname+'/'+word_id+'$',
        'drills.views.lists.single_word'),
    (r'^'+listname+'/'+word_id+'/add-irregular-noun-form/'+number+'$',
        'drills.views.lists.add_irregular_noun_form'),
    (r'^'+listname+'/'+word_id+'/add-irregular-adj-form/'+number+'$',
        'drills.views.lists.add_irregular_adj_form'),
    (r'^'+listname+'/'+word_id+'/add-irregular-verb-form/'+number+'$',
        'drills.views.lists.add_irregular_verb_form'),
    (r'^'+listname+'/'+word_id+'/add-irregular-stem/'+number+'$',
        'drills.views.lists.add_irregular_stem'),
    (r'^'+listname+'/'+word_id+'/add-irregular-augment/'+number+'$',
        'drills.views.lists.add_irregular_augment'),
    (r'^'+listname+'/'+word_id+'/add-no-passive-tense/'+number+'$',
        'drills.views.lists.add_tense_with_no_passive'),

    # Site media
    (r'^site-media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # Login stuff
    (r'accounts/login/$', 'django.contrib.auth.views.login', {'template_name':
        'login.html'}),
)
