
import json
from django import template
from SALESManager.models import ProductOrderList

register = template.Library()
# ============ORDER Manager================
# ============ORDER Manager================
@register.simple_tag
def pendingORDERS():
    return ProductOrderList.objects.filter(is_confirmed=False).exclude(is_confirmed=True, is_cancel=True).count()

@register.simple_tag
def confirmedORDERS():
    return ProductOrderList.objects.filter(is_confirmed=True).exclude(is_shipped=True).exclude(is_deleted=True).exclude(is_shipped=True).count()

@register.simple_tag
def shippedORDERS():
    return ProductOrderList.objects.filter(is_shipped=True).exclude(is_deleted=True, is_cancel=True).count()

@register.simple_tag
def cancelORDERS():
    return ProductOrderList.objects.filter(is_cancel=True).count()

@register.simple_tag
def deliveryORDERS(status=0):
    return ProductOrderList.objects.filter(is_delivered=True).count()

@register.simple_tag
def ontheWayORDERS(status=0):
    return ProductOrderList.objects.filter(is_deleted=True).exclude(is_delivered=True).count()

@register.inclusion_tag('./template/orders/COLORQTY.html', )
def getcolorQTYList(pk):
    try:
        targetModel = ProductOrderList.objects.get(pk=pk)
        Array = json.loads(targetModel.color)
        arrayCOLOR = Array.values()

        qty = json.loads(targetModel.qty)
        arrayQTY = qty.values()
        context = {
            'attributes': zip(arrayCOLOR, arrayQTY)
        }
        return context
    except Exception:
        return 'DoesNotExist'


