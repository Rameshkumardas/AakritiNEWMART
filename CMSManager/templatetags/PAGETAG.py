from django.utils.safestring import mark_safe
from ..models import PAGEList, SECTIONList
from django.shortcuts import render
from django import template

register = template.Library()

@register.filter(name='highlight')
def highlight(text, search):
    highlighted = text.replace(search, '<b class="text bg-warning">{}</b>'.format(search))
    return mark_safe(highlighted)



@register.simple_tag
def draftPAGE():
    PAGE = PAGEList.objects.filter(is_draft=True).exclude(is_deleted=True).count()
    return PAGE

@register.simple_tag
def activePAGE():
    PAGE = PAGEList.objects.filter(is_draft=False, is_active=True).count()
    return PAGE

@register.simple_tag
def deactivePAGE():
    PAGE = PAGEList.objects.filter(is_draft=False, is_active=False).exclude(is_deleted=True).count()
    return PAGE

@register.simple_tag
def deletedPAGE():
    PAGE = PAGEList.objects.filter(is_deleted=True).count()
    return PAGE
    
    



@register.inclusion_tag('./template/TAGS/PAGEList.html')
def allPAGEList(section_id, total):
    try:
        context = {
            'PAGEList':PAGEList.objects.filter(section_id=section_id, is_active=True, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).order_by('id')[:total],
            }
        return context
    except:
        pass


@register.inclusion_tag('./template/TAGS/PAGEMenuList.html', )
def PAGEMenuList(section, total):
    try:
        allMemuList = PAGEList.objects.select_related('section').filter(section_id=section, is_active=True, is_verified=True)[:total]
        context = {
            'PAGEMenuList': allMemuList
        }
        return context
    except PAGEList.DoesNotExist:
        return 'Error Occured'

