from django.conf.urls import patterns, include, url
from django.contrib import admin
from urly.views import UrlCreate
from urly.views import UrlSuccess, UrlRedirect
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', UrlCreate.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^created_url/(?P<url>\w+)',
                           UrlSuccess.as_view(), name='created_url'),
                       url(r'^(?P<url>\w+)$', UrlRedirect.as_view()),
                       )
