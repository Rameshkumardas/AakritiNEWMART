import datetime
from email.policy import default
from io import BytesIO
from statistics import mode
from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
from tinymce.models import HTMLField
# from Accounts.models import UserRegistration
# from django.contrib.postgres.fields import ArrayField
class FAQCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = AutoSlugField(populate_from='name',  unique=True, max_length=255, default=None)
    img = models.ImageField(max_length=200, upload_to="FAQMainCat", blank=False, null=False)
    is_active = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)    

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FAQList(models.Model):
    mainCat = models.ForeignKey(FAQCategory, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, blank=False, null=False)
    slug = AutoSlugField(populate_from='name',  unique=True, max_length=255, default=None)
    description = models.TextField(max_length=6000, blank=False, null=False, default='Description is Required')    
    is_draft = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)    
    is_verified = models.BooleanField(default=False)    
    is_deleted = models.BooleanField(default=False)    
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    def faq_name(self):
        return self.name
