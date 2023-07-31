from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import EMAILList, EMAILTEMPLATEList

class EMAILListResource(resources.ModelResource):
    class Meta:
        model = EMAILList
        
class EMAILTEMPLATEListResource(resources.ModelResource):
    class Meta:
        model = EMAILTEMPLATEList
