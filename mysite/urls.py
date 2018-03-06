"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello, my_homepage_view, current_datetime, hours_ahead, display_meta, contact
from books import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    # url(r'^$', my_homepage_view),
    url(r'^time/$', current_datetime),
    url(r'^another-time-page/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^display-meta/$', display_meta),
    # url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
]

if settings.DEBUG:
    urlpatterns += [url(r'^debuginfo/$', views.debug),]
