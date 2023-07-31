from django.shortcuts import render, redirect
from PRODUCTManager.models import ProductRatting
from django.http import Http404

def OneStar(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session['ADMIN-ROLE']==1:
            Products = ProductRatting.objects.filter(Ratting=1)
            context = {
                    'AllProducts':'menu-open', 
                    'productRatting': 'active',
                    'OneStar': '1',

                    'Products':Products
            }
            return render(request,"./template/ratting/ProductRatting.html", context)
        else: 
            raise Http404
    else:
        raise Http404

def TwoStar(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session['ADMIN-ROLE']==1:
            Products = ProductRatting.objects.filter(Ratting=2)
            context = {
                    'AllProducts':'menu-open', 
                    'productRatting': 'active',
                    'TwoStar': '1',
                    'Products':Products
            }
            return render(request,"./template/ratting/ProductRatting.html", context)
        else:
            raise Http404
    else:
        raise Http404

def ThreeStar(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session['ADMIN-ROLE']==1:
            Products = ProductRatting.objects.filter(Ratting=3)
            context = {
                    'AllProducts':'menu-open', 
                    'productRatting': 'active',
                    'ThreeStar': '3',

                    'Products':Products
            }
            return render(request,"./template/ratting/ProductRatting.html", context)
        else:
            raise Http404
    else:
        raise Http404

def FourStar(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session['ADMIN-ROLE']==1:
            Products = ProductRatting.objects.filter(Ratting=4)
            context = {
                
                    'AllProducts':'menu-open', 
                    'productRatting': 'active',
                    'FourStar': '4',

                    'Products':Products
            }
            return render(request,"./template/ratting/ProductRatting.html", context)
        else:
            raise Http404
    else:
        raise Http404

def FiveStar(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session['ADMIN-ROLE']==1:
            Products = ProductRatting.objects.filter(Ratting=5)
            context = {
                    'AllProducts':'menu-open', 
                    'productRatting': 'active',
                    'FiveStar':'3',
                    'Products':Products
            }
            return render(request,"./template/ratting/ProductRatting.html", context)
        else:
            raise Http404
    else:
        raise Http404
    