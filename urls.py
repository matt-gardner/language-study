from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Main index page
    (r'^$', 'drills.main.index'),

    # Common urls
    (r'^add-tag-to-word/(?P<tag_name>[^/]*)$',
        'drills.common.add_tag_to_word'),

    # Filters
    (r'^new-filter/(?P<name>[^/]*)$', 'drills.filters.add_filter'),
    (r'^remove-filter/(?P<id>[^/]*)$', 'drills.filters.remove_filter'),
    (r'^update-tag-filter/(?P<id>[^/]*)/(?P<tag>[^/]*)$',
        'drills.filters.update_tag_filter'),
    (r'^update-difficulty-filter/(?P<id>[^/]*)/(?P<comp>[^/]*)/'
        '(?P<value>[^/]*)$', 'drills.filters.update_difficulty_filter'),
    (r'^update-string-filter/(?P<id>[^/]*)/(?P<string>[^/]*)$',
        'drills.filters.update_string_filter'),
    (r'^update-date-filter/(?P<id>[^/]*)/(?P<comp>[^/]*)/(?P<year>[^/]*)/'
        '(?P<month>[^/]*)/(?P<day>[^/]*)$',
        'drills.filters.update_date_filter'),

    # All words urls
    (r'^all-words/$', 'drills.all_words.index'),
    (r'^all-words/create-word-list$', 'drills.all_words.create_word_list'),
    (r'^all-words/add-tag$', 'drills.all_words.add_tag'),
    (r'^all-words/delete-word-list/(?P<name>[^/]*)$',
        'drills.all_words.delete_word_list'),
    (r'^all-words/add-word-to-list$', 'drills.all_words.add_word_to_list'),
    (r'^all-words/next-word/(?P<difficulty>[^/]*)$',
        'drills.common.next_word'),
    (r'^all-words/prev-word/$', 'drills.common.prev_word'),
    (r'^all-words/get-word-list/(?P<name>[^/]*)$',
        'drills.common.get_word_list'),
    (r'^all-words/reorder-word-list/(?P<ordering>[^/]*)$',
        'drills.common.reorder_word_list'),

    # Difficulty urls
    (r'^difficulty/$', 'drills.difficulty.index'),
    (r'^difficulty/create-word-list$',
        'drills.difficulty.create_word_list'),
    (r'^difficulty/add-tag$', 'drills.difficulty.add_tag'),
    (r'^difficulty/delete-word-list/(?P<name>[^/]*)$',
        'drills.difficulty.delete_word_list'),
    (r'^difficulty/add-word-to-list$',
        'drills.difficulty.add_word_to_list'),
    (r'^difficulty/next-word/(?P<difficulty>[^/]*)$',
        'drills.difficulty.next_word'),
    (r'^difficulty/get-word-list/(?P<name>[^/]*)$',
        'drills.common.get_word_list'),

    # Site media
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # Login stuff
    (r'accounts/login/$', 'django.contrib.auth.views.login', {'template_name':
        'login.html'}),
)
