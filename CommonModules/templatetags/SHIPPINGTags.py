import json
from CommonModules.models import SHIPPINGList
from django import template
register = template.Library()

@register.simple_tag
def getMINRNAGE(pk):
    try:
        data = SHIPPINGList.objects.get(pk=pk).kg_range
        range01 = data.replace("(", "")
        range02 = range01.replace(")", "")
        range03 = range02.replace(" ", "")
        range04 = range03.replace("'", "")
        kg = range04.split(',')
        return kg[0]
    except Exception:
        return 0

@register.simple_tag
def getMAXRANGE(pk):
    try:
        data = SHIPPINGList.objects.get(pk=pk).kg_range
        range01 = data.replace("(", "")
        range02 = range01.replace(")", "")
        range02 = range01.replace(")", "")
        range03 = range02.replace(" ", "")
        range04 = range03.replace("'", "")
        kg = range04.split(',')
        return kg[1]
    except Exception:
        return 0
