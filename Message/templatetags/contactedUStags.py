from django import template
from AdminAuthentication.models import AdminRegistration
from Message.models import ContactUS

register = template.Library()


@register.simple_tag
def allCONTACTEDUSER():
    return ContactUS.objects.all().count()

@register.simple_tag
def pendingCONTACTEDUSER():
    return ContactUS.objects.filter(is_received=False).count()

@register.simple_tag
def acceptedCONTACTEDUSER():
    return ContactUS.objects.filter(is_received=True, is_verified=True).count()

@register.simple_tag
def closedCONTECTEDUSER():
    return ContactUS.objects.filter(is_rejected=True).count()

@register.simple_tag
def userNAME(user_id):
    return AdminRegistration.objects.get(user_id=user_id).full_name
    
