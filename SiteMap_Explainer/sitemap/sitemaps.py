from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Article

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'about', 'contact', 'article_list']

    def location(self, item):
        return reverse(item)

class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
