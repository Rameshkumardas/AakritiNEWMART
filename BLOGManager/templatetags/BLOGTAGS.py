from django import template

from AdminAuthentication.HELPER import CONVERT_NUMBER
from ..models import BLOGList, BlogSubCat
from django import template

register = template.Library()

        
@register.simple_tag
def totalBLOG():
    allBLOG = BLOGList.objects.select_related('SubCat').select_related('author').filter(is_draft=True).count()
    return CONVERT_NUMBER(allBLOG)

@register.simple_tag
def draftBLOG():
    allBLOG = BLOGList.objects.select_related('SubCat').select_related('author').filter(is_draft=True).exclude(is_deleted=True).count()
    return CONVERT_NUMBER(allBLOG)

@register.simple_tag
def activeBLOG():
    allBLOG = BLOGList.objects.select_related('SubCat').select_related('author').filter(is_active=True, is_verified=True).count()
    return CONVERT_NUMBER(allBLOG)

@register.simple_tag
def deactivateBLOG():
    allBLOG = BLOGList.objects.select_related('SubCat').select_related('author').filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).count()
    return CONVERT_NUMBER(allBLOG)

@register.simple_tag
def deletedBLOG():
    allBLOG = BLOGList.objects.select_related('SubCat').select_related('author').filter(is_deleted=True).count()
    return CONVERT_NUMBER(allBLOG)

@register.inclusion_tag('./template/TAGS/BLOGSubCatMEGAMENU.html',)
def BLOGSUBCATMenuList(mainCat, total):
    try:
        BLOGSUBCATMenuList = BlogSubCat.objects.select_related('mainCat').filter(mainCat_id=mainCat)[:total]
        context = {
            'BLOGSUBCATMenuList': BLOGSUBCATMenuList
        }
        return context
    except BlogSubCat.DoesNotExist:
        return 'Error Occured'