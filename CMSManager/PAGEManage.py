from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib import messages

from AdminAuthentication.decorators import accountant_required, superadmin_required
from django.utils.decorators import method_decorator

from SLIDERManager.models import BANNERList
from .models import SECTIONList, PAGEList
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Q
from PRODUCTManager.models import ProductList
from django.db.models import Q
# # =============================================================================
# # =============================================================================
# # MANAGE PAGE 
# # =============================================================================
# # =============================================================================
@method_decorator(accountant_required, name='dispatch')
class ALLPAGEList(ListView):
    paginate_by = 20
    template_name = './template/PAGE/PAGESTATUS.html'
    ordering = ['id'] 
    context_object_name = 'PAGEList'
    extra_context = { 'CMSManager':'menu-open', 'allPAGE':'active'}
    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_active = self.request.GET.get('is_active', 'is_active')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')
        search = self.request.GET.get('search')
        if(is_draft=='True'):
            if search:
                return PAGEList.objects.filter(is_draft=True).exclude(is_deleted=True).filter(Q(name__icontains=search))
            else:
                return PAGEList.objects.filter(is_draft=True).exclude(is_deleted=True)
                
        elif(is_verified=='True'):
            if search:
                return PAGEList.objects.filter(is_active=True, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).filter(Q(name__icontains=search))
            else:
                return PAGEList.objects.filter(is_active=True, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True)
        elif(is_active=='False'):
            if search:
                return PAGEList.objects.filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_active=True).exclude(is_deleted=True).filter(Q(name__icontains=search))
            else:
                return PAGEList.objects.filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_active=True).exclude(is_deleted=True)
        elif(is_deleted=='True'):
            if search:
                return PAGEList.objects.filter(is_deleted=True).filter(Q(name__icontains=search))
            else:
                return PAGEList.objects.filter(is_deleted=True)                
        else:
            q = self.request.GET.get('search') 
            if q:
                return PAGEList.objects.filter(Q(name__icontains=q))
            else:
                return PAGEList.objects.all()

    def get_paginate_by(self, queryset):
        filter = self.request.GET.get('filter')
        if filter:
            return self.request.GET.get("paginate_by", filter)
        else:            
            return self.request.GET.get("paginate_by", self.paginate_by)
       
