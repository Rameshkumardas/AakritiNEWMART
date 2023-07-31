from django import template
from ..models import TestimonialList

register = template.Library()


@register.simple_tag
def draftTESTIMONIAL():
    allTESTIMONIAL = TestimonialList.objects.filter(is_draft=True).count()
    return allTESTIMONIAL

@register.simple_tag
def activeTESTIMONIAL():
    allTESTIMONIAL = TestimonialList.objects.filter(is_active=True).count()
    return allTESTIMONIAL

@register.simple_tag
def deactivateTESTIMONIAL():
    allTESTIMONIAL = TestimonialList.objects.filter(is_active=False).exclude(is_draft=True).exclude(is_deleted=True).count()
    return allTESTIMONIAL

@register.simple_tag
def deletedTESTIMONIAL():
    allTESTIMONIAL = TestimonialList.objects.filter(is_deleted=True).count()
    return allTESTIMONIAL