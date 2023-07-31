from django import template
from ..models import EMAILList
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
def totalEMAIL():
    allEMAIL = EMAILList.objects.select_related('SubCat').select_related('author').filter(is_draft=True).count()
    return CONVERT_NUMBER(allEMAIL)

@register.simple_tag
def draftEMAIL():
    allEMAIL = EMAILList.objects.select_related('SubCat').select_related('author').filter(is_draft=True).exclude(is_deleted=True).count()
    return CONVERT_NUMBER(allEMAIL)

@register.simple_tag
def activeEMAIL():
    allEMAIL = EMAILList.objects.select_related('SubCat').select_related('author').filter(is_active=True, is_verified=True).count()
    return CONVERT_NUMBER(allEMAIL)

@register.simple_tag
def deactivateEMAIL():
    allEMAIL = EMAILList.objects.select_related('SubCat').select_related('author').filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).count()
    return CONVERT_NUMBER(allEMAIL)

@register.simple_tag
def deletedEMAIL():
    allEMAIL = EMAILList.objects.select_related('SubCat').select_related('author').filter(is_deleted=True).count()
    return CONVERT_NUMBER(allEMAIL)


@register.simple_tag
def stillEMAIL():
    allEMAIL = EMAILList.objects.select_related('author').filter(is_sent=False).count()
    return CONVERT_NUMBER(allEMAIL)

@register.simple_tag
def sentEMAIL():
    allEMAIL = EMAILList.objects.select_related('author').filter(is_sent=True).count()
    return CONVERT_NUMBER(allEMAIL)