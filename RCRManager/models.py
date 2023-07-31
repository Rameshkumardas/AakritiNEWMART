from AdminAuthentication.models import AdminRegistration
from SALESManager.models import ProductOrderList
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.db import models
from math import log, floor
def CONVERT_NUMBER(count, *args, **kwargs):
        if(count>1000):
            units = ['', 'K', 'M', 'G', 'T', 'P']
            k = 1000.0
            magnitude = int(floor(log(count, k)))
            return '%.2f%s' % (count / k**magnitude, units[magnitude])
        else:
            return count

class RCRREQUESTList(models.Model):
    order = models.ForeignKey(ProductOrderList, null=True, blank=True, on_delete=models.SET_NULL, related_name="RCRList")
    is_return =models.BooleanField(default=False)
    is_cancel =models.BooleanField(default=False)
    is_replacement =models.BooleanField(default=False)

    is_draft =models.BooleanField(default=True)
    is_active =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

 
        



