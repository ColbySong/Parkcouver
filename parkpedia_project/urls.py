from django.conf.urls import patterns, include, url
from django.contrib import admin
from parkpedia import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
   #url(r'^parkpedia/', include('parkpedia.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'parkpedia.views.index', name='index'),
    url(r'^logout/$', 'parkpedia.views.logout', name='logout'),
    url(r'^favourite_park/', 'parkpedia.views.favourite_park', name='favourite'),
)
