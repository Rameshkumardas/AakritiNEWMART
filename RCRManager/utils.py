from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import RCRREQUESTList

class RETURNListResource(resources.ModelResource):
    class Meta:
        model = RCRREQUESTList

class CANCELListResource(resources.ModelResource):
    class Meta:
        model = RCRREQUESTList

class REPLACEMENTListResource(resources.ModelResource):
    class Meta:
        model = RCRREQUESTList
