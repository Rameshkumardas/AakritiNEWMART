from BLOGManager.models import BLOGList, BlogMainCat, BlogSubCat
from django.contrib.sitemaps import Sitemap

class MAINCATBLOGListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return BlogMainCat.objects.filter(is_active=True)
    
    def location(self, item):
        return f'/blogs/{item.slug}/' 

class SUBCATBLOGListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return BlogSubCat.objects.filter(is_active=True)
    
    def location(self, item):
        return f'/blogs/{item.mainCat.slug}/{item.slug}/' 

class BLOGListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return BLOGList.objects.filter(is_active=True, is_verified=True)
    
    def location(self, item):
        return f'/learn/{item.slug}/' 

 