from django import template
from PRODUCTManager.models import ProductList
register = template.Library()

@register.simple_tag
def draftPRODUCT():
    allPRODUCT = ProductList.objects.select_related('mainCat', 'subCat','SubSubCat').filter(is_draft=True).exclude(is_deleted=True).count()
    return allPRODUCT

@register.simple_tag
def activePRODUCT():
    allPRODUCT = ProductList.objects.select_related('mainCat', 'subCat','SubSubCat').filter(is_active=True, is_verified=True).count()
    return allPRODUCT

@register.simple_tag
def deactivatePRODUCT():
    allPRODUCT = ProductList.objects.select_related('mainCat', 'subCat','SubSubCat').filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).count()
    return allPRODUCT

@register.simple_tag
def deletedPRODUCT():
    allPRODUCT = ProductList.objects.select_related('mainCat', 'subCat','SubSubCat').filter(is_deleted=True).count()
    return allPRODUCT