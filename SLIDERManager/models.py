from autoslug import AutoSlugField
from django.utils import timezone
from django.db import models
from django.core.validators import FileExtensionValidator


from AdminAuthentication.models import AdminRegistration
from CMSManager.models import PAGEList
# BANNER CATEGORY 
class BANNERCatList(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)    
    is_draft =models.BooleanField(default=True)
    is_active =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
#BANNER LIST
class BANNERList(models.Model):
    BANNERCat = models.ForeignKey(BANNERCatList, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(AdminRegistration, null=True, blank=True, on_delete=models.CASCADE)
    page = models.ForeignKey(PAGEList, null=True, blank=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)    
    target = models.CharField(max_length=225, blank=False, null=False)
    
    
    title = models.CharField(max_length=225, blank=True, null=True, default='')
    code = models.CharField(max_length=225, blank=True, null=True, default='')


    img = models.ImageField(max_length=200, upload_to="SLIDER/BANNERS/IMG/", blank=True, null=True, default='')

    is_video =models.BooleanField(default=False)
    is_youtube = models.BooleanField(default=False)    
    is_vimeo = models.BooleanField(default=False)   
    is_local = models.BooleanField(default=False)   
    
    local_video = models.FileField(upload_to='SLIDER/BANNERS/VIDEO/',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], default='')
    

    is_draft =models.BooleanField(default=True)
    is_active =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
