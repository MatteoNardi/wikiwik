from django.conf.urls import patterns, include, url
from django.contrib import admin

from wiki.views import PageView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PageView.as_view(), { 'slug': 'indice' }, name='page'),
    url(r'^(?P<slug>\w+)/$', PageView.as_view(), name='page'),
)
