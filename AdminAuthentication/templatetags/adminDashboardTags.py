from django import template
from AdminAuthentication.models import AdminRegistration


register = template.Library()


# ===============Admin Tags=============
@register.simple_tag
def TotalAdmins():
    allData = AdminRegistration.objects.filter(role=1).count()
    return allData

@register.simple_tag
def TotalActiveAdmins():
    allData = AdminRegistration.objects.filter(role=1, is_active=True).count()
    return allData

@register.simple_tag
def TotalDeactiveAdmins():
    allData = AdminRegistration.objects.filter(role=1, is_active=False).count()
    return allData

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
def activeUSER():
    allData = AdminRegistration.objects.filter(is_active=True, is_verified=True).exclude(is_accountant=True).count()
    return allData

@register.simple_tag
def deactiveUSER():
    allData = AdminRegistration.objects.filter(is_active=True, is_verified=True).exclude(is_accountant=True).count()
    return allData

@register.simple_tag
def onlineUSER():
    allData = AdminRegistration.objects.filter(is_active=True, is_verified=True, is_login=True).exclude(is_accountant=True).count()
    return allData

@register.simple_tag
def offlineUSER():
    allData = AdminRegistration.objects.filter(is_active=True, is_verified=True, is_login=False).exclude(is_accountant=True).count()
    return allData
# ===============End Users Tags=============
# ===============End Users Tags=============
# ===============End Users Tags=============
# ===============End Users Tags=============
# ===============End Users Tags=============

