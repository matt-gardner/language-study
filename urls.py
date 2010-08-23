from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'flashcards.views.index'),
    (r'^create-card-list$',
        'flashcards.views.create_card_list'),
    (r'^delete-card-list/(?P<name>[^/]*)$',
        'flashcards.views.delete_card_list'),
    (r'^add-card-to-list$', 'flashcards.views.add_card_to_list'),
    (r'accounts/login/$', 'django.contrib.auth.views.login', {'template_name':
        'login.html'}),

    # Feeds
    (r'^feeds/get-card-list/(?P<name>[^/]*)$',
        'flashcards.views.get_card_list'),
    (r'^feeds/randomize-card-list/$', 'flashcards.views.randomize_card_list'),
    (r'^feeds/unrandomize-card-list/$',
        'flashcards.views.unrandomize_card_list'),
    (r'^feeds/next-card/(?P<difficulty>[^/]*)$', 'flashcards.views.next_card'),
    (r'^feeds/prev-card/(?P<difficulty>[^/]*)$', 'flashcards.views.prev_card'),

    # Site media
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
