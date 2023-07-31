from django import template
from ..models import BANNERList
from django import template

register = template.Library()


@register.simple_tag
def totalBANNER():
    BANNER = BANNERList.objects.filter(is_draft=True).count()
    return BANNER

@register.simple_tag
def draftBANNER():
    allBANNER = BANNERList.objects.filter(is_draft=True).exclude(is_deleted=True).count()
    return allBANNER

@register.simple_tag
def activeBANNER():
    allBANNER = BANNERList.objects.filter(is_active=True, is_verified=True).count()
    return allBANNER

@register.simple_tag
def deactivateBANNER():
    allBANNER = BANNERList.objects.filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).count()
    return allBANNER

@register.simple_tag
def deletedBANNER():
    allBANNER = BANNERList.objects.filter(is_deleted=True).count()
    return allBANNER