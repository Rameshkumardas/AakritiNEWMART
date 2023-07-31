from django import template
from PRODUCTManager.models import ProductList

register = template.Library()

@register.simple_tag
def mainCATPRODUCT(mainCat):
    allPRODUCT = ProductList.objects.select_related('mainCat').select_related('subCat').select_related('SubSubCat').filter(mainCat_id=mainCat, is_active=True, is_verified=True).count()
    return allPRODUCT