# # =============================================================================
# # =============================================================================
# # CREATE PAGE
# # =============================================================================
# # =============================================================================
@accountant_required
def createPAGE(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            allSECTIONS = SECTIONList.objects.filter(is_active=True)
            allPRODUCTList = ProductList.objects.filter(is_active=True, is_verified=True)
            if request.method == "POST":
                name = request.POST.get('name')
                
                description = request.POST.get('description')
                redirect_to = request.POST.get('slug')
                product = request.POST.getlist('product')

                if description:
                    description = description
                else:
                    description = ''

                section = request.POST.get('section')
                if section:
                    section_id = section
                else:
                    section_id = ''
                
                is_url = request.POST.get('PAGE_TYPE')
                if is_url == 'is_url':                    
                    is_url = True
                elif is_url == 'is_product':
                    is_product = True
                    description = description
                elif is_url == 'is_content':
                    is_content = True
                else:
                    is_content = False
                    is_product = False
                    is_url = False
                
                
                meta_title = request.POST.get('meta_title')
                if meta_title:
                    meta_title = meta_title
                else:
                    meta_title = ''

                meta_keywords = request.POST.get('meta_keywords')
                if meta_keywords:
                    meta_keywords = meta_keywords
                else:
                    meta_keywords = ''

                meta_description = request.POST.get('meta_description')
                if meta_description:
                    meta_description = meta_description
                else:
                    meta_description = ''
                
                if redirect_to and is_url:
                    PAGEList.objects.create(section_id=section_id, name=name,is_url=is_url, redirect_to=redirect_to, meta_title=meta_title, meta_keywords=meta_keywords, meta_description=meta_description)
                elif product and is_product:
                    obj = PAGEList.objects.create(section_id=section_id, is_product=is_product, name=name, description=description, meta_title=meta_title, meta_keywords=meta_keywords, meta_description=meta_description)
                    obj.product.set(product)
                    obj.save()
                elif description and is_content:
                    PAGEList.objects.create(section_id=section_id, name=name, description=description, meta_title=meta_title, meta_keywords=meta_keywords, meta_description=meta_description)
                
                messages.success(request, 'PAGE Created')
                base_url = reverse('PAGEList')  
                query_string =  urlencode({'is_draft': True}) 
                url = '{}?{}'.format(base_url, query_string) 
                return redirect(url)
        
            context = {
                    'CMSManager':'menu-open', 
                    'createPAGE': 'active',
                    'allSECTIONS': allSECTIONS,
                    'allPRODUCTList':allPRODUCTList,
            }
            return render(request,"./template/PAGE/createPAGE.html", context)
        else:
            messages.error(request, 'Login First')
            return redirect('AdminLogOut')
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')
# # =============================================================================
# # =============================================================================
# # UPDATE PAGE
# # =============================================================================
# # =============================================================================
from django.utils import timezone
@accountant_required
def updatePAGE(request, slug=None):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:            
            try:
                PAGE = PAGEList.objects.get(slug=slug)
                allPRODUCTList = ProductList.objects.filter(is_active=True, is_verified=True)
                if request.method == "POST":
                    name = request.POST.get('name')
                    if name:
                        PAGE.name = name
                        PAGE.save()
                
                    description = request.POST.get('description')
                    redirect_to = request.POST.get('slug')
                    product = request.POST.getlist('product')
                    is_url = request.POST.get('PAGE_TYPE')
                    
                    if description:
                        PAGE.description = description
                        PAGE.save()

                    
                    if is_url == 'is_url':
                        PAGE.redirect_to = redirect_to
                        PAGE.is_url = True
                        PAGE.is_product = False
                        PAGE.save()
                    elif is_url == 'is_product':
                        PAGE.is_product = True
                        PAGE.is_url = False
                        if product:
                            PAGE.product.set(product)
                        PAGE.save()

                    elif is_url == 'is_content':
                        PAGE.description = description
                        PAGE.save()
                 
                    meta_title = request.POST.get('meta_title')
                    if meta_title:
                        PAGE.meta_title = meta_title
                        PAGE.save()
            
                    meta_keywords = request.POST.get('meta_keywords')
                    if meta_keywords:
                        PAGE.meta_keywords = meta_keywords
                        PAGE.save()
                    
                    meta_description = request.POST.get('meta_description')
                    if meta_description:
                        PAGE.meta_description = meta_description
                        PAGE.save()
                    messages.success(request, f'Updated Created')
                    base_url = reverse('PAGEList')  
                    query_string =  urlencode({'is_draft': True}) 
                    url = '{}?{}'.format(base_url, query_string) 
                    
                    PAGE.last_update = timezone.now()
                    PAGE.save()
                    return redirect(url)
            
                context = {
                        'CMSManager':'menu-open', 
                        'updatePAGE': 'active',
                        'PAGE':PAGE,
                        'allPRODUCTList':allPRODUCTList,
                }
                return render(request,"./template/PAGE/updatePAGE.html", context)
            except Exception as e:
                print(e)
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Login First')
            return redirect('AdminLogOut')
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')
# # =============================================================================
# # =============================================================================
# # MOVE TO TRASH PAGE
# # =============================================================================
# # =============================================================================
@superadmin_required
def DeletePAGE(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                PAGE = PAGEList.objects.get(pk=pk)
                PAGE.is_deleted = True
                PAGE.is_active = False
                PAGE.save()
                messages.success(request, 'Delete Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except PAGEList.DoesNotExist:
                messages.error(request, 'DoesNotExist')
                return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Login First')
            return redirect('AdminLogOut')
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')
# # =============================================================================
# # =============================================================================
# # RESTORE PAGE FROM TRASH
# # =============================================================================
# # =============================================================================
@accountant_required
def RestorePAGE(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                PAGE = PAGEList.objects.get(pk=pk)
                PAGE.is_deleted = False
                PAGE.save()
                messages.success(request, 'Delete Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except PAGEList.DoesNotExist:
                messages.error(request, 'DoesNotExist')
                return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Login First')
            return redirect('AdminLogOut')
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')
# # =============================================================================
# # =============================================================================
# # PERMANENTLY DELETE PAGE
# # =============================================================================
# # =============================================================================
@accountant_required
def deletePermanentlyPAGE(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                PAGEList.objects.get(pk=pk, is_active=True, is_verified=True)
                messages.error(request, 'Live Can Not Be Delete')
                return redirect(request.META['HTTP_REFERER'])
            except PAGEList.DoesNotExist:
                PAGEList.objects.get(pk=pk).delete()
                messages.success(request, 'Delete Successfully')
                return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Login First')
            return redirect('AdminLogOut')
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')
# # =============================================================================
# # =============================================================================
# # ACTIVATED PAGE
# # =============================================================================
# # =============================================================================
@accountant_required
def ActivatePAGE(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            PAGE = PAGEList.objects.get(pk=pk)
            PAGE.is_draft = False
            PAGE.is_active = True
            PAGE.is_verified = True
            PAGE.save()
            messages.success(request, 'Activated Successfully')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Login First')
            return redirect('AdminLogOut')
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')
# # =============================================================================
# # =============================================================================
# # DEACTIVEATED PAGE
# # =============================================================================
# # =============================================================================
@accountant_required
def DeactivatePAGE(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            PAGE = PAGEList.objects.get(pk=pk)
            PAGE.is_active = False
            PAGE.save()
            messages.success(request, 'Deactivated Successfully')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Login First')
            return redirect('AdminLogOut')
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')
# # =============================================================================
# # =============================================================================
# # MORE OPERATIONS
# # =============================================================================
# # =============================================================================



# # =============================================================================
# # =============================================================================
# # OPEN PAGE
# # =============================================================================
# # =============================================================================
from django.utils import timezone

def OPENCONTENTPAGE(request, slug=None):
    try:
        PAGE = PAGEList.objects.get(slug=slug)  
        if PAGE.is_product:
            context = {
                'page':PAGE,
            }    
            return render(request,"./template/home/CMSProductList.html", context)
        else:
            context = {
                'page':PAGE,
            }    
            return render(request,"./template/home/descriptionVIEW.html", context)
    except Exception as e:
        print(e)
        messages.error(request, 'Error Occured')
        return redirect(request.META.get('HTTP_REFERER'))
# # =============================================================================
# # =============================================================================
# # MOVE TO TRASH PAGE
# # =============================================================================
# # =============================================================================
