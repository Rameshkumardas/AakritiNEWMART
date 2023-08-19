from AdminAuthentication.models import AdminRegistration
from PRODUCTManager.models import ProductList
from django.db import models
import datetime

class ProductOrderList(models.Model):
    user = models.ForeignKey(AdminRegistration, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductList, null=False, blank=False, on_delete=models.CASCADE)
    orderId = models.CharField(max_length=225, null=False, blank=False)

    invoice = models.CharField(max_length=225, null=False, blank=False)
    
    fname = models.CharField(max_length=225, null=False, blank=False, default='')
    lname = models.CharField(max_length=225, null=False, blank=False, default='')
    email = models.CharField(max_length=225, null=False, blank=False, default='')    
    contact = models.IntegerField(null=False, blank=False, default=0000000000)


    amount = models.FloatField()
    gst = models.FloatField(null=False, blank=False, default=1)
    shipping = models.FloatField(null=False, blank=False, default=1)
    discount = models.FloatField()
    subtotal = models.FloatField(null=False, blank=False, default=1)    
    total = models.FloatField(null=False, blank=False, default=1)    
    
    qty = models.IntegerField(null=False, blank=False, default=1)    
    color = models.CharField(max_length=225, null=False, blank=False)
    attribute = models.CharField(max_length=225, null=False, blank=False)



    code = models.IntegerField(blank=True, null=True, default='')
    house_no = models.CharField(max_length=255, blank=True, null=True, default='')
    landmark = models.CharField(max_length=500, blank=True, null=True, default='')
    colony = models.CharField(max_length=500, blank=True, null=True, default='')
    city = models.CharField(max_length=255, blank=True, null=True, default='')
    state = models.CharField(max_length=255, blank=True, null=True, default='')
    country = models.CharField(max_length=255, blank=True, null=True, default='')
    
    is_confirmed =models.BooleanField(default=True)    
    is_cancel =models.BooleanField(default=False)    
    is_shipped =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)
    is_delivered =models.BooleanField(default=False)
    
    payMethod = models.CharField(max_length=225, null=False, blank=False, default='')
    is_payment = models.BooleanField(default=False)
    is_otp = models.IntegerField(default=000000)

    track = models.CharField(max_length=225, null=False, blank=False, default="")
    

    order_id = models.CharField(max_length=225, null=True, blank=True)
    payment_id = models.CharField(max_length=225, null=True, blank=True)
    signature = models.CharField(max_length=225, null=True, blank=True)

    jsonOBJ = models.TextField(max_length=5000, null=False, blank=False, default="")    

    date = models.DateTimeField(auto_now_add=True)    
    on_delivered = models.DateTimeField(auto_now_add=True)    
