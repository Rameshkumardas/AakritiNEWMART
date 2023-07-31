from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from autoslug import AutoSlugField


class adminModelManager(BaseUserManager):    

    def create_user(self, name, username, email, phone, password=None, img=None):
        if not name:
            raise ValueError('Name Required*')
        if not username:
            raise ValueError('Username Required*')
        if not email:
            raise ValueError('Email Required*')
        if not password:
            raise ValueError('Password Required*')
        if not phone:
            raise ValueError('Mobile Number Required*')

        admin = self.model(
            name=name,
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            password=password,
            img=img,
        )
        admin.is_user = True  
        admin.set_password(password)
        admin.save(using=self._db)
        return admin
    
    def create_admin(self, name, username, email, phone, password=None, img=None):

        admin = self.create_user(
            name=name,
            email=email,
            username=username,
            phone=phone,
            password=password,
            img=img,
        )
        admin.is_admin = True
        admin.is_accountant = True
        admin.is_user = True  
        admin.is_manager = True      
        admin.set_password(password)
        admin.save(using=self._db)
        return admin
    
    def create_superadmin(self, name, username, email, phone, password=None, img=None):
        admin = self.create_admin(
            name=name,
            email=email,
            username=username,
            phone=phone,
            password=password,
            img=img,
        )
        admin.is_superadmin = True
        admin.is_manager = True
        admin.is_accountant = True
        admin.is_user = True        
        admin.is_active = True        
        admin.is_verified = True    
        admin.login_block = False    
        admin.save(using=self._db)
        return admin

    def create_superuser(self, name, username, email, phone, password=None, img=None):
        admin = self.create_superadmin(
            name=name,
            email=email,
            username=username,
            phone=phone,
            password=password,
            img=img,
        )
        admin.save(using=self._db)
        return admin


    def create_reference_accountant(self, name, username, email, phone, password=None, img=None):
        ref = self.model(
            name=name,
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            password=password,
            img=img,
        )
        ref.set_password(password)
        ref.is_accountant = True
        ref.is_user = True        
        ref.is_reference=True
        ref.save(using=self._db)
        return ref

    def create_reference_staff(self, name, username, email, phone, password=None, img=None):
        ref = self.create_reference_accountant(
            name=name,
            email=email,
            username=username,
            phone=phone,
            password=password,
            img=img,
        )
        ref.is_admin = True
        ref.is_manager = True
        ref.save(using=self._db)
        return ref
    
    def create_reference_manager(self, name, username, email, phone, password=None, img=None):
        ref = self.create_reference_staff(
            name=name,
            email=email,
            username=username,
            phone=phone,
            password=password,
            img=img,
        )
        ref.is_admin = False
        ref.is_manager = True
        ref.save(using=self._db)
        return ref


class AdminRegistration(AbstractBaseUser):
    token = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    fname = models.CharField(max_length=100, null=True, blank=True)
    lname = models.CharField(max_length=100, null=True, blank=True)

    email = models.EmailField(unique=True, max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, blank=True, null=True, default='+917322057677')
    username = AutoSlugField(populate_from='email', unique=True, null=True, default=None)    
    password = models.CharField(max_length=100, null=False, blank=False, default='new')
    img = models.ImageField(max_length=200, upload_to="Accounts/AakritiMART/profileIMG/", null=True, blank=True, default='Accounts/DefaultIMG/profile.png')

    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)

    is_draft =models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)    
    is_verified = models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)

    is_account_completed = models.BooleanField(default=False)
    is_agree = models.BooleanField(default=True)

    is_reference = models.BooleanField(default=False)
    reference = models.CharField(max_length=100, blank=True, null=True, default='')
    
    is_login = models.BooleanField(default=False)

    is_suspended = models.BooleanField(default=False)

    is_access = models.BooleanField(default=False)
    is_access_days = models.IntegerField(default=0)

    AttemptCount = models.IntegerField(default=1)
    login_block = models.BooleanField(default=True)

    designation = models.CharField(max_length=100, null=False, blank=False, default='Developer')
    gender = models.CharField(max_length=200, blank=True, null=True, default='')
    dbirth = models.CharField(max_length=200, blank=True, null=True, default='')
   
    role = models.IntegerField(blank=True, default=0)

    pancard = models.CharField(max_length=200, blank=True, null=True, default='')
    aadharcard = models.CharField(max_length=200, blank=True, null=True, default='') 

    intro = models.TextField(max_length=1000, blank=True, null=True, default='')    

    experience = models.TextField(max_length=1000, blank=True, null=True, default='')    
    education = models.TextField(max_length=1000, blank=True, null=True, default='B-Tech in Computer Science from Geeta University')    

    address = models.CharField(max_length=200, blank=True, null=True, default='')
    address1 = models.CharField(max_length=200, blank=True, null=True, default='')
    pincode = models.IntegerField(default=110058)
    state = models.CharField(max_length=200, blank=True, null=True, default='')
    city = models.CharField(max_length=200, blank=True, null=True, default='')
    country = models.CharField(max_length=200, blank=True, null=True, default='')

    skills = models.CharField(max_length=200, blank=True, null=True, default='')                                      
    note = models.CharField(max_length=200, blank=True, null=True, default='')

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.CharField(max_length=15, null=True, blank=True, default='')
    
    objects = adminModelManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username', 'password', 'phone', 'img']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superadmin

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

class AdminActivity(models.Model):
    admin = models.ForeignKey(AdminRegistration, related_name="AdminActivity", on_delete=models.CASCADE)
    log = models.TextField(max_length=6000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwarg):
    if created:
        Token.objects.create(user=instance)
