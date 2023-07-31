from AdminAuthentication.decorators import accountant_required, admin_required, superadmin_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import Http404
from SALESManager.models import ProductOrderList
import datetime

@method_decorator(superadmin_required, name='dispatch')
class ALLORDERList(ListView):
    paginate_by = 10
    context_object_name = 'ORDERList'
    template_name = './template/orders/orderSTATUS.html'
    ordering = ['id']    
    extra_context = { 'SALESManager':'menu-open', 'allORDERS': 'active'}
    def get_queryset(self, *args, **kwargs):
        is_confirmed = self.request.GET.get('is_confirmed', 'is_confirmed')
        is_shipped = self.request.GET.get('is_shipped', 'is_shipped')
        is_delivered = self.request.GET.get('is_delivered', 'is_delivered')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')        
        if is_confirmed == 'True':
            return ProductOrderList.objects.select_related('product', 'user').filter(is_confirmed=True).exclude(is_shipped=True).exclude(is_deleted=True).order_by('-date')
        elif is_shipped == 'True':
            return ProductOrderList.objects.select_related('product', 'user').filter(is_delivered=False, is_shipped=True, is_confirmed=True)
        elif is_delivered == 'True':
            return ProductOrderList.objects.select_related('product', 'user').filter(is_delivered=True, is_shipped=True, is_confirmed=False)
        elif is_deleted == 'True':
            return ProductOrderList.objects.select_related('product', 'user').filter(is_deleted=True)
        else:
            return ProductOrderList.objects.select_related('product', 'user').all()

    def get_paginate_by(self, queryset):
        filter = self.request.GET.get('filter')
        if filter:
            return self.request.GET.get("paginate_by", filter)
        else:            
            return self.request.GET.get("paginate_by", self.paginate_by)


@accountant_required
def productINVOICE(request, orderId, user, pk):
    try:
        order = ProductOrderList.objects.get(pk=pk)                 
        orderProducts = ProductOrderList.objects.filter(orderId=orderId, user_id=user)      
        subTotal = sum([item.amount for item in orderProducts])
        # GSTTotal = sum([item.gst for item in orderProducts])
        ShippingTotal = 120
        Total = subTotal+ShippingTotal           
        context = {
                'AllProducts':'menu-open', 
                'allProduct': 'active',
                'subTotal': subTotal,
                # 'GSTTotal': GSTTotal,
                'ShippingTotal': ShippingTotal,
                'Total': Total,
                'order': order,
                'today':datetime.datetime.now().strftime("%d, %b - %Y  (%I:%M %p) "),
                'orderId':orderId,
                'orders': orderProducts,
        }
        return render(request,"./template/invoice/productINVOICE.html", context)
    except ProductOrderList.DoesNotExist:
        raise Http404                               

def productINVOICEFORUser(request, orderId, user, pk=None):
    try:
        order = ProductOrderList.objects.get(pk=pk)                 
        orderProducts = ProductOrderList.objects.filter(orderId=orderId, user=user)      
        subTotal = sum([item.amount for item in orderProducts])
        GSTTotal = sum([item.gst for item in orderProducts])
        ShippingTotal = sum([item.shipping for item in orderProducts])
        Total = subTotal+GSTTotal+ShippingTotal           
        context = {
                'AllProducts':'menu-open', 
                'allProduct': 'active',
                'subTotal': subTotal,
                'GSTTotal': GSTTotal,
                'ShippingTotal': ShippingTotal,
                'Total': Total,
                'order': order,
                'today':datetime.datetime.now().strftime("%d, %b - %Y  (%I:%M %p) "),
                'orderId':orderId,
                'orders': orderProducts,
        }
        return render(request,"./template/invoice/productINVOICEFORUSER.html", context)
    except ProductOrderList.DoesNotExist:
        raise Http404                               
