from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout


admin.autodiscover()

urlpatterns = patterns('',
                       # shows list of products, ordered by recently added.
                       url(r'^$', 'products.views.index'),
                       # compare products
                       # url(r'^products/compare/', 'products.views.compare1'),
                       url(r'^products/compare(?:/(?P<product1_slug>[-\w]+)/(?P<product2_slug>[-\w]+))?/$', 'products.views.compare'),
                       # add a new product.
                       url(r'^product/add/$', 'products.views.add'),
                       # show a product by id
                       url(r'^product/(?P<product_id>\d+)/', 'products.views.get_by_id'),
                       #show a product by slug
                       url(r'^product/(?P<product_slug>[-\w]+)/$', 'products.views.get_by_name'),

                       url(r'^categories/$', 'category.views.index'),
                       url(r'^category/add/$', 'category.views.add'),
                       url(r'^category/shootout/$', 'category.views.shootout'),
                       url(r'^category/savecategory/$', 'category.views.save'),
                       url(r'^category/(?P<cat_slug>[-\w]+)/$', 'category.views.get_by_slug'),
                       
                       url(r'^tags/add/$', 'tags.views.add'),
                       url(r'^admin/', include(admin.site.urls)),
                       
                       (r'^accounts/login/$',  login),
                       (r'^accounts/logout/$', logout),
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()