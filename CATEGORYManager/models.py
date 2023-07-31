from AdminAuthentication.HELPER import CONVERT_NUMBER
from autoslug import AutoSlugField
from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    img = models.ImageField(max_length=200, upload_to="MainCategory", blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)    
    is_header = models.BooleanField(default=False)
    is_draft =models.BooleanField(default=True)
    is_active =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    # @property
    # def mainCatPRODUCTCOUNT(self, *args, **kwargs):        
    #     return CONVERT_NUMBER(ProductList.objects.select_related('author','mainCat','subCat','SubSubCat','brand','color').filter(mainCat_id=self.pk, is_active=True, is_verified=True).exclude(is_deleted=True).count())
    
 

class SubCategory(models.Model):
    mainCat = models.ForeignKey(MainCategory, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)  
    img = models.ImageField(max_length=200, upload_to="SubCategory", blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)    
    
    is_draft =models.BooleanField(default=True)
    is_active =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)


    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

class SubSubCategory(models.Model):
    subCat = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)  
    img = models.ImageField(max_length=200, upload_to="SubSubCategory", blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)    

    is_draft =models.BooleanField(default=True)
    is_active =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)


    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)