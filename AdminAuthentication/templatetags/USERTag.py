from django import template
from AdminAuthentication.models import AdminRegistration

register = template.Library()
# ===============End Admin Tags=============

# ===============Users Tags=============
# ===============Users Tags=============

# ===============Users Tags=============
# ===============Users Tags=============
# ===============Users Tags=============
@register.simple_tag
def totalUSER():
    allData = AdminRegistration.objects.all().exclude(is_accountant=True).count()
    return allData

@register.simple_tag
def draftUSER():
    allData = AdminRegistration.objects.filter(is_draft=True).exclude(is_accountant=True).count()
    return allData


@register.simple_tag
def activeUSER():
    allData = AdminRegistration.objects.filter(is_active=True, is_verified=True, is_draft=False).exclude(is_accountant=True).count()
    return allData


@register.simple_tag
def deactiveUSER():
    allData = AdminRegistration.objects.filter(is_draft=True, is_active=False).exclude(is_deleted=True).exclude(is_accountant=True).count()
    return allData

@register.simple_tag
def onlineUSER():
    allData = AdminRegistration.objects.filter(is_active=True, is_verified=True, is_login=True).exclude(is_accountant=True).count()
    return allData

@register.simple_tag
def offlineUSER():
    allData = AdminRegistration.objects.filter(is_active=True, is_verified=True, is_login=False).exclude(is_accountant=True).count()
    return allData

@register.simple_tag
def deletedUSER():
    allData = AdminRegistration.objects.filter(is_deleted=True).exclude(is_draft=True).exclude(is_accountant=True).count()
    return allData
# ===============End Users Tags=============
# ===============End Users Tags=============
# ===============End Users Tags=============
# ===============End Users Tags=============
# ===============End Users Tags=============

