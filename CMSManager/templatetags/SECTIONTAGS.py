from django import template
from CMSManager.models import SECTIONList
from django import template
from math import log, floor

register = template.Library()

#Convert Number into K M G T P
def CONVERT_NUMBER(count, *args, **kwargs):
        if(count>1000):
            units = ['', 'K', 'M', 'G', 'T', 'P']
            k = 1000.0
            magnitude = int(floor(log(count, k)))
            return '%.2f%s' % (count / k**magnitude, units[magnitude])
        else:
            return count
        
@register.simple_tag
def totalSECTION():
    allSECTION = SECTIONList.objects.select_related('SubCat').select_related('author').filter(is_draft=True).count()
    return CONVERT_NUMBER(allSECTION)

@register.simple_tag
def draftSECTION():
    allSECTION = SECTIONList.objects.select_related('SubCat').select_related('author').filter(is_draft=True).exclude(is_deleted=True).count()
    return CONVERT_NUMBER(allSECTION)

@register.simple_tag
def activeSECTION():
    allSECTION = SECTIONList.objects.select_related('SubCat').select_related('author').filter(is_active=True, is_verified=True).count()
    return CONVERT_NUMBER(allSECTION)

@register.simple_tag
def deactivateSECTION():
    allSECTION = SECTIONList.objects.select_related('SubCat').select_related('author').filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).count()
    return CONVERT_NUMBER(allSECTION)

@register.simple_tag
def deletedSECTION():
    allSECTION = SECTIONList.objects.select_related('SubCat').select_related('author').filter(is_deleted=True).count()
    return CONVERT_NUMBER(allSECTION)


