from django.contrib.auth.decorators import login_required
from CATEGORYManager.models import MainCategory
def mainCatList(request):
    return {'mainCatList': MainCategory.objects.filter(is_active=True)}


