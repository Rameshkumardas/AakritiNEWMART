from PRODUCTManager.models import ProductList
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from BLOGManager.models import BLOGList

class staticSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = 'https'
    def items(self):
        return [
                'KHANTAILOR',
                'HowItWork',
                'About',
                'Contact',
                'FeedBack',
                'TermsCondition',
                'PrivicyPolicy',
                'CopyRightPolicy',
                'Security',
                'Disclaimer',
                'SIGNIN',
                'SIGNUP',
                'OTPLOGINVERFIFICATION',
                'FORGOTPASSWORD',
                'RESETPASSWORD',
                'ProductList',
                'ProductList',
            ]
        
    def location(self, item):
        return reverse(item)



class ProductListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ProductList.objects.filter(is_verified=True, is_active=True)
    def location(self, item):
        return '/product/%s' % (item.slug)


class BLOGListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
    
    def items(self):
        return BLOGList.objects.filter(is_active=True, is_verfified=True)
    
    def location(self, item):
        return '/BLOGVIEW/%s' % (item.slug)

 