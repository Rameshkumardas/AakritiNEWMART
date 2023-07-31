# Create your models here.
from email.policy import default
from pyexpat import model
from django.db import models
from django.template.defaultfilters import slugify
import datetime



# Create Color Code Model
class COLORList(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    code = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=False)
    date = models.CharField(max_length=15, null=True, blank=True, default=datetime.datetime.now().strftime("%d, %B - %Y"))
    last_update = models.CharField(max_length=15, null=True, blank=True, default='')
    def __str__(self):
        return self.name


class REGIONList(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    pcode = models.CharField(unique=True, max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=False)
    date = models.CharField(max_length=15, null=True, blank=True, default=datetime.datetime.now().strftime("%d, %B - %Y"))
    last_update = models.CharField(max_length=15, null=True, blank=True, default='')
    def __str__(self):
        return self.name


class SHIPPINGList(models.Model):
    type = models.CharField(max_length=255, blank=False, null=False)
    kg_range = models.CharField(max_length=255, blank=False, null=False)
    local = models.FloatField(blank=False, null=False,default=0)
    regional = models.FloatField(blank=False, null=False,default=0)
    national = models.FloatField(blank=False, null=False,default=0)
    special = models.FloatField(blank=False, null=False,default=0)
    is_active = models.BooleanField(default=False)
    date = models.CharField(max_length=15, null=True, blank=True, default=datetime.datetime.now().strftime("%d, %B - %Y"))
    last_update = models.CharField(max_length=15, null=True, blank=True, default='')
    def __str__(self):
        return self.name
    
    
