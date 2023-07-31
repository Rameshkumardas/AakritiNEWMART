from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.template.defaultfilters import slugify
from AdminAuthentication.models import AdminRegistration
from django.core.validators import RegexValidator
from django.db import models

phoneREG = RegexValidator(regex=r'^\+?1?\d{9,15}$', message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
EmailREG = RegexValidator(regex=r'^\+?1?\d{9,15}$', message = "Email Example@gmail.com Allowed.")

class shippingADDRESS(models.Model):
    user = models.ForeignKey(AdminRegistration, related_name="BILLINGADDRESS", on_delete=models.CASCADE)
    scode = models.CharField(max_length=10, blank=True, null=True, default='')
    shouse_no = models.CharField(max_length=255, blank=True, null=True, default='')
    slandmark = models.CharField(max_length=500, blank=True, null=True, default='')
    scolony = models.CharField(max_length=500, blank=True, null=True, default='')
    scity = models.CharField(max_length=255, blank=True, null=True, default='')
    sstate = models.CharField(max_length=255, blank=True, null=True, default='')
    scountry = models.CharField(max_length=255, blank=True, null=True, default='')
    more = models.CharField(max_length=255, blank=True, null=True, default='')

class billingADDRESS(models.Model):
    user = models.ForeignKey(AdminRegistration, related_name="SHIPPINGADDRESS", on_delete=models.CASCADE)
    bcode = models.CharField(max_length=10, blank=True, null=True, default='')
    bhouse_no = models.CharField(max_length=255, blank=True, null=True, default='')
    blandmark = models.CharField(max_length=500, blank=True, null=True, default='')
    bcolony = models.CharField(max_length=500, blank=True, null=True, default='')
    bcity = models.CharField(max_length=255, blank=True, null=True, default='')
    bstate = models.CharField(max_length=255, blank=True, null=True, default='')
    bcountry = models.CharField(max_length=255, blank=True, null=True, default='')

    more = models.CharField(max_length=255, blank=True, null=True, default='')



# Create AdminRegistration Profile Model
class mobileOTP(models.Model):
    pNumber = models.CharField(max_length=15,validators=[phoneREG], blank=True, null=True)
    Vcode = models.IntegerField(blank=True, null=True, default=0)


class emailOTP(models.Model):
    email = models.CharField(max_length=15,validators=[EmailREG], blank=True, null=True)
    Vcode = models.IntegerField(blank=True, null=True, default=0)


