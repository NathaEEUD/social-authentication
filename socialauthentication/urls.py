"""Main URLs."""

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

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

    # Home URL
    url(
        r'^$',
        TemplateView.as_view(template_name="home.html"),
        name="home"
    ),

    # Logout URL
    url(
        r'^users/logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name="user-logout"
    ),
]
