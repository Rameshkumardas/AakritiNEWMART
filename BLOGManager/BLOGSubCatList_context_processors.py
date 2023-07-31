from django.contrib.auth.decorators import login_required
from BLOGManager.models import BlogSubCat

def SubCatList(request):
    return {'BLOGSubCatList': BlogSubCat.objects.filter(is_active=True)}



