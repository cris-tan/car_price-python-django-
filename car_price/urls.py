from django.conf.urls import url, include

from django.contrib import admin
from project import views
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    url(r'^$', views.main, name="main"),
    url(r'^(?P<car_name>[^/]+)/$', views.req_brand, name="brand"),
    url(r'^(?P<car_name>[^/]+)/(?P<brand>[^/]+)/$', views.redirect_url, name="year"),
    
    url(r'^robots\.txt$', include('robots.urls')),
]

