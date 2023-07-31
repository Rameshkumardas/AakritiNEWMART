from django.contrib.auth.decorators import login_required
from Category.models import SubCategory

def SubCatList(request):
    return {'SubCatList': SubCategory.objects.filter(is_active=True)}



