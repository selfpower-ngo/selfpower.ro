'''
sitemaps.py
'''
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Entry
from hub.models import Proiect

class StaticViewSitemap(Sitemap):
    '''
    StaticViewSitemap(Sitemap)
        items()
        location()
    '''
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'membri', 'doilasuta','contact']

    def location(self, item):
        return reverse(item)

class BlogPostSitemap(Sitemap):
    '''
    BlogPostSitemap(Sitemap)
        items()
        lastmod()
    '''
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return Entry.objects.published()

    def lastmod(self, obj):
        return obj.modified

#    def location(self, item):
#        return reverse(item)


class ProiecteIndexSitemap(Sitemap):
    '''
    ProiecteIndexSitemap(Sitemap)
        items()
        location()
    '''
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Proiect.objects.published()
        