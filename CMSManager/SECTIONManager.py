from AdminAuthentication.decorators import accountant_required, superadmin_required 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from AdminAuthentication.models import AdminActivity
from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import urlencode
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
from .models import SECTIONList
import random
# ==============================================================================
# CREATE SERVICE MAIN CATEGORY
# ==============================================================================
@accountant_required
def CreateSECTION(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            q = request.GET.get('search')
            if q:
                posts_list = SECTIONList.objects.filter(Q(name__icontains=q)).order_by('-id')
            else:
                posts_list = SECTIONList.objects.all().order_by('-last_update')
                
            if request.method=="POST":
                try:
                    if request.POST['SECTION']:
                        name = request.POST['SECTION']
                    else:
                        messages.error(request, 'SECTION Required*')
                        return redirect('SECTIONList')

                    
                    
                    redirect_to = request.POST.get('redirect_to') 
                    if redirect_to:
                        redirect_to = redirect_to
                    else:
                        redirect_to = 'javascript:void(0);'
                        
                        
                    is_header = request.POST.get('header') 
                    if is_header == 'is_header':
                        is_header = True
                    else:
                        is_header = False
                        
                    is_footer = request.POST.get('footer') 
                    if is_footer == 'is_footer':
                        is_footer = True
                    else:
                        is_footer = False
                        
                    is_menu = request.POST.get('menu') 
                    if is_menu == 'is_menu':
                        is_menu = True
                    else:
                        is_menu = False
                    
                    logo = request.POST.get('logo') 
                    if logo:
                        logo = logo
                    else:
                        logo = ''
                        
                    
   
                    SECTIONList.objects.create(name=name, logo=logo, redirect_to=redirect_to, is_header=is_header, is_footer=is_footer, is_menu=is_menu)
                    messages.success(request, f'{name} - Created')
                    base_url = reverse('SECTIONList')  
                    query_string =  urlencode({'page': 1}) 
                    url = '{}?{}'.format(base_url, query_string)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {name} ] - SECTION Created<span>')
                    return redirect(url)

                except Exception as e:
                    print("admin", e)
                    messages.error(request, 'Error Occured')
                    return redirect('SECTIONList')  
            try:
                page = request.GET.get('page', 1)
                filter = request.GET.get('filter')
                if filter:
                    paginator = Paginator(posts_list, filter)
                else:
                    paginator = Paginator(posts_list, 6)
                    
                service_mainCatList = paginator.page(page)  
            except PageNotAnInteger:
                service_mainCatList = paginator.page(1)
            except EmptyPage:
                service_mainCatList = paginator.page(paginator.num_pages)

            context = {
                'CMSManager':'menu-open', 
                'allSECTIONList': 'active', 
                'SECTION':service_mainCatList,
            }
            return render(request,"./template/SECTION/SECTIONList.html", context)

        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    else:
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")
# ==============================================================================
# UPDATE SERVICE MAIN CATEGORY
# ==============================================================================
@accountant_required
def UpdateSECTION(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            data = SECTIONList.objects.get(pk=pk)
            if request.method=="POST":
                try:
                    SECTION = SECTIONList.objects.get(pk=pk)
                    if request.POST['SECTION']:
                        SECTION.name = request.POST['SECTION']
                    else:
                        messages.error(request, 'SECTION Name Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

                    
                    redirect_to = request.POST.get('redirect_to') 
                    if redirect_to:
                        SECTION.redirect_to = redirect_to
                    else:
                        SECTION.redirect_to = 'javascript:void(0);'
                    
                    
                    
                    is_header = request.POST.get('header') 
                    if is_header:
                        SECTION.is_header = True
                    else:
                        SECTION.is_header = False
                        
                    is_footer = request.POST.get('footer') 
                    if is_footer:
                        SECTION.is_footer = True
                    else:
                        SECTION.is_footer = False
                        
                    is_menu = request.POST.get('mobile') 
                    if is_menu:
                        SECTION.is_menu = True
                    else:
                        SECTION.is_menu = False
   
                    logo = request.POST.get('logo') 
                    if logo:
                        SECTION.logo = logo
              
                    
                    SECTION.last_update = timezone.now()
                    SECTION.save()
                    messages.success(request, 'Update Successfully')
                    base_url = reverse('SECTIONList')  
                    query_string =  urlencode({'page': 1}) 
                    url = '{}?{}'.format(base_url, query_string) 
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {request.POST["SECTION"]} ] - SECTION Updated<span>')
                    return redirect(url)            
                    # return redirect(request.META.get('HTTP_REFERER'))
                except Exception:
                    messages.error(request, 'Error Occured')
                    return redirect(request.META.get('HTTP_REFERER'))
                
            context = {
                'CMSManager':'menu-open', 
                'updateSECTION': 'active', 
                'data':data,
            }             
            return render(request,"./template/SECTION/updateSECTION.html", context)
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    else:
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")

# ==============================================================================
# ACTIVATED SERVICE MAIN CATEGORY
# ==============================================================================
@accountant_required
def ActivatedSECTION(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                SECTIONList.objects.filter(pk=pk).update(is_active=True)
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {SECTIONList.objects.get(pk=pk).name} ] - SECTION Activated<span>')
                messages.success(request, 'Activated Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    else:
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")
# ==============================================================================
# DEACTIVATED SERVICE MAIN CATEGORY
# ==============================================================================
@accountant_required
def DeactivatedSECTION(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                SECTIONList.objects.filter(pk=pk).update(is_active=False)
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {SECTIONList.objects.get(pk=pk).name} ] - SECTION Deactivated<span>')
                messages.success(request, 'Deactivated Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    else:
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")
# ==============================================================================
# COPY SERVICE MAIN CATEGORY
# ==============================================================================
@accountant_required
def CopySECTION(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                mainCat = SECTIONList.objects.get(pk=pk)
                name =f'aakriticms'+''.join((random.choice('.com') for i in range(4)))+'-'+mainCat.name
                img  = mainCat.img
                SECTIONList.objects.create(name=name, img=img)
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {name} ] - SECTION Created<span>')
                messages.success(request, 'Category Copy Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except Exception:
                messages.error(request, 'mainCat-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    else:
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")
# ==============================================================================
# DELETE SERVICE MAIN CATEGORY
# ==============================================================================
@superadmin_required
def DeleteSECTION(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            try:
                SECTIONList.objects.filter(pk=pk).delete()
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {SECTIONList.objects.get(pk=pk).name} ] - SECTION Deleted<span>')
                messages.success(request, 'Delete Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    else:
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")