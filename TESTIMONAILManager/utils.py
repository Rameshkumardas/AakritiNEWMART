from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export import resources, fields, instance_loaders
from .models import TestimonialList

class TESTIMONAILListResource(resources.ModelResource):
    class Meta:
        model = TestimonialList
        # fields = ('id', 'name', 'img', 'is_active',)
        # export_order = ('id', 'img', 'name', 'is_active')

# class EVENTSubCatListResource(resources.ModelResource):
#     class Meta:
#         model = EVENTSubCat


# class EVENTListResource(resources.ModelResource):
#     class Meta:
#         model = EVENTList
