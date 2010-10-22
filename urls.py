from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Main index page
    (r'^$', 'flashcards.main.index'),

    # Common urls
    (r'^add-tag-to-card/(?P<tag_name>[^/]*)$',
        'flashcards.common.add_tag_to_card'),
    (r'^new-filter/(?P<name>[^/]*)$', 'flashcards.filters.add_filter'),
    (r'^remove-filter/(?P<id>[^/]*)$', 'flashcards.filters.remove_filter'),
    (r'^update-tag-filter/(?P<id>[^/]*)/(?P<tag>[^/]*)$',
        'flashcards.filters.update_tag_filter'),
    (r'^update-difficulty-filter/(?P<id>[^/]*)/(?P<comp>[^/]*)/'
        '(?P<value>[^/]*)$', 'flashcards.filters.update_difficulty_filter'),

    # All words urls
    (r'^all-words/$', 'flashcards.all_words.index'),
    (r'^all-words/create-card-list$', 'flashcards.all_words.create_card_list'),
    (r'^all-words/add-tag$', 'flashcards.all_words.add_tag'),
    (r'^all-words/delete-card-list/(?P<name>[^/]*)$',
        'flashcards.all_words.delete_card_list'),
    (r'^all-words/add-card-to-list$', 'flashcards.all_words.add_card_to_list'),
    (r'^all-words/next-card/(?P<difficulty>[^/]*)$',
        'flashcards.common.next_card'),
    (r'^all-words/prev-card/$', 'flashcards.common.prev_card'),
    (r'^all-words/get-card-list/(?P<name>[^/]*)$',
        'flashcards.common.get_card_list'),
    (r'^all-words/reorder-card-list/(?P<ordering>[^/]*)$',
        'flashcards.common.reorder_card_list'),

    # Difficulty urls
    (r'^difficulty/$', 'flashcards.difficulty.index'),
    (r'^difficulty/create-card-list$',
        'flashcards.difficulty.create_card_list'),
    (r'^difficulty/add-tag$', 'flashcards.difficulty.add_tag'),
    (r'^difficulty/delete-card-list/(?P<name>[^/]*)$',
        'flashcards.difficulty.delete_card_list'),
    (r'^difficulty/add-card-to-list$',
        'flashcards.difficulty.add_card_to_list'),
    (r'^difficulty/next-card/(?P<difficulty>[^/]*)$',
        'flashcards.difficulty.next_card'),
    (r'^difficulty/get-card-list/(?P<name>[^/]*)$',
        'flashcards.common.get_card_list'),

    # Site media
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # Login stuff
    (r'accounts/login/$', 'django.contrib.auth.views.login', {'template_name':
        'login.html'}),
)
