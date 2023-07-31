from AdminAuthentication.models import AdminRegistration
from PRODUCTManager.models import ProductList
from django.db import models
import datetime

class PaymentGatewayList(models.Model):
    private_key = models.CharField(max_length=225, null=True, blank=True)
    secret_key = models.CharField(max_length=225, null=True, blank=True)
    is_agree = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    otp = models.IntegerField(null=False, blank=False)
    author = models.CharField(max_length=225, null=True, blank=True, default='Super Admin')
    date = models.DateTimeField(auto_now_add=False,null=True, blank=True)    
    last_update = models.CharField(max_length=20, blank=True, null=True, default=datetime.datetime.now().strftime("%d, %B - %Y"))
 
class Transactions(models.Model):
    user = models.ForeignKey(AdminRegistration, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True)
    method = models.CharField(max_length=225, null=True, blank=True)
    pay_status = models.CharField(max_length=225, null=True, blank=True, default='')
    tno = models.CharField(max_length=225, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=False,null=True, blank=True)    

class ProductOrderList(models.Model):
    user = models.ForeignKey(AdminRegistration, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductList, null=False, blank=False, on_delete=models.CASCADE)
    orderId = models.CharField(max_length=225, null=False, blank=False)

    invoice = models.CharField(max_length=225, null=False, blank=False)
    
    amount = models.FloatField()
    gst = models.FloatField(null=False, blank=False, default=1)
    shipping = models.FloatField(null=False, blank=False, default=1)
    discount = models.FloatField()
    subtotal = models.FloatField(null=False, blank=False, default=1)    
    total = models.FloatField(null=False, blank=False, default=1)    
    
    qty = models.IntegerField(null=False, blank=False, default=1)    
    color = models.CharField(max_length=225, null=False, blank=False)
    attribute = models.CharField(max_length=225, null=False, blank=False)


    scode = models.IntegerField(blank=True, null=True, default='')
    shouse_no = models.CharField(max_length=255, blank=True, null=True, default='')
    slandmark = models.CharField(max_length=500, blank=True, null=True, default='')
    scolony = models.CharField(max_length=500, blank=True, null=True, default='')
    scity = models.CharField(max_length=255, blank=True, null=True, default='')
    sstate = models.CharField(max_length=255, blank=True, null=True, default='')
    scountry = models.CharField(max_length=255, blank=True, null=True, default='')
    more = models.CharField(max_length=255, blank=True, null=True, default='')
    
    bcode = models.IntegerField(blank=True, null=True, default='')
    bhouse_no = models.CharField(max_length=255, blank=True, null=True, default='')
    blandmark = models.CharField(max_length=500, blank=True, null=True, default='')
    bcolony = models.CharField(max_length=500, blank=True, null=True, default='')
    bcity = models.CharField(max_length=255, blank=True, null=True, default='')
    bstate = models.CharField(max_length=255, blank=True, null=True, default='')
    bcountry = models.CharField(max_length=255, blank=True, null=True, default='')
    more = models.CharField(max_length=255, blank=True, null=True, default='')

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
