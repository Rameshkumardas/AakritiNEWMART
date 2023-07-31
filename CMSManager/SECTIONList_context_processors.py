from django.contrib.auth.decorators import login_required
from CMSManager.models import SECTIONList


def HEADERSECTIONList(request):
    return {'HEADERSECTIONList': SECTIONList.objects.filter(is_active=True, is_header=True)}

def FOOTERSECTIONList(request):
    return {'FOOTERSECTIONList': SECTIONList.objects.filter(is_active=True, is_footer=True)}

def MOBILESECTIONList(request):
    return {'MOBILESECTIONList': SECTIONList.objects.filter(is_active=True, is_menu=True)}
