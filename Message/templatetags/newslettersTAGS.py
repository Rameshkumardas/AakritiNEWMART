from django import template
from Message.models import EmailNewslatters, MobileNewslatters

register = template.Library()


@register.simple_tag
def allEmailNewslattersCOUNT():
    return EmailNewslatters.objects.all().count()

@register.simple_tag
def allMobileNewslattersCOUNT():
    return MobileNewslatters.objects.all().count()

