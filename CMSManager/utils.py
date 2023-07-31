from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import SECTIONList, PAGEList

class PAGEResource(resources.ModelResource):
    class Meta:
        model = PAGEList
        # fields = ('id', 'name', 'img', 'is_active',)
        # export_order = ('id', 'img', 'name', 'is_active')



class SECTIONListResource(resources.ModelResource):
    class Meta:
        model = SECTIONList
