from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import REFUNDREQUESTList

class REFUNDListResource(resources.ModelResource):
    class Meta:
        model = REFUNDREQUESTList

