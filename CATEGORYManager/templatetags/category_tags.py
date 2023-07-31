from django import template
from ..models import MainCategory, SubCategory, SubSubCategory

register = template.Library()


@register.simple_tag
def MainCatName(pk):
    mainCat = MainCategory.objects.get(pk=pk)
    return mainCat.name

@register.simple_tag
def SubCatName(pk):
    subCat = SubCategory.objects.get(pk=pk)
    return subCat.name

@register.simple_tag
def SubSubCatName(pk):
    subCat = SubSubCategory.objects.get(pk=pk)
    return subCat.name

@register.simple_tag
def CountSubCategory(cat_id):
    allSubCat = SubCategory.objects.filter(cat_id=cat_id).count()
    return allSubCat

@register.simple_tag
def CountSubCategoryTopic(sub_cat_id):
    allSubCat = SubCategory.objects.filter(cat_id=cat_id).count()
    return allSubCat
    
# # @register.simple_tag
# # def define(val=None):
# #   return val
  
# # @register.filter
# # def lower(value):
# #     return value.lower()

# # @register.inclusion_tag("html file path")


@register.simple_tag
def CountMainCategory():
    allmainCat = MainCategory.objects.all().count()
    return allmainCat

@register.simple_tag
def CountAllSubCategory():
    allSubCat = SubCategory.objects.all().count()
    return allSubCat


# SubCatListTAG
@register.inclusion_tag('./template/TAGS/TopCategories.html', )
def TopCategoryList(total):
    try:
        memberList = MainCategory.objects.filter(is_active=True)[:total]
        context = {
            'mainCatList': memberList
        }
        return context
    except MainCategory.DoesNotExist:
        return 'Error Occured'
     