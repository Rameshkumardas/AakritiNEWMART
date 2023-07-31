from django import template
from ..models import SubCategory, SubSubCategory

register = template.Library()

@register.inclusion_tag('./template/TAGS/SUBCATMenuList.html', )
def SubCatMenuList(mainCat, total):
    try:
        allMemuList = SubCategory.objects.select_related('mainCat').filter(mainCat_id=mainCat, is_active=True)[:total]
        context = {
            'SubCatMenuList': allMemuList
        }
        return context
    except SubCategory.DoesNotExist:
        return 'Error Occured'


@register.inclusion_tag('./template/TAGS/SUBSUBCATMenuList.html',)
def SubSubCatMenuList(subcat, total):
    try:
        allSubMemuList = SubSubCategory.objects.select_related('subCat', 'subCat__mainCat').filter(subCat_id=subcat)[:total]
        context = {
            'SubSubCatMenuList': allSubMemuList
        }
        return context
    except SubSubCategory.DoesNotExist:
        return 'Error Occured'