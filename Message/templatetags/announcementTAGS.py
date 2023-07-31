from django import template
from Message.models import Announcements

register = template.Library()


@register.simple_tag
def allANNOUNCEMETS():
    return Announcements.objects.all().count()

@register.simple_tag
def pendingANNOUNCEMETS():
    return Announcements.objects.filter(status=0).count()

@register.simple_tag
def verifiedANNOUNCEMETS():
    return Announcements.objects.filter(status=1).count()


