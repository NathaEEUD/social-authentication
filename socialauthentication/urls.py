"""Main URLs."""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Administration site
    url(
        r'^admin/',
        include(admin.site.urls)
    ),

    # Python Social Auth
    url(
        '',
        include('social.apps.django_app.urls', namespace='social')
    ),
]
