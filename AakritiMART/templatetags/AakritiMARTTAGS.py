from django import template

from PRODUCTManager.models import SIMILARPRODUCTSList
register = template.Library()


@register.simple_tag()
def multiply(qty, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
    return int(qty) * int(unit_price)


@register.inclusion_tag('./template/TAGS/ATTRIBUTEList.html', )
def ATTRIBUTEList(product_id):
    try:
        targetModel = SIMILARPRODUCTSList.objects.filter(product_id=product_id)
        context = {
            'attributes': targetModel,
        }
        return context
    except Exception:
        return 'DoesNotExist'