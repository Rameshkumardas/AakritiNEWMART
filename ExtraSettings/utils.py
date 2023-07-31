from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import PROJECTInformation

class SETTINGResource(resources.ModelResource):
    class Meta:
        model = PROJECTInformation
