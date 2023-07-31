from itertools import product
from django import template
from django.shortcuts import render
from requests import request
from SALESManager.models import ProductOrderList
from PRODUCTManager.models import OfferList , ProductList

register = template.Library()
# ============RetailerMainCategory================
# ============RetailerMainCategory================
# ============RetailerMainCategory================
# ============RetailerMainCategory================
# ============RetailerMainCategory================
# ============RetailerMainCategory================
# ============RetailerMainCategory================
# ============RetailerMainCategory================
# ============RetailerMainCategory================
# ============RetailerMainCategory================
# ============RetailerMainCategory================
# ============RetailerMainCategory================


# ============Product COMMON FEATURES================
# ============Product COMMON FEATURES================
# ============Product COMMON FEATURES================ 
# ============Product COMMON FEATURES================
# ============Product COMMON FEATURES================
# ============Product COMMON FEATURES================ 
# 
@register.simple_tag
def LiveProducts():
    return ProductList.objects.filter(is_closed=False, is_ban=False, status=1, draft=1).count()

@register.simple_tag
def TopTrendingProducts():
    return ProductList.objects.filter(is_trending=True).count()

@register.simple_tag
def TopSellingProducts():
    return ProductList.objects.filter(is_top_selling=True).count()

@register.simple_tag
def BestOfferProducts(status=0):
    return ProductList.objects.filter(is_best_offer=True).count()

# ============RetailerSubCategory================
# ============RetailerSubCategory================
# ============RetailerSubCategory================
# ============RetailerSubCategory================
# ============RetailerSubCategory================
# ============RetailerSubCategory================
# ============RetailerSubCategory================
# ============RetailerSubCategory================
# ============RetailerSubCategory================
# ============RetailerSubCategory================
# ============RetailerSubCategory================
# ============RetailerSubCategory================

# ============RetailerProducts================
# ============RetailerProducts================
# ============RetailerProducts================
# ============RetailerProducts================
# ============RetailerProducts================
# ============RetailerProducts================
# ============RetailerProducts================
# ============RetailerProducts================
# ============RetailerProducts================
# ============RetailerProducts================
# ============RetailerProducts================
# ============RetailerProducts================
@register.simple_tag
def allProducts():
    return ProductList.objects.all().count()

@register.simple_tag
def draftProducts():
    return ProductList.objects.filter(status=0, draft=0, is_ban=False, is_closed=False).count()

@register.simple_tag
def activeProducts():
    return ProductList.objects.filter(status=1, draft=1, is_ban=False, is_closed=False).count()

@register.simple_tag
def deactiveProducts():
    return ProductList.objects.filter(status=1, draft=1, is_ban=False, is_closed=True).count()


@register.simple_tag
def banProducts(status=0):
    return ProductList.objects.filter(status=1, draft=1, is_closed=True, is_ban=True).count()

@register.simple_tag
def closedProducts(status=0):
    return ProductList.objects.filter(status=1, draft=1, is_closed=True, is_ban=False).count()

