from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^products/$', 'products.views.index'),
                       url(r'^product/add/$', 'products.views.add'),
                       url(r'^product/(?P<product_id>\d+)/', 'products.views.get_by_id'),
                       url(r'^product/(?P<product_slug>[-\w]+)/$', 'products.views.get_by_name'),

                       url(r'^categories/$', 'category.views.index'),
                       url(r'^category/add/$', 'category.views.add'),
                       url(r'^category/savecategory/$', 'category.views.save'),
                       url(r'^category/(?P<cat_slug>[-\w]+)/$', 'category.views.categorydetail'),
                       
                       
                       url(r'^admin/', include(admin.site.urls)),
                       
                       (r'^accounts/login/$',  login),
                       (r'^accounts/logout/$', logout),
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()