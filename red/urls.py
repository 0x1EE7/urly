from django.conf.urls import include, url
from django.contrib import admin
from urly.views import UrlCreate, UrlSuccess, UrlRedirect
admin.autodiscover()

urlpatterns = (url(r'^$', UrlCreate.as_view()),
               url(r'^admin/', include(admin.site.urls)),
               url(r'^created_url/(?P<url>\w+)',
                   UrlSuccess.as_view(), name='created_url'),
               url(r'^(?P<url>\w+)$', UrlRedirect.as_view()),
               )
