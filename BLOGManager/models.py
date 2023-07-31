from AdminAuthentication.HELPER import CONVERT_NUMBER
from AdminAuthentication.models import AdminRegistration
from autoslug import AutoSlugField
from django.db import models


class BlogMainCat(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    img = models.ImageField(max_length=200, upload_to="BLOG/BlogMainCat", blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)    
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    
    @property
    def mainCatBLOGCOUNT(self, *args, **kwargs):        
        return CONVERT_NUMBER(BLOGList.objects.select_related('mainCat','SubCat', 'author').filter(mainCat_id=self.pk, is_active=True, is_verified=True).exclude(is_deleted=True).count())
    
 

class BlogSubCat(models.Model):
    mainCat = models.ForeignKey(BlogMainCat, null=True, related_name='MainCat', blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)  
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)    
    img = models.ImageField(max_length=200, upload_to="BLOG/BlogSubCat", blank=False, null=False)

    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    
    @property
    def subCatBLOGCOUNT(self, *args, **kwargs):        
        return CONVERT_NUMBER(BLOGList.objects.select_related('mainCat','SubCat', 'author').filter(SubCat_id=self.pk, is_active=True, is_verified=True).exclude(is_deleted=True).count())
    

class BLOGList(models.Model):
    mainCat = models.ForeignKey(BlogMainCat, related_name='BLOGMainCat', null=True, blank=True, on_delete=models.SET_NULL)
    SubCat = models.ForeignKey(BlogSubCat, related_name='BLOGSubCat', null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(AdminRegistration, null=True, blank=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)    
    img = models.ImageField(max_length=255, upload_to="BLOG/Items", null=True, blank=True)    
    intro = models.TextField(max_length=6500)
    description = models.TextField(max_length=6500)

    summary = models.TextField(max_length=6500)
    reference = models.TextField(max_length=6500)

    is_draft =models.BooleanField(default=True)
    is_active =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)

    meta_title = models.CharField(max_length=255)
    meta_keywords = models.TextField(max_length=6500)
    meta_description = models.CharField(max_length=255)
    
    likes = models.IntegerField(blank=True, null=True, default=0)
    views = models.IntegerField(blank=True, null=True, default=0)
    comment = models.IntegerField(blank=True, null=True, default=0)

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    @property
    def get_view_count(self, *args, **kwargs):
        return CONVERT_NUMBER(self.views)
        
    @property
    def draftBLOG():
        return CONVERT_NUMBER(BLOGList.objects.select_related('mainCat','SubCat', 'author').filter(is_draft=True).exclude(is_deleted=True).count())

    @property
    def activeBLOG():
        allBLOG = BLOGList.objects.select_related('mainCat','SubCat', 'author').filter(is_active=True, is_verified=True).count()
        return CONVERT_NUMBER(allBLOG)

    @property
    def deactivateBLOG():
        allBLOG = BLOGList.objects.select_related('mainCat','SubCat', 'author').filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).count()
        return CONVERT_NUMBER(allBLOG)

    @property
    def deletedBLOG():
        allBLOG = BLOGList.objects.select_related('mainCat','SubCat', 'author').filter(is_deleted=True).count()
        return CONVERT_NUMBER(allBLOG)

    
class allBLOGCOMMENTS(models.Model):
    blog = models.ForeignKey(BLOGList, on_delete=models.CASCADE)
    user = models.ForeignKey(AdminRegistration, related_name="users", on_delete=models.CASCADE)
    description = models.TextField(max_length=6000 , blank=True, null=True)
    count_reply = models.IntegerField(default=0)
    like = models.IntegerField(blank=True, null=True, default=0)
    
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)


class replyBLOGCOMMENTS(models.Model):
    comment = models.ForeignKey(allBLOGCOMMENTS, on_delete=models.CASCADE)
    author = models.ForeignKey(AdminRegistration, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000 , blank=True, null=True)
    like = models.IntegerField(blank=True, null=True, default=0)

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

class replyCHILDBLOGCOMMENTS(models.Model):
    comment = models.ForeignKey(replyBLOGCOMMENTS, on_delete=models.CASCADE)
    author = models.ForeignKey(AdminRegistration, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000 , blank=True, null=True)
    like = models.IntegerField(blank=True, null=True, default=0)

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

