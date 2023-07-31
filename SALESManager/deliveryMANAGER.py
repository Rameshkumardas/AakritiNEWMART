from SALESManager.models import ProductOrderList
from PRODUCTManager.models import ProductList
from django.http import Http404
from django.shortcuts import render, redirect
from AdminAuthentication.models import AdminRegistration
from django.contrib import messages
import random

# Create your views here.
def productDelivered(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            Products = ProductOrderList.objects.all()
            context = {
                    'AllProducts':'menu-open', 
                    'delivery': 'active',
                    'Products':Products,
                    'OrderStatus':1,
            }
            return render(request,"./template/delivery/orderSTATUS.html", context)
        else:
            raise Http404
    else:
        raise Http404
    
def replacementORDER(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            Products = ProductOrderList.objects.all()
            context = {
                    'AllProducts':'menu-open', 
                    'delivery': 'active',
                    'Products':Products,
                    'OrderReplacement':1
            }
            return render(request,"./template/delivery/orderSTATUS.html", context)
        else:
            raise Http404
    else:
        raise Http404

def cancelORDER(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            Products = ProductOrderList.objects.all()
            context = {
                    'AllProducts':'menu-open', 
                    'delivery': 'active',
                    'Products':Products,
                    'OrderCancelandReturn':1
            }
            return render(request,"./template/delivery/orderSTATUS.html", context)
        else:
            raise Http404
    else:
        raise Http404
