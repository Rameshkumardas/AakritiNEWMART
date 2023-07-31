from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from CATEGORYManager.models import MainCategory, SubSubCategory
from PRODUCTManager.models import ProductList, ProductRatting
from django.contrib import messages
from ExtraSettings.models import  Disclaimer, TermCondition,PrivacyPolicy,CopyrightPolicy, AboutUS, HowitWorks, Security
# from CommonModules.models import BANNERLists
# ==============================================================================
# ALL PRODUCT LIST
# ==============================================================================
def allProductList(request):
    if (request.GET.get('cat_id')):
        productList = ProductList.objects.filter(is_active=True, is_verified=True, SubSubCat_id=request.GET.get('cat_id')).all()
    elif (request.GET.get('loadPorudct') == 'Short by Oldest'):
        productList = ProductList.objects.filter(is_active=True, is_verified=True).order_by('id').all()

    elif (request.GET.get('loadPorudct') == 'Short by Latest'):
        productList = ProductList.objects.filter(is_active=True, is_verified=True).order_by('-id').all()

    elif (request.GET.get('loadPorudct') == 'Short by Name'):
        productList = ProductList.objects.filter(is_active=True, is_verified=True).order_by('name').all()

    elif (request.GET.get('loadPorudct') == 'Short by Price'):
        productList = ProductList.objects.filter(is_active=True, is_verified=True).order_by('sp').all()

    elif (request.GET.get('loadPorudct') == 'Best Offers'):
        productList = ProductList.objects.filter(is_active=True, is_verified=True, is_best_offer=True).all()

    elif (request.GET.get('loadPorudct') == 'Today Deals'):
        productList = ProductList.objects.filter(is_active=True, is_verified=True, is_today_seals=True).all()
    else:
        productList = ProductList.objects.filter(is_active=True, is_verified=True).all()
        
    context = {
        'SubSubCatList': SubSubCategory.objects.filter(is_active=True).all().exclude(pk=request.GET.get('cat_id')),
        'ProductList': productList,
        'resultCount': productList.count(),

    }
    return render(request,"./template/product/productList.html", context)
# ==============================================================================
# VIEW PRODUCT
# ==============================================================================
def VIEWProduct(request, slug):
    try:
        product = ProductList.objects.get(slug=slug)
        saveAmount = product.mrp - product.sp        
        product.views = product.views+1
        product.save()
        Feedbacks = ProductRatting.objects.filter(product_id=product.pk)
        totalReview = ProductRatting.objects.filter(product_id=product.pk).count()
        print(totalReview)
        context = {
            'RecentlyViewedProductList':ProductList.objects.filter(is_active=True).exclude(pk=product.pk)[:5],
            'product': product,
            'totalReview':totalReview,
            'Feedbacks':Feedbacks,
            'saveAmount':saveAmount,
        }
        return render(request,"./template/product/productVIEW.html", context)
    except ProductList.DoesNotExist:
        return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================================
# WOMEN'S AND CHILDREN'S FOUNDATION TERM AND CONDITION
# ==============================================================================