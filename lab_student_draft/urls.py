# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',  # noqa
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here
    url(r'^rank-preference/$', 'students.views.rank_preference', name="rank-preference"),
    url(r'^update-group/$', 'students.views.update_group', name="update-group"),
    url(r'^select-group/$', 'labs.views.select_group', name="select-group"),
    url(r'^results-list/$', 'students.views.results_list', name="results-list"),
    url(r'^lab-results/$', 'labs.views.lab_results', name="lab-results"),
    url(r'^lab-slots/$', 'labs.views.lab_slots', name="lab-slots"),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
