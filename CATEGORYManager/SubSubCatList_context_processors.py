from django.contrib.auth.decorators import login_required
from CATEGORYManager.models import SubSubCategory

def SubSubCatList(request):
    return {'SubSubCatList': SubSubCategory.objects.select_related('subCat').filter(is_active=True)}


# 