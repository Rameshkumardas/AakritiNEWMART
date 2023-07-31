from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import COLORList, REGIONList, SHIPPINGList
from import_export.fields import Field

class COLORListResource(resources.ModelResource):
    class Meta:
        model = COLORList

class REGIONListResource(resources.ModelResource):
    class Meta:
        model = REGIONList

class SHIPPINGListResource(resources.ModelResource):
    class Meta:
        model = SHIPPINGList
