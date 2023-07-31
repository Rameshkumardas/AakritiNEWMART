from django import template
from SALESManager.models import ProductOrderList

register = template.Library()

@register.simple_tag
def allORDERS(user):
    all = ProductOrderList.objects.filter(user_id=user).count()
    return all

@register.simple_tag
def allCANCELORDERS(user):
    all = ProductOrderList.objects.filter(user_id=user, is_cancel=True).count()
    return all
