from AdminAuthentication.models import AdminRegistration
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

class EMAILList(models.Model):
    author = models.ForeignKey(AdminRegistration, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30, blank=True, null=True, default='')
    email = models.CharField(max_length=100, blank=True, null=True, default='')  
    contact = models.CharField(max_length=20, blank=True, null=True, default='')
    is_draft = models.BooleanField(default=True)
    is_active =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)


class EMAILTEMPLATEList(models.Model):
    author = models.ForeignKey(AdminRegistration, null=True, blank=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=255)    
    description = models.TextField(max_length=6500, null=False, blank=False)
    is_draft =models.BooleanField(default=True)
    is_active =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)

    views = models.IntegerField(blank=True, null=True, default=0)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    @property
    def get_view_count(self, *args, **kwargs):
        return CONVERT_NUMBER(self.views)
    