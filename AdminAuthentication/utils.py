from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import AdminRegistration

class STAFFListResource(resources.ModelResource):
    class Meta:
        model = AdminRegistration

class USERListResource(resources.ModelResource):
    class Meta:
        model = AdminRegistration
