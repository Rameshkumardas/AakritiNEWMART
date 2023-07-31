from django.contrib.auth.decorators import login_required
from BLOGManager.models import BlogMainCat


def BLOGmainCatList(request):
    return {'BLOGmainCatList': BlogMainCat.objects.filter(is_active=True)}


