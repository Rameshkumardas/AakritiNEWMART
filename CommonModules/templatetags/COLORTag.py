import json
from django import template
from CommonModules.models import COLORList
from PRODUCTManager.models import ProductList
register = template.Library()
# ============AllColors================
# ============AllColors================
# ============AllColors================
# ============AllColors================
# ============AllColors================
# ============AllColors================
@register.inclusion_tag('./template/commonFeatures/allColors.html', )
def allcolors():
    data = COLORList.objects.filter(is_active=True).values('id', 'name')
    return {'colors': data}



# pass 1 2 3
@register.inclusion_tag('./template/commonFeatures/webCOLOR.html', )
def getCOLORList(pk):
    try:
        targetModel = ProductList.objects.get(pk=pk)
        Array = targetModel.color.split(',')
        # ProductColor0 = Array.replace('[', '')
        # ProductColor1 = ProductColor0.replace(']', '')
        # ProductColor2 = ProductColor1.replace("'", "")
        # ProductColor3 = ProductColor2.replace(" ", "")
        # ProductColorArray = ProductColor3.split(',')
        print(Array)
        PRODUCTCODEArray = []
        for i in Array:
            PRODUCTCODEArray.append(COLORList.objects.get(pk=i).name)
        
        print(PRODUCTCODEArray)

        context = {
            'colors': zip(Array, PRODUCTCODEArray),
        }
        return context
    except Exception:
        return 'DoesNotExist'




@register.simple_tag
def colorName(code):
    color = COLORList.objects.get(code=code)
    return color.name



