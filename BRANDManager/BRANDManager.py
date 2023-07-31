from django.contrib.auth.decorators import login_required
from AdminAuthentication.models import AdminRegistration
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BRANDList
from django.http import Http404
import datetime
import random
import datetime
from django.contrib.auth.decorators import login_required
from AdminAuthentication.models import AdminRegistration
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib import messages
from django.http import Http404
import random
from django.urls import reverse
from urllib.parse import urlencode

@method_decorator(login_required, name='dispatch')
class ALLBRANDList(ListView):
    paginate_by = 5
    template_name = './template/BRAND/BRANDSTATUS.html'
    ordering = ['id'] 
    extra_context = { 'BRANDManager':'menu-open', 'BRANDListActive': 'active'}
    context_object_name = 'BRANDList'
    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_active = self.request.GET.get('is_active', 'is_active')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')
        if is_draft == 'True':
            return BRANDList.objects.filter(is_active=False, is_verified=False, is_draft=True)
        elif is_verified == 'True':
            return BRANDList.objects.filter(is_active=True, is_verified=True, is_draft=False, is_deleted=False)
        elif is_active == 'False':
            return BRANDList.objects.filter(is_active=False, is_verified=True, is_draft=False).exclude(is_deleted=True)
        elif is_deleted == 'True':
            return BRANDList.objects.filter(is_deleted=True)
        else:
            return BRANDList.objects.all()

    def get_paginate_by(self, queryset):
        filter = self.request.GET.get('filter')
        if filter:
            return self.request.GET.get("paginate_by", filter)
        else:            
            return self.request.GET.get("paginate_by", self.paginate_by)

# ==============================================================================
# CREATEBRAND Category  
# ==============================================================================
@login_required
def CreateBRAND(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            if request.method=="POST":
                try:
                    if request.POST.get('name')!='':
                        name = request.POST.get('name')
                    else:
                        messages.error(request, 'BRAND Category Required')
                        return redirect(request.META.get('HTTP_REFERER'))

                    if request.FILES.get('img')!='':
                        img = request.FILES.get('img')
                    else:
                        messages.error(request, 'IMG Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

                    if request.POST.get('description')!='':
                        description = request.POST.get('description')
                        BRANDList.objects.create(name=name, img=img, description=description)
                        messages.success(request, 'BRAND Created')
                        # messages.success(request, 'Created Successfully')
                        base_url = reverse('BRANDList')  
                        query_string =  urlencode({'is_draft': True}) 
                        url = '{}?{}'.format(base_url, query_string) 
                        return redirect(url)
                
                    else:
                        messages.error(request, 'Description Required*')             
                        return redirect(request.META.get('HTTP_REFERER'))
                except Exception as e:
                    messages.error(request, f'{e}')
                    return redirect(request.META.get('HTTP_REFERER'))
            context = {
                'BRANDManager':'menu-open', 
                'CreateBRAND': 'active', 
            }
            return render(request,"./template/BRAND/createBRAND.html", context)
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# UPDATEBRAND Category 
# ==============================================================================
@login_required
def updateBRAND(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                BRAND = BRANDList.objects.get(pk=pk)
                if request.method=="POST":
        
                    if request.POST.get('name')!='':
                        BRAND.name = request.POST.get('name')
                        BRAND.save()
                    else:
                        messages.error(request, 'BRAND Category Required')
                        return redirect(request.META.get('HTTP_REFERER'))

                    if request.FILES.get('img'):
                        BRAND.img = request.FILES.get('img')
                        BRAND.save()

                    if request.POST.get('description')!='':
                        BRAND.description = request.POST.get('description')
                        BRAND.save()
                        messages.success(request, 'Updated Successfully')
                        # return redirect(request.META.get('HTTP_REFERER'))
                        base_url = reverse('BRANDList')  
                        query_string =  urlencode({'is_draft': True}) 
                        url = '{}?{}'.format(base_url, query_string) 
                        return redirect(url)
                    else:
                        messages.error(request, 'Description Required*')             
                        return redirect(request.META.get('HTTP_REFERER'))
                context = {
                    'BRANDManager':'menu-open', 
                    'BRAND': 'active', 
                    'BRAND':BRAND,
                    }
                return render(request,"./template/BRAND/updateBRAND.html", context)
            except Exception:
                messages.error(request, 'Error Occured*')             
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DELETEBRAND Category 
# ==============================================================================
@login_required
def DeleteBRAND(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                BRANDList.objects.filter(pk=pk).update(is_deleted = True, is_active=False, is_draft=False)
                messages.success(request, 'Deleted Successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# ACTIVATEBRAND Category 
# ==============================================================================
@login_required
def ActivatedBRAND(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                BRANDList.objects.filter(pk=pk).update(is_active = True,is_verified=True, is_draft=False)
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
# DEACTIVATEDBRAND Category 
# ==============================================================================
@login_required
def DeactivatedBRAND(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                BRANDList.objects.filter(pk=pk).update(is_active = False, is_draft=False)
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
# DEACTIVATEDBRAND Category 
# ==============================================================================
@login_required
def PermanentlyDeleteBRAND(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                BRANDList.objects.filter(pk=pk).delete()
                messages.success(request, 'Permanently Deleted')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DEACTIVATEDBRAND Category 
# ==============================================================================
@login_required
def RestoreBRAND(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin:
            try:
                BRANDList.objects.filter(pk=pk).update(is_deleted = False, is_active=False, is_draft=False)
                messages.success(request, 'Restore Successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# MORE ACCTIONS
# ==============================================================================