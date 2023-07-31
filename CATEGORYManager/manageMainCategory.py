from django.contrib.auth.decorators import login_required
from AdminAuthentication.decorators import accountant_required, superadmin_required
from AdminAuthentication.models import AdminRegistration
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ExtraSettings.models import PROJECTInformation
from .models import MainCategory
from django.http import Http404, JsonResponse
import datetime
from django.db.models import Q

import random
# ==============================================================================
# CREATE MAIN CATEGORY  
# ==============================================================================
@accountant_required
def CreateMainCategory(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            q = request.GET.get('search')
            if q:
                posts_list = MainCategory.objects.filter(Q(name__icontains=q))
            else:
                posts_list = MainCategory.objects.all()
                
                        
            if request.method=="POST":
                try:
                    if request.POST['mainCat']!='':
                        name = request.POST['mainCat']
                    else:
                        messages.error(request, 'Name Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    if request.FILES.get('img'):
                        img = request.FILES['img']
                    else:
                        img = ''
                        
                    MainCategory.objects.create(name=name, img=img)
                    messages.success(request, ' Main Category Created')
                    return redirect(request.META.get('HTTP_REFERER'))
                except Exception as e:
                    messages.error(request, f'{e}')
                    return redirect(request.META.get('HTTP_REFERER'))
            
            try:
                page = request.GET.get('page', 1)
                filter = request.GET.get('filter')
                if filter:
                    paginator = Paginator(posts_list, filter)
                else:
                    paginator = Paginator(posts_list, 5)
                mainCat = paginator.page(page)
            except PageNotAnInteger:
                mainCat = paginator.page(1)
            except EmptyPage:
                mainCat = paginator.page(paginator.num_pages)
                
            context = {
                'CATEGORYManager':'menu-open', 
                'MainCategory': 'active', 
                'mainCat':mainCat,
                
            }
            return render(request,"./template/mainCategory.html", context)
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# UPDATE MAIN CATEGORY 
# ==============================================================================
@accountant_required
def UpdateMainCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            data = MainCategory.objects.get(pk=pk)
            if request.method=="POST":
                try:
                    mainCat = MainCategory.objects.get(pk=pk)
                    if request.POST['maincatName']!='':
                        if len(request.POST['maincatName'])<50:
                            name = request.POST['maincatName']
                            newname = name.lower()
                            mainCat.name = request.POST['maincatName']
                            mainCat.slug = newname.replace(" ", "-")
                            mainCat.save()
                        else:
                            messages.error(request, 'Category Name Less 50 Char')
                            return redirect(request.META.get('HTTP_REFERER'))
                        if request.FILES['img']!='':
                            mainCat.img = request.FILES['img']
                            mainCat.last_update = datetime.date.today()
                            mainCat.save()
                            messages.success(request, 'Update successfully')
                            return redirect(request.META.get('HTTP_REFERER'))
                    else:
                        messages.error(request, 'Category Name is Empty')
                        return redirect(request.META.get('HTTP_REFERER'))
                except Exception:
                    mainCat.img = MainCategory.objects.get(pk=pk).img
                    mainCat.last_update = datetime.date.today()
                    mainCat.save()
                    messages.success(request, 'Update successfully')
                    return redirect(request.META.get('HTTP_REFERER'))
            context = {
                'CATEGORYManager':'menu-open', 
                'updateMainCat': 'active', 
                'data':data
                }
    
            return render(request,"./template/update-mainCategory.html", context)
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DELETE MAIN CATEGORY 
# ==============================================================================
@superadmin_required
def DeleteMainCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                mainCat = MainCategory.objects.get(pk=pk)
                mainCat.delete()
                messages.success(request, 'Delete successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# COPY MAIN CATEGORY 
# ==============================================================================
@accountant_required
def CopyMainCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                mainCat = MainCategory.objects.get(pk=pk)
                name ='Copy-ozymed-'+''.join((random.choice('.com') for i in range(4)))+'-'+mainCat.name
                slug  ='Copy-ozymed-'+''.join((random.choice('.com') for i in range(4)))+'-'+mainCat.slug
                img = mainCat.img
                MainCategory.objects.create(name=name, slug=slug, img=img)
                messages.success(request, 'Copy successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# ACTIVATE MAIN CATEGORY 
# ==============================================================================
@accountant_required
def ActivatedMainCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                mainCat = MainCategory.objects.get(pk=pk)
                mainCat.is_active = True
                mainCat.save()
                messages.success(request, 'Activated successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DEACTIVATED MAIN CATEGORY 
# ==============================================================================
@accountant_required
def DeactivatedMainCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                mainCat = MainCategory.objects.get(pk=pk)
                mainCat.is_active = False
                mainCat.save()
                messages.error(request, 'Deactivated successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404

# ==============================================================================
# ACTIVATE HEADER MAIN CATEGORY 
# ==============================================================================
@accountant_required
def ActiveHeaderMainCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                mainCat = MainCategory.objects.get(pk=pk)
                mainCat.is_header = True
                mainCat.save()
                messages.success(request, 'Set successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DEACTIVE HEADER MAIN CATEGORY 
# ==============================================================================
@accountant_required
def DeactiveHeaderMainCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                mainCat = MainCategory.objects.get(pk=pk)
                mainCat.is_header = False
                mainCat.save()
                messages.success(request, 'Set successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DELETE MAIN CATEGORY USING AJAX
# ==============================================================================
@superadmin_required
def DELETEMainCat(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                if request.POST.get('targetMainCat'):
                    mainCat = MainCategory.objects.get(pk=request.POST.get('targetMainCat'))
                    mainCat.delete()
                    return JsonResponse({'status':1, 'message':'Permanently Deleted Successfully', 'Reload':request.META.get('HTTP_REFERER')})
                else:
                    return JsonResponse({'status':0, 'message':'Target Required*'})
            except Exception:
                messages.error(request, 'Error Occured')
                return JsonResponse({'status':0, 'message':'BError Occured'})
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# MORE ACCTIONS
# ==============================================================================
