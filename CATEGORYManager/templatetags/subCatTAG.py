from django import template
from ..models import MainCategory, SubCategory, SubSubCategory

register = template.Library()

@register.inclusion_tag('./template/TAGS/subCatDropdown.html', )
def SubCatListTAG(mainCat, total):
    try:
        allMemuList = SubCategory.objects.filter(mainCat_id=mainCat, is_active=True)[:total]
        context = {
            'subCatList': allMemuList
        }
        return context
    except MainCategory.DoesNotExist:
        return 'Error Occured'
     

