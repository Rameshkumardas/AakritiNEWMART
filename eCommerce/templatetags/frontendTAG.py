from django import template
from CATEGORYManager.models import MainCategory, SubCategory, SubSubCategory
from django.utils.safestring import mark_safe

import json

register = template.Library()

@register.inclusion_tag('./templates/includes/MegaMenuSubSubCatList.html', )
def SubSubCatListTAG(subCat):
    try:
        SubSubCatList = SubSubCategory.objects.filter(subCat_id=subCat)
        context = {
            'SubSubCatList': SubSubCatList
        }
        return context
    except Exception:
        return 'DoesNotExist'
    
    

@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))