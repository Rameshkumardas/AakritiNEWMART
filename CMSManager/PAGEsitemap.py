from .models import PAGEList
from django.contrib.sitemaps import Sitemap

class PAGEListSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return PAGEList.objects.filter(is_active=True, is_verified=True).exclude(is_url=True)

    def location(self, item):
        return f'/{item.slug}/' 
