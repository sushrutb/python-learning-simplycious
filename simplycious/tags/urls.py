from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'add/$', 'tags.views.add'),
                       url(r'$', 'tags.views.index'),
)
