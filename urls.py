from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'flashcards.views.index'),
    (r'^create-card-list$', 'flashcards.views.create_card_list'),
    (r'accounts/login/$', 'django.contrib.auth.views.login', {'template_name':
        'login.html'}),
    # Example:
    # (r'^memorizing/', include('memorizing.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
