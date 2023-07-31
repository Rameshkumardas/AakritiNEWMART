import datetime
from email.policy import default
from io import BytesIO
from statistics import mode
from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from AdminAuthentication.HELPER import CONVERT_NUMBER
from PRODUCTManager.models import ProductList
# from Accounts.models import UserRegistration
# from django.contrib.postgres.fields import ArrayField

class SECTIONList(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    img = models.ImageField(max_length=200, upload_to="INDUSTRYList/Items", blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)    

    redirect_to = models.CharField(max_length=225, blank=True, null=True, default="javascript:void(0);")

    logo = HTMLField(max_length=6000, blank=True, null=True, default="logo")

    is_header = models.BooleanField(default=False)
    is_footer = models.BooleanField(default=False)
    is_menu = models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

class PAGEList(models.Model):
    section = models.ForeignKey(SECTIONList, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ManyToManyField(ProductList, related_name="CMSProductList")

    name = models.CharField(max_length=50, blank=False, null=False)
    slug = AutoSlugField(populate_from='name',  unique=True, max_length=255, default=None)

    is_product = models.BooleanField(default=False)
    is_url = models.BooleanField(default=False)
    redirect_to = models.CharField(max_length=50, blank=False, null=False, default='')
    description = models.TextField(max_length=6000, blank=False, null=False, default='Description is Required')    

    meta_title = models.CharField(max_length=255, default='')
    meta_keywords = models.TextField(max_length=6500, default='')
    meta_description = models.CharField(max_length=255, default='')
    

    views = models.IntegerField(default=0)

    
    is_draft = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)    
    is_verified = models.BooleanField(default=False)    
    is_deleted = models.BooleanField(default=False)    
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    
    def PAGE_name(self):
        return self.name

    @property
    def get_view_count(self, *args, **kwargs):
        return CONVERT_NUMBER(self.views)