from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from sitemap.sitemaps import StaticViewSitemap, ArticleSitemap
sitemaps = {
    'static': StaticViewSitemap,
    'articles': ArticleSitemap,
 }
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sitemap.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
 ]