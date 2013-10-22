from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.PageView.as_view(), { 'slug': 'indice' }, name='page'),
    url(r'^(?P<slug>\w+)/$', views.PageView.as_view(), name='page'),
)
