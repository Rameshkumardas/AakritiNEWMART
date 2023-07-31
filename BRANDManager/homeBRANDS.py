from BRANDManager.models import BRANDList
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

def BRAND(request, slug=None):
    try:
        BRAND = BRANDList.objects.get(slug=slug)
        
        BRAND.views = BRAND.views +1
        BRAND.save()

        context = {
            'dashboard':'menu-open', 
            'default': 'active',
            'brand':BRAND,
        }
        return render(request,"./template/BRAND/home/views.html", context )
    except Exception as e:
        print(e)
        return redirect(request.META.get('HTTP_REFERER'))
