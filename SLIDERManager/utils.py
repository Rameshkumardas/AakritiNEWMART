from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import BANNERCatList, BANNERList

class BANNERResource(resources.ModelResource):
    class Meta:
        model = BANNERList
        # fields = ('id', 'name', 'img', 'is_active',)
        # export_order = ('id', 'img', 'name', 'is_active')


class BANNERCatListResource(resources.ModelResource):
    class Meta:
        model = BANNERCatList
