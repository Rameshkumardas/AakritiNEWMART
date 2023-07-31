from AdminAuthentication.HELPER import CONVERT_NUMBER
from AdminAuthentication.models import AdminRegistration
from CATEGORYManager.models import MainCategory, SubCategory, SubSubCategory
from CommonModules.models import COLORList
from BRANDManager.models import BRANDList
from autoslug import AutoSlugField
from datetime import datetime as dt
from datetime import datetime
from django.db import models
import datetime
from django.db.models import Avg




class ProductList(models.Model):
    author = models.ForeignKey(AdminRegistration, null=True, blank=True, on_delete=models.SET_NULL)
    mainCat = models.ForeignKey(MainCategory, null=False, blank=False, on_delete=models.CASCADE)
    subCat = models.ForeignKey(SubCategory, null=False, blank=False, on_delete=models.CASCADE)
    SubSubCat = models.ForeignKey(SubSubCategory, null=False, blank=False, on_delete=models.CASCADE)
    brand = models.ForeignKey(BRANDList, null=True, blank=True, on_delete=models.SET_NULL)
    color = models.ForeignKey(COLORList, null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=50, blank=False, null=False, default='')
    slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)        
    
    img = models.ImageField(max_length=200, upload_to="Products/ThumbnailIMG/", blank=True, null=True)
    img1 = models.ImageField(max_length=200, upload_to="Products/Items/", blank=True, null=True)
    img2 = models.ImageField(max_length=200, upload_to="Products/Items/", blank=True, null=True)
    img3 = models.ImageField(max_length=200, upload_to="Products/Items/", blank=True, null=True)
    img4 = models.ImageField(max_length=200, upload_to="Products/Items/", blank=True, null=True)

    dimension = models.CharField(max_length=200, default='')
    length = models.FloatField(blank=False, null=False,default=1)
    width = models.FloatField(blank=False, null=False,default=1)
    hight = models.FloatField(blank=False, null=False,default=1)

    weight = models.FloatField(blank=False, null=False,default=1)


    mrp = models.FloatField(blank=False, null=False, default=0.0)
    sp = models.FloatField(blank=False, null=False, default=0.0)
    
    total_qty = models.IntegerField(default=50)
    low_stock_warning = models.IntegerField(default=50)

    HSNCode = models.CharField(max_length=100, blank=True, null=True, default='')  
    igst = models.FloatField(blank=True, null=True, default=18.0)
    cgst = models.FloatField(blank=True, null=True, default=9.0)
    sgst = models.FloatField(blank=True, null=True, default=9.0)
 

    is_cash_on_delivery = models.BooleanField(default=True)

    is_refundable = models.BooleanField(default=True)
    description = models.TextField(max_length=500, blank=False, null=False, default="This Product will refundable within 7 Days")  

    is_draft = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_out_of_stock = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    
    label = models.CharField(max_length=100, blank=True, null=True, default="")

    is_arrivals = models.BooleanField(default=False)
    is_deal = models.BooleanField(default=False)

    is_trending = models.BooleanField(default=False)

    is_trending_new = models.BooleanField(default=False)
    is_trending_featured = models.BooleanField(default=False)
    is_trending_top_sale = models.BooleanField(default=False)

    is_discount = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_selling = models.BooleanField(default=False)

    views = models.IntegerField(blank=True, null=True, default=0)
    likes = models.IntegerField(blank=True, null=True, default=0)
    
    review = models.IntegerField(blank=False, null=False, default=0)  
    ratting = models.IntegerField(blank=False, null=False, default=0)  
    
    meta_title = models.CharField(max_length=100, blank=False, null=False, default='')  
    meta_tags = models.CharField(max_length=100, blank=False, null=False, default='')  
    meta_description = models.TextField(max_length=2000, blank=False, null=False, default='')  
    meta_img = models.ImageField(max_length=200, upload_to="Products/MetaIMG/", blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_view_count(self, *args, **kwargs):
        return CONVERT_NUMBER(self.views)

    @property
    def get_like_count(self, *args, **kwargs):
        return CONVERT_NUMBER(self.likes)
    
    
    @property
    def allPRODUCT():
        return CONVERT_NUMBER(ProductList.objects.filter(is_draft=True).exclude(is_deleted=True).count())

    # is_arrivals
    # is_deal
    # is_selling
    # is_discount
    # is_featured
    # is_trending
   
    @classmethod
    def all_product_rows(self, *args, **kwargs):
        return ProductList.objects.select_related('mainCat', 'subCat', 'SubSubCat', 'brand', 'color').filter(is_active=True, is_verified=True).exclude(is_deleted=True)


    @classmethod
    def new_arrivals_20_rows(self, *args, **kwargs):
        return ProductList.objects.select_related('SubSubCat').filter(is_active=True, is_verified=True, is_arrivals=True).exclude(is_deleted=True)[:20]

    # , 'subCat', 'SubSubCat', 'brand', 'color'

    @classmethod
    def trending_new_20_rows(self, *args, **kwargs):
        return ProductList.objects.select_related('author', 'mainCat', 'subCat', 'SubSubCat', 'brand', 'color').filter(is_active=True, is_verified=True, is_trending=True, is_trending_new=True).exclude(is_deleted=True)[:20]

    @classmethod
    def trending_featured_20_rows(self, *args, **kwargs):
        return ProductList.objects.select_related('author', 'mainCat', 'subCat', 'SubSubCat', 'brand', 'color').filter(is_active=True, is_verified=True, is_trending=True, is_trending_featured=True).exclude(is_deleted=True)[:20]

    @classmethod
    def trending_top_sale_20_rows(self, *args, **kwargs):
        return ProductList.objects.select_related('author', 'mainCat', 'subCat', 'SubSubCat', 'brand', 'color').filter(is_active=True, is_verified=True, is_trending=True, is_trending_top_sale=True).exclude(is_deleted=True)[:20]

    @classmethod
    def deal_20_rows(self, *args, **kwargs):
        return ProductList.objects.select_related('author', 'mainCat', 'subCat', 'SubSubCat', 'brand', 'color').filter(is_active=True, is_verified=True, is_deal=True).exclude(is_deleted=True)[:20]

    @classmethod
    def discount_20_rows(self, *args, **kwargs):
        return ProductList.objects.select_related('author', 'mainCat', 'subCat', 'SubSubCat', 'brand', 'color').filter(is_active=True, is_verified=True, is_discount=True).exclude(is_deleted=True)[:20]

    @classmethod
    def featured_20_rows(self, *args, **kwargs):
        return ProductList.objects.select_related('author', 'mainCat', 'subCat', 'SubSubCat', 'brand', 'color').filter(is_active=True, is_verified=True, is_featured=True).exclude(is_deleted=True)[:20]

    @classmethod
    def selling_20_rows(self, *args, **kwargs):
        return ProductList.objects.select_related('author', 'mainCat', 'subCat', 'SubSubCat', 'brand', 'color').filter(is_active=True, is_verified=True, is_selling=True).exclude(is_deleted=True)[:20]


class ATTRIBUTEProductList(models.Model):
    product = models.ForeignKey(ProductList, null=True, blank=True, on_delete=models.CASCADE, db_constraint=True)
    color = models.ForeignKey(COLORList, null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=50, blank=False, null=False, default='')
    slug = AutoSlugField(populate_from='name', unique=True, max_length=250 )

    img = models.ImageField(max_length=200, upload_to="Products/ThumbnailIMG/", blank=True, null=True)
    img1 = models.ImageField(max_length=200, upload_to="Products/Items/", blank=True, null=True)
    img2 = models.ImageField(max_length=200, upload_to="Products/Items/", blank=True, null=True)
    img3 = models.ImageField(max_length=200, upload_to="Products/Items/", blank=True, null=True)
    img4 = models.ImageField(max_length=200, upload_to="Products/Items/", blank=True, null=True)

    mrp = models.FloatField(blank=False, null=False, default=0.0)
    sp = models.FloatField(blank=False, null=False, default=0.0)
    
    total_qty = models.IntegerField(default=50)
    low_stock_warning = models.IntegerField(default=50)

    is_draft = models.BooleanField(default=False)
    is_ban = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    
    is_today_seals = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    is_top_selling = models.BooleanField(default=False)
    is_best_offer = models.BooleanField(default=False)

    views = models.IntegerField(blank=True, null=True, default=0)
    likes = models.IntegerField(blank=True, null=True, default=0)
    
    review = models.IntegerField(blank=False, null=False, default=0)  
    ratting = models.IntegerField(blank=False, null=False, default=0)  

    
    meta_title = models.CharField(max_length=100, blank=False, null=False, default='')  
    meta_tags = models.CharField(max_length=100, blank=False, null=False, default='')  
    meta_description = models.TextField(max_length=2000, blank=False, null=False, default='')  
    meta_img = models.ImageField(max_length=200, upload_to="Products/MetaIMG/", blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)




class ProductRatting(models.Model):
    product = models.ForeignKey(ProductList, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(AdminRegistration, on_delete=models.CASCADE, related_name="RattingUser")
    Ratting = models.IntegerField(blank=False, null=False)  
    message = models.CharField(max_length=100, blank=False, null=False)  
    date = models.DateTimeField(auto_now_add=True)




class PRODUCTQList(models.Model):
    product = models.ForeignKey(ProductList, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(AdminRegistration, on_delete=models.CASCADE, related_name="QUESTIONUSER")
    message = models.CharField(max_length=100, blank=False, null=False)  
    date = models.DateTimeField(auto_now_add=True)
    
class PRODUCTAList(models.Model):
    q = models.ForeignKey(PRODUCTQList, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(AdminRegistration, on_delete=models.CASCADE, related_name="ANSWERUSER")
    message = models.CharField(max_length=100, blank=False, null=False)  
    date = models.DateTimeField(auto_now_add=True)


class ProductMyCart(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE, related_name="MyCartProduct")
    user = models.ForeignKey(AdminRegistration, on_delete=models.CASCADE, related_name="MyCartUser")
    qty = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

class ProductMyWishlist(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE, related_name="MyWishlist")
    user = models.ForeignKey(AdminRegistration, on_delete=models.CASCADE, related_name="MyWishlisttUser")
    date = models.DateTimeField(auto_now_add=True)   
     
class COMPAREProducts(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE, related_name="COMPAREProducts")
    user = models.ForeignKey(AdminRegistration, on_delete=models.CASCADE, related_name="Users")
    date = models.DateTimeField(auto_now_add=True)

class ProductRecentViews(models.Model):
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE, related_name="RecentViews")
    user = models.ForeignKey(AdminRegistration, on_delete=models.CASCADE, related_name="RecentViewUser")
    date = models.DateTimeField(auto_now_add=True)

class OfferList(models.Model):
    product = models.ForeignKey(ProductList, null=True, blank=True, on_delete=models.CASCADE)
    Code = models.CharField(max_length=100, blank=False, null=False)  
    offerType = models.CharField(max_length=100, blank=False, null=False)  
    offer = models.IntegerField(blank=False, null=False, default=18)
    start_date = models.CharField(max_length=15, null=True, blank=True, default=datetime.datetime.now().strftime("%d %b, %Y"))
    end_date = models.CharField(max_length=15, null=True, blank=True, default=datetime.datetime.now().strftime("%d %b, %Y"))
    is_active = models.BooleanField(default=True)
    

