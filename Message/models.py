from django.db import models
from AdminAuthentication.models import AdminRegistration


class Feedback(models.Model):
    user =  models.ForeignKey(AdminRegistration, on_delete=models.CASCADE)
    is_for = models.CharField(max_length=255,  blank=True, null=True, default='')
    ratting = models.IntegerField(blank=True, null=True, default=1)
    is_useful = models.CharField(max_length=10,  blank=True, null=True, default='')
    subject = models.CharField(max_length=255,  blank=True, null=True, default='')
    opinion = models.TextField(max_length=6000,  blank=True, null=True, default='')
    description = models.TextField(max_length=6000,  blank=True, null=True, default='')
    status = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)    
    last_update = models.CharField(max_length=25,  blank=True, null=True)

class Portfolio(models.Model):
    name = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    img = models.ImageField(max_length=200, upload_to="user/portfolio", blank=True, null=True, default='')
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.CharField(max_length=25, null=True)


class ContactUS(models.Model):
    firstname = models.CharField(max_length=150, blank=True, null=True, default='')
    lastname= models.CharField(max_length=150, blank=True, null=True, default='')
    email = models.CharField(max_length=150, blank=True, null=True, default='')
    phone = models.CharField(max_length=150, blank=True, null=True, default='')
    subject = models.CharField(max_length=150, blank=True, null=True, default='')
    message = models.TextField(max_length= 5000, blank=True, null=True, default='')
    is_received = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    
    date = models.DateTimeField(auto_now_add=True)


class EmailNewslatters(models.Model):
    email = models.EmailField(unique=True, max_length=50, blank=False, null=False)
    is_verified = models.BooleanField(default=True)
    is_subscribed = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

class MobileNewslatters(models.Model):
    number = models.CharField(max_length=50, blank=False, null=False)
    is_verified = models.BooleanField(default=True)
    is_subscribed = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)


class ContactUSwithWEB(models.Model):
    name = models.CharField(max_length= 255, blank=True, null=True, default='')
    email = models.EmailField(unique=False, max_length=50, blank=False, null=False)
    phone = models.CharField(max_length= 255, blank=True, null=True, default='')
    address = models.CharField(max_length= 255, blank=True, null=True, default='')
    description = models.TextField(max_length= 5000, blank=True, null=True, default='')
    
    status = models.CharField(max_length=150, blank=True, null=True, default='pending')
    satisfied = models.IntegerField(blank=True, null=True, default=0)
    date = models.DateTimeField(auto_now_add=True)

class downloadREQUEST(models.Model):
    first_name = models.CharField(max_length= 255, blank=True, null=True, default='')
    last_name = models.CharField(max_length= 255, blank=True, null=True, default='')
    email = models.EmailField(unique=False, max_length=50, blank=False, null=False)
    phone = models.CharField(max_length= 255, blank=True, null=True, default='')
    status = models.IntegerField(blank=True, null=True, default=0)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date',)




class Announcements(models.Model):
    author = models.ForeignKey(AdminRegistration, null=True, blank=True, on_delete=models.CASCADE)

    subject = models.CharField(max_length= 255, blank=True, null=True, default='')
    description = models.TextField(max_length= 5000, blank=True, null=True, default='')
    status = models.CharField(max_length= 255, blank=True, null=True, default='pending')
    date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)


