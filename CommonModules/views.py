from AdminAuthentication.decorators import accountant_required, admin_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from CommonModules.models import  COLORList, REGIONList, SHIPPINGList
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
# ==============================================================================
# COLOR SETTING => CREATE NEW COLOR
# ==============================================================================  
@admin_required
def COLORManager(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            q = request.GET.get('search')
            if q:
                posts_list = COLORList.objects.filter(Q(name__icontains=q))
            else:
                posts_list = COLORList.objects.all()
            try:
                page = request.GET.get('page', 1)
                filter = request.GET.get('filter')
                if filter:
                    paginator = Paginator(posts_list, filter)
                else:
                    paginator = Paginator(posts_list, 5)
                allCOLORS = paginator.page(page)
            except PageNotAnInteger:
                allCOLORS = paginator.page(1)
            except EmptyPage:
                allCOLORS = paginator.page(paginator.num_pages)

            context = {
                    'CommonModules':'menu-open', 
                    'COLORManager': 'active', 
                    'allCOLORS':allCOLORS,
            }
            return render(request,"./template/color/COLORManager.html", context)
        else:
            messages.error(request, 'You Dont Have Acceess')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You Dont Have Acceess')
        return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================================
# COLOR SETTING =>  UPDATE COLOR
# ==============================================================================
@admin_required  
def updateCOLOR(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            allCOLORS = COLORList.objects.all()
            color = COLORList.objects.get(pk=pk)
            context = {
                    'CommonModules':'menu-open', 
                    'COLORManager': 'active', 
                    'allCOLORS':allCOLORS,
                    'color':color,
            }
            return render(request, './template/color/updateCOLOR.html', context)  
        else:
            messages.error(request, 'You Dont Have Acceess')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You Dont Have Acceess')
        return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================================
# COLOR SETTING =>  MORE COLOR
# ==============================================================================  
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------









# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# ==============================================================================
# RGION SETTING => CREATE NEW RGION
# ==============================================================================  
@admin_required
def REGIONList1(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            q = request.GET.get('search')
            if q:
                posts_list = REGIONList.objects.filter(Q(name__icontains=q))
            else:
                posts_list = REGIONList.objects.all()
            try:
                page = request.GET.get('page', 1)
                filter = request.GET.get('filter')
                if filter:
                    paginator = Paginator(posts_list, filter)
                else:
                    paginator = Paginator(posts_list, 5)
                AllRegionList = paginator.page(page)
            except PageNotAnInteger:
                AllRegionList = paginator.page(1)
            except EmptyPage:
                AllRegionList = paginator.page(paginator.num_pages)



            context = {
                'CommonModules':'menu-open', 
                'REGIONManage': 'active', 
                'AllRegionList':AllRegionList,
            }
            return render(request,"./template/region/REGIONManager.html", context)
        else:
            messages.error(request, 'You Dont Have Acceess')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You Dont Have Acceess')
        return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================================
# RGION SETTING =>  UPDATE RGION
# ==============================================================================  
@admin_required
def updateREGION(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            Region = REGIONList.objects.get(pk=pk)
            AllRegionList = REGIONList.objects.all().exclude(pk=pk)
            context = {
                'CommonModules':'menu-open', 
                'REGIONManage': 'active', 
                'AllRegionList':AllRegionList,
                'Region':Region,
            }
            return render(request,"./template/region/updateREGION.html", context)
        else:
            messages.error(request, 'You Dont Have Acceess')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You Dont Have Acceess')
        return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================================
# RGION SETTING =>  MORE RGION
# ==============================================================================  
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------








# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# ==============================================================================
# RGION SETTING => CREATE NEW RGION
# ==============================================================================  
@admin_required
def SHIPPINGList1(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            posts_list = SHIPPINGList.objects.all()
            try:
                page = request.GET.get('page', 1)
                filter = request.GET.get('filter')
                if filter:
                    paginator = Paginator(posts_list, filter)
                else:
                    paginator = Paginator(posts_list, 5)
                AllShippingList = paginator.page(page)
            except PageNotAnInteger:
                AllShippingList = paginator.page(1)
            except EmptyPage:
                AllShippingList = paginator.page(paginator.num_pages)

            context = {
                'CommonModules':'menu-open', 
                'SHIPPINGManage': 'active', 
                'AllShippingList':AllShippingList,
            }
            return render(request,"./template/shipping/shippingMANAGER.html", context)
        else:
            messages.error(request, 'You Dont Have Acceess')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You Dont Have Acceess')
        return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================================
# RGION SETTING =>  UPDATE RGION
# ==============================================================================  
@admin_required
def updateSHIPPING(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            Region = SHIPPINGList.objects.get(pk=pk)
            AllRegionList = SHIPPINGList.objects.all().exclude(pk=pk)
            context = {
                'CommonModules':'menu-open', 
                'SHIPPINGManage': 'active', 
                'AllRegionList':AllRegionList,
                'Region':Region,
            }
            return render(request,"./template/region/shippingMANAGER.html", context)
        else:
            messages.error(request, 'You Dont Have Acceess')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'You Dont Have Acceess')
        return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================================
# RGION SETTING =>  MORE RGION
# ==============================================================================  
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------




