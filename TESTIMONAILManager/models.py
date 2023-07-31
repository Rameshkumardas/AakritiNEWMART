from django.db import models

# Create your models here.

class TestimonialCatList(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

class TestimonialList(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')    
    is_draft = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    destination = models.CharField(max_length=200, blank=True, default='Student')
    ratting = models.IntegerField(default=5)
    img = models.ImageField(max_length=200, upload_to="Testimonial/IMG/", null=True, blank=True, default=None)
    description = models.TextField(max_length=6000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)


