from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import  FAQCategory, FAQList




class FAQMainCatListResource(resources.ModelResource):
    class Meta:
        model = FAQCategory
        # fields = ('id', 'name', 'img', 'is_active',)
        # export_order = ('id', 'img', 'name', 'is_active')

class FAQResource(resources.ModelResource):
    class Meta:
        model = FAQList
