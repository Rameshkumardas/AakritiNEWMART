from django import template
from ..models import BRANDList
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
def draftBRAND():
    allBRAND = BRANDList.objects.filter(is_draft=True).count()
    return CONVERT_NUMBER(allBRAND)

@register.simple_tag
def activeBRAND():
    allBRAND = BRANDList.objects.filter(is_active=True).count()
    return CONVERT_NUMBER(allBRAND)

@register.simple_tag
def deactivateBRAND():
    allBRAND = BRANDList.objects.filter(is_active=False).exclude(is_draft=True).exclude(is_deleted=True).count()
    return CONVERT_NUMBER(allBRAND)

@register.simple_tag
def deletedBRAND():
    allBRAND = BRANDList.objects.filter(is_deleted=True).count()
    return CONVERT_NUMBER(allBRAND)