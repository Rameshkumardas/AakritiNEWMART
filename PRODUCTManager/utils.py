from import_export import resources, fields, instance_loaders
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget

from import_export import resources

from PRODUCTManager.models import ProductList

class PRODUCTListResource(resources.ModelResource):
    class Meta:
        model = ProductList


