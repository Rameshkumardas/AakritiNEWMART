from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.template.defaultfilters import slugify
from AdminAuthentication.models import AdminRegistration
from django.core.validators import RegexValidator
from django.db import models

phoneREG = RegexValidator(regex=r'^\+?1?\d{9,15}$', message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
EmailREG = RegexValidator(regex=r'^\+?1?\d{9,15}$', message = "Email Example@gmail.com Allowed.")


class shippingADDRESS(models.Model):
    user = models.ForeignKey(AdminRegistration, related_name="SHIPPINGADDRESSList", on_delete=models.CASCADE)
    fname = models.CharField(max_length=100, blank=True, null=True, default='')
    lname = models.CharField(max_length=100, blank=True, null=True, default='')
    email = models.CharField(max_length=100, blank=True, null=True, default='')
    contact = models.CharField(max_length=100, blank=True, null=True, default='')
    code = models.CharField(max_length=10, blank=True, null=True, default='')
    house_no = models.CharField(max_length=255, blank=True, null=True, default='')
    landmark = models.CharField(max_length=500, blank=True, null=True, default='')
    colony = models.CharField(max_length=500, blank=True, null=True, default='')
    city = models.CharField(max_length=255, blank=True, null=True, default='')
    state = models.CharField(max_length=255, blank=True, null=True, default='')
    country = models.CharField(max_length=255, blank=True, null=True, default='')
    date = models.DateTimeField(auto_now_add=True)    
    last_update = models.DateTimeField(auto_now_add=True)    
