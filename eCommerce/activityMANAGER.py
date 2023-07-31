from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from AdminAuthentication.models import  AdminRegistration
from Accounts.models import billingADDRESS, shippingADDRESS

from CATEGORYManager.models import MainCategory
from PRODUCTManager.models import ProductList, ProductMyCart, ProductMyWishlist
from SALESManager.shippingGST import getGST, getSHIPPING
from django.contrib import messages
from ExtraSettings.models import  Disclaimer, TermCondition,PrivacyPolicy,CopyrightPolicy, AboutUS, HowitWorks, Security
from CommonModules.models import COLORList
# ==============================================================================
# ALL PRODUCT LIST
# ==============================================================================

# ==============================================================================
# VIEW PRODUCT
# ==============================================================================
def CheckOut(request):
    checkoutFor = request.GET.get('checkoutFor')
    if request.session.has_key('KHANTAILORusername'):
        if (checkoutFor == 'singleProduct'):
            try:   
                slug = request.GET.get('product')
                qty = int(request.GET.get('qty'))
                product = ProductList.objects.get(slug=slug)
                ShippingTotal = 120    
                subTotal = (product.sp*qty)
                Total = subTotal+ShippingTotal
                discount = (product.mrp*qty) - (product.sp*qty)

                
                if not ProductMyCart.objects.filter(user_id=request.user.pk, product_id=product.pk).exists():
                    ProductMyCart.objects.create(user_id=request.user.pk, product_id=product.pk)

                context = {                                
                    'shippings':shippingADDRESS.objects.filter(user_id=request.user.pk),
                    'billings':billingADDRESS.objects.filter(user_id=request.user.pk),
                    'product': product,
                    'subTotal': subTotal,
                    'ShippingTotal': ShippingTotal,
                    'total': float(Total),
                    'discount': discount,
                    'user': AdminRegistration.objects.get(pk=request.user.pk),
                }
                return render(request,"./template/activity/checkout.html", context)
            except Exception as e:
                print("eeeeeeeeeeeeeeee",e)
                messages.error(request, f'{e} Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        elif (checkoutFor == 'myCartList'):
            try:    
                CartList = ProductMyCart.objects.filter(user_id=request.user.pk)                
                SubTotal = []
                grandSHIPING = []
                grandGST = []
                grandDISCOUNT = []
                for cart in CartList:
                    SubTotal.append((cart.product.sp)*int(cart.qty))
                    totalSHIPPING = 120  
                    totalGST = 120
                    grandSHIPING.append(totalSHIPPING)            
                    grandGST.append(totalGST)
                    grandDISCOUNT.append(((cart.product.mrp)*int(cart.qty))-((cart.product.sp)*int(cart.qty)))
                
                context = {                                
                    'shippings':shippingADDRESS.objects.filter(user_id=request.user.pk),
                    'billings':billingADDRESS.objects.filter(user_id=request.user.pk),
                    'CartList': CartList,
                    'subTotal': sum(SubTotal),
                    'ShippingTotal': sum(grandSHIPING),
                    'total': sum(SubTotal+grandSHIPING),
                    'discount': sum(grandDISCOUNT),
                    'user': AdminRegistration.objects.get(pk=request.user.pk),
                }
                return render(request,"./template/activity/checkout.html", context)
            except Exception as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
    else:
        try:
            slug = request.GET.get('product')
            qty = int(request.GET.get('qty'))
            if qty !=None and  qty!='':
                qty = qty
            else:
                qty=1

            product = ProductList.objects.get(slug=slug)
            
            ShippingTotal = 120            
            subTotal = (product.sp*qty)
            Total = subTotal+ShippingTotal
            discount = product.mrp*qty - product.sp*qty
            context = {

                'product': product,
                'subTotal': subTotal,
                'ShippingTotal': ShippingTotal,
                'total': Total,
                'discount': discount,
            }
            return render(request,"./template/activity/checkout.html", context)
        except Exception as e:
            messages.error(request, f'SORRY: {e}')
            return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================================
# WOMEN'S AND CHILDREN'S FOUNDATION TERM AND CONDITION
# ==============================================================================
# ==============================================================================
# VIEW PRODUCT
# ==============================================================================
def OrderConfirm(request, orderId):
    if request.session.has_key('KHANTAILORusername') and request.session.has_key('KHANTAILORpassword') and request.session.has_key('KHANTAILORrole')and request.session.has_key('KHANTAILORUser'):
            try:    
                # slug = request.GET.get('product')
                # product = ProductList.objects.get(is_active=True, slug=slug)
                # subTotal = product.sp       
                # GSTTotal = product.sp
                # ShippingTotal = product.sp
                # Total = subTotal+ShippingTotal                   
                # discount = product.mrp - product.sp 
                # context = {                                
                #     'shippings':shippingADDRESS.objects.filter(user_id=request.user.pk),
                #     'billings':billingADDRESS.objects.filter(user_id=request.user.pk),
                #     'product': product,
                #     'subTotal': subTotal,
                #     'GSTTotal': GSTTotal,
                #     'ShippingTotal': ShippingTotal,
                #     'total': Total,
                #     'discount': discount,
                #     'user': AdminRegistration.objects.get(pk=request.user.pk),
                # }
                return render(request,"./template/activity/orderConfirm.html",)
            except Exception as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, f'Register Account & Login First')
        return redirect(request.META.get('HTTP_REFERER'))
