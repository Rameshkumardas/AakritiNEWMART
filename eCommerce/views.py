from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from Accounts.models import shippingADDRESS
from CATEGORYManager.models import MainCategory, SubSubCategory
from PRODUCTManager.models import ProductList, ProductMyCart, ProductMyWishlist
from django.contrib import messages
from ExtraSettings.models import  Disclaimer, TermCondition,PrivacyPolicy,CopyrightPolicy, AboutUS, HowitWorks, Security
from SLIDERManager.models import BANNERCatList, BANNERList
from Accounts.access import user_login_required

# ==============================================================================
# COMPANY HOME PAGE
# ==============================================================================
def eComHome(request):
    try:
        ecommerce_id = BANNERCatList.objects.get(slug='ecommerce').pk
    except Exception:
        ecommerce_id = 1
    # is_Flash = models.BooleanField(default=False)
    # is_Best = models.BooleanField(default=False)
    # is_Arrivals = models.BooleanField(default=False)
    # is_today = models.BooleanField(default=False)
    context = {
        'SubSubCatList':SubSubCategory.objects.filter(is_active=True),
        'HOMEBANNERList': BANNERList.objects.filter(BANNERCat_id=ecommerce_id, is_active=True).order_by('-id'),
        'BestSellingProductList':ProductList.objects.filter(is_active=True, is_verified=True, is_Best=True).order_by('-views')[:10],
        'NewArrivalsProductList':ProductList.objects.filter(is_active=True, is_verified=True, is_Arrivals=True).order_by('-date')[:16],
        'ExploreProducts':ProductList.objects.filter(is_active=True, is_verified=True).order_by('-views')[:16],
        'active_this':'active',
    }
    return render(request,"./template/home/eCommerce.html", context)


@user_login_required
def cart(request):
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
        'CartList': CartList,
        'subTotal': sum(SubTotal),
        'GSTTotal': sum(grandGST),
        'ShippingTotal': sum(grandSHIPING),
        'total': sum(SubTotal),
        'discount': sum(grandDISCOUNT),
    }
    return render(request,"./template/home/mycart.html", context)

# ==============================================================================
# MY WHITELIST
# ==============================================================================
@user_login_required
def WishList(request):
    try:
        wishlist =  ProductMyWishlist.filter(user_id=request.user.pk)
        context = {
            'wishlist': wishlist,
        }
        return render(request,"./template/account/wishlist.html", context)
    except Exception:
        messages.error(request, 'Error Occured')
        return redirect(request.META.get('HTTP_REFERER'))

# ==============================================================================
# DELETE MYCART LIST
# ==============================================================================
@user_login_required
def deleteMYCARTLIST(request):
    if request.user.is_user:
        try:            
            ProductMyCart.objects.filter(user_id=request.user.pk).delete()
            messages.success(request, 'Cart Successfully Deleted')
            return redirect(request.META.get('HTTP_REFERER'))
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Register Account & Login First')
        return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================================
# DELETE SINGLE PRODUCT FROM MY CART
# ==============================================================================
@user_login_required
def deleteSINGLEPRODUCTFROMCART(request, pk):
    if request.user.is_user:
        try:            
            ProductMyCart.objects.filter(pk=pk, user_id=request.user.pk).delete()
            messages.success(request, 'Cart Successfully Deleted')
            return redirect(request.META.get('HTTP_REFERER'))
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Register Account & Login First')
        return redirect(request.META.get('HTTP_REFERER'))