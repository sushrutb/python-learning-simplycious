from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^products/$', 'products.views.index'),
                       url(r'^products/add/$', 'products.views.add'),
                       url(r'^products/(?P<product_id>\d+/$)', 'products.views.productdetail'),
                       url(r'^tag/', include('tags.urls')),
                       
                       url(r'^category/$', 'category.views.index'),
                       url(r'^category/add/$', 'category.views.add'),
                        url(r'^category/savecategory/$', 'category.views.save'),
                       url(r'^category/(?P<cat_slug>[-\w]+/$)', 'category.views.categorydetail'),

                       
                       
                       url(r'^admin/', include(admin.site.urls)),
                       
                       (r'^accounts/login/$',  login),
                       (r'^accounts/logout/$', logout),
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()