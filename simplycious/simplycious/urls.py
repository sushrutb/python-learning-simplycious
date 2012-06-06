from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^products/$', 'products.views.index'),
                       url(r'^products/(?P<product_id>\d+/$)', 'products.views.productdetail'),
                       url(r'^category/$', 'products.views.categoryindex'),                     
                       url(r'^tag/', include('tags.urls')),
                       
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^accounts/login/$',  login),
                       (r'^accounts/logout/$', logout),
)
