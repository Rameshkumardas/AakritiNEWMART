from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import BlogMainCat, BlogSubCat, BLOGList

class BLOGMainCatListResource(resources.ModelResource):
    class Meta:
        model = BlogMainCat
        # fields = ('id', 'name', 'img', 'is_active',)
        # export_order = ('id', 'img', 'name', 'is_active')

class BLOGSubCatListResource(resources.ModelResource):
    class Meta:
        model = BlogSubCat


class BLOGListResource(resources.ModelResource):
    class Meta:
        model = BLOGList
