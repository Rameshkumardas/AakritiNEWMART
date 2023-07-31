from django import template
from ..models import FAQList

from django.shortcuts import render

register = template.Library()

@register.simple_tag
def draftFAQ():
    faq = FAQList.objects.filter(is_draft=True).exclude(is_deleted=True).count()
    return faq

@register.simple_tag
def activeFAQ():
    faq = FAQList.objects.filter(is_draft=False, is_active=True).count()
    return faq

@register.simple_tag
def deactiveFAQ():
    faq = FAQList.objects.filter(is_draft=False, is_active=False).exclude(is_deleted=True).count()
    return faq

@register.simple_tag
def deletedFAQ():
    faq = FAQList.objects.filter(is_deleted=True).count()
    return faq
    
    
    

# @register.inclusion_tag('articleslist.html')
# def popularARTICLES(mainCat, total, pk):
#     context = {
#         'articles':FAQList.objects.filter(is_draft=False, is_active=True).order_by('-views')[:total]
#         }
#     return context


@register.inclusion_tag('./templates/includes/faqList.html')
def getFAQList(total):
    context = {
        'faqList':FAQList.objects.filter(is_active=True, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).order_by('-id')[:total],
        }
    return context


