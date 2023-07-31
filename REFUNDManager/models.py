from django.db import models
from AdminAuthentication.models import AdminRegistration
from PRODUCTManager.models import ProductList
from SALESManager.models import ProductOrderList

# Create your models here.
class REFUNDREQUESTList(models.Model):
    user = models.ForeignKey(AdminRegistration, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductList, null=False, blank=False, on_delete=models.CASCADE)
    order = models.ForeignKey(ProductOrderList, null=False, blank=False, on_delete=models.CASCADE)
    orderId = models.CharField(max_length=225, null=False, blank=False)
    amount = models.CharField(max_length=225, null=False, blank=False)
    is_request =models.BooleanField(default=False)    

    is_draft =models.BooleanField(default=True)
    is_active =models.BooleanField(default=False)
    is_verified =models.BooleanField(default=False)
    is_deleted =models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=False,null=True, blank=True)    
    last_update = models.CharField(max_length=225, null=False, blank=False)

