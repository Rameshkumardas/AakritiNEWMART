from django import template
from ..models import REFUNDREQUESTList
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
def totalREFUND():
    allREFUND = REFUNDREQUESTList.objects.select_related('product', 'user').filter(is_draft=True).count()
    return CONVERT_NUMBER(allREFUND)

@register.simple_tag
def draftREFUND():
    allREFUND = REFUNDREQUESTList.objects.select_related('product', 'user').filter(is_draft=True).exclude(is_deleted=True).count()
    return CONVERT_NUMBER(allREFUND)

@register.simple_tag
def activeREFUND():
    allREFUND = REFUNDREQUESTList.objects.select_related('product', 'user').filter(is_active=True, is_verified=True).count()
    return CONVERT_NUMBER(allREFUND)

@register.simple_tag
def deactivateREFUND():
    allREFUND = REFUNDREQUESTList.objects.select_related('product', 'user').filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).count()
    return CONVERT_NUMBER(allREFUND)

@register.simple_tag
def deletedREFUND():
    allREFUND = REFUNDREQUESTList.objects.select_related('product', 'user').filter(is_deleted=True).count()
    return CONVERT_NUMBER(allREFUND)