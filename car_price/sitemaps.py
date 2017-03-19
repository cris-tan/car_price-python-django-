from django.contrib import sitemaps

from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site, SiteManager

from project.models import *
from django.template.defaultfilters import slugify
from django.db.models import Q, Avg, Count

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def location(self, obj):
        if len(obj) == 1:
            return reverse(obj[0])
        elif len(obj) == 2:
            return reverse(obj[0],args=[obj[1]])
        else:
            return reverse(obj[0],args=[obj[1], obj[2]])

    def items(self):
        urls = [["main"], ]

        #names = Car.objects.values('name').distinct().annotate(davg=Avg('price'))
        names = Make.objects.all()
        
        tp_names = [["brand", slugify(name.name)+"-prices"] for name in names]
        
        brands = []
        for name in names:
            #tp_brand = Car.objects.filter(name=name["name"]).values('brand').distinct().annotate(davg=Avg('price'))
            tp_brand = name.model_set.values('name').distinct()
            brand = [["brand", slugify(name.name) + "-" + slugify(brand["name"])+"-prices"] for brand in tp_brand]
            brands += brand

        return urls + tp_names + brands

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='www.supercarreport.com', name='www.supercarreport.com')
        return super(StaticViewSitemap, self).get_urls(site=site, **kwargs)

