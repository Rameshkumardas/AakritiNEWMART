from autoslug import AutoSlugField
from django.db import models


class BRANDList(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)    
    img = models.ImageField(max_length=200, upload_to="BRAND/IMG/", null=True, blank=True, default=None)
    description = models.TextField(max_length=6000, null=False, blank=False)
    views = models.PositiveIntegerField(default=0)
    is_draft = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)


