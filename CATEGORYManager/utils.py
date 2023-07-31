from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget

from import_export import resources, fields, instance_loaders
from .models import MainCategory, SubCategory, SubSubCategory
from import_export.fields import Field



class MainCatListResource(resources.ModelResource):
    class Meta:
        model = MainCategory
        # fields = ('id', 'name', 'img', 'is_active',)
        # export_order = ('id', 'img', 'name', 'is_active')

class SubCatListResource(resources.ModelResource):
    class Meta:
        model = SubCategory

class SubSubCatListResource(resources.ModelResource):
    class Meta:
        model = SubSubCategory



class SubCatListResource11(resources.ModelResource):
    mainCat_name = Field(column_name='mainCat_name', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory.name, field='name'))
    mainCat_slug = Field(column_name='mainCat_slug', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='slug'))
    mainCat_img = Field(column_name='mainCat_img', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='img'))
    mainCat_is_draft = Field(column_name='mainCat_is_draft', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='is_draft'))
    mainCat_is_active = Field(column_name='mainCat_is_active', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='is_active'))
    mainCat_is_verified = Field(column_name='mainCat_is_verified', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='is_verified'))
    mainCat_is_deleted = Field(column_name='mainCat_is_deleted', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='is_deleted'))
    # mainCat_date = Field(column_name='date', attribute='date', widget=ForeignKeyWidget(model=MainCategory.date, field='date'))
    # mainCat_last_update = Field(column_name='last_update', attribute='last_update', widget=ForeignKeyWidget(model=MainCategory.last_update, field='last_update'))
    class Meta:
        model = SubCategory
        fields = ('mainCat_name', 'mainCat_slug', 'mainCat_img', 'mainCat_is_draft', 'mainCat_is_active', 'mainCat_is_verified', 'mainCat_is_deleted','mainCat_date', 'mainCat_last_update', 'name', 'slug', 'img', 'is_draft', 'is_active', 'is_verified', 'is_deleted','date', 'last_update')


class SubSubCatListResource11(resources.ModelResource):
    mainCat_name = Field(column_name='mainCat_name', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory.name, field='name'))
    mainCat_slug = Field(column_name='mainCat_slug', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='slug'))
    mainCat_img = Field(column_name='mainCat_img', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='img'))
    mainCat_is_draft = Field(column_name='mainCat_is_draft', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='is_draft'))
    mainCat_is_active = Field(column_name='mainCat_is_active', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='is_active'))
    mainCat_is_verified = Field(column_name='mainCat_is_verified', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='is_verified'))
    mainCat_is_deleted = Field(column_name='mainCat_is_deleted', attribute='mainCat', widget=ForeignKeyWidget(model=MainCategory, field='is_deleted'))
    # mainCat_date = Field(column_name='date', attribute='date', widget=ForeignKeyWidget(model=MainCategory.date, field='date'))
    # mainCat_last_update = Field(column_name='last_update', attribute='last_update', widget=ForeignKeyWidget(model=MainCategory.last_update, field='last_update'))
    class Meta:
        model = SubSubCategory
        fields = ('mainCat_name', 'mainCat_slug', 'mainCat_img', 'mainCat_is_draft', 'mainCat_is_active', 'mainCat_is_verified', 'mainCat_is_deleted','mainCat_date', 'mainCat_last_update', 'name', 'slug', 'img', 'is_draft', 'is_active', 'is_verified', 'is_deleted','date', 'last_update')
