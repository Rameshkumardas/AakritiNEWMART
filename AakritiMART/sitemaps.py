from CMSManager.models import PAGEList
from PRODUCTManager.models import ProductList
from django.contrib.sitemaps import Sitemap
from BLOGManager.models import BLOGList
from django.urls import reverse

class staticSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = 'https'
    def items(self):
        return ()
        
    def location(self, item):
        return reverse(item)



class PageListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return PAGEList.objects.filter(is_verified=True, is_active=True)
    def location(self, item):
        return (f"/{(item.slug)}/")

