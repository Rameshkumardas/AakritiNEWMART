from AdminAuthentication.decorators import accountant_required, superadmin_required 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from AdminAuthentication.models import AdminActivity
from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import urlencode
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
from .models import BANNERCatList
import random
# ==============================================================================
# CREATE SERVICE MAIN CATEGORY
# ==============================================================================
@accountant_required
def CreateBANNERCat(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            q = request.GET.get('search')
            if q:
                posts_list = BANNERCatList.objects.filter(Q(name__icontains=q)).order_by('-last_update')
            else:
                posts_list = BANNERCatList.objects.all().order_by('-last_update')
                
            if request.method=="POST":
                try:
                    if request.POST['BANNERCat']:
                        name = request.POST['BANNERCat']
                    else:
                        messages.error(request, 'BANNERCat Required*')
                        return redirect('BANNERCatList')

                    BANNERCatList.objects.create(name=name)
                    messages.success(request, f'{name} - Created')
                    base_url = reverse('BANNERCatList')  
                    query_string =  urlencode({'page': 1}) 
                    url = '{}?{}'.format(base_url, query_string)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {name} ] - BANNERCat Created<span>')
                    return redirect(url)

                except Exception:
                    messages.error(request, 'Error Occured')
                    return redirect('BANNERCatList')  

            
            try:
                page = request.GET.get('page', 1)
                paginator = Paginator(posts_list, 6)
                service_mainCatList = paginator.page(page)  
            except PageNotAnInteger:
                service_mainCatList = paginator.page(1)
            except EmptyPage:
                service_mainCatList = paginator.page(paginator.num_pages)

            context = {
                'BANNERManager':'menu-open', 
                'BANNERCatList': 'active', 
                'BANNERCat':service_mainCatList,
            }
            return render(request,"./template/BANNERCat/BANNERCatList.html", context)

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
def UpdateBANNERCat(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            data = BANNERCatList.objects.get(pk=pk)
            if request.method=="POST":
                try:
                    BANNERCat = BANNERCatList.objects.get(pk=pk)
                    if request.POST['BANNERCat']:
                        BANNERCat.name = request.POST['BANNERCat']
                    else:
                        messages.error(request, 'BANNERCat Name Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

                    BANNERCat.last_update = timezone.now()
                    BANNERCat.save()
                    messages.success(request, 'Update Successfully')
                    base_url = reverse('BANNERCatList')  
                    query_string =  urlencode({'page': 1}) 
                    url = '{}?{}'.format(base_url, query_string) 
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {request.POST["BANNERCat"]} ] - BANNERCat Updated<span>')
                    return redirect(url)            
                    # return redirect(request.META.get('HTTP_REFERER'))
                except Exception:
                    messages.error(request, 'Error Occured')
                    return redirect(request.META.get('HTTP_REFERER'))
                
            context = {
                'BANNERManager':'menu-open', 
                'updateBANNERCat': 'active', 
                'data':data,
            }             
            return render(request,"./template/BANNERCat/updateBANNERCat.html", context)
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
def ActivatedBANNERCat(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                BANNERCatList.objects.filter(pk=pk).update(is_active=True)
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {BANNERCatList.objects.get(pk=pk).name} ] - BANNERCat Activated<span>')
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
def DeactivatedBANNERCat(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                BANNERCatList.objects.filter(pk=pk).update(is_active=False)
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {BANNERCatList.objects.get(pk=pk).name} ] - BANNERCat Deactivated<span>')
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
def CopyBANNERCat(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                mainCat = BANNERCatList.objects.get(pk=pk)
                name =f'aakriticms'+''.join((random.choice('.com') for i in range(4)))+'-'+mainCat.name
                img  = mainCat.img
                BANNERCatList.objects.create(name=name, img=img)
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {name} ] - BANNERCat Created<span>')
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
def DeleteBANNERCat(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            try:
                BANNERCatList.objects.filter(pk=pk).delete()
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {BANNERCatList.objects.get(pk=pk).name} ] - BANNERCat Deleted<span>')
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