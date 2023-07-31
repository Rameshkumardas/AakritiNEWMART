from PRODUCTManager.models import ProductList
from django.contrib.sitemaps import Sitemap
from django.urls import reverse



class ProductListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ProductList.objects.filter(is_verified=True, is_active=True)
    def location(self, item):
        return (f"/product/{(item.slug)}/")

class MainCatProductListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ProductList.objects.filter(is_verified=True, is_active=True)
    def location(self, item):
        return (f"/all/{(item.mainCat.slug)}/")

        
class SubCatProductListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ProductList.objects.filter(is_verified=True, is_active=True)
    def location(self, item):
        return (f"/all/{(item.mainCat.slug)}/{(item.subCat.slug)}/")

class SubSubCatProductListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ProductList.objects.filter(is_verified=True, is_active=True)
    def location(self, item):
        return (f"/all/{(item.mainCat.slug)}/{(item.subCat.slug)}/{(item.SubSubCat.slug)}/")

