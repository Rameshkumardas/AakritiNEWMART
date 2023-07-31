from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib import messages

from AdminAuthentication.decorators import accountant_required, superadmin_required
from django.utils.decorators import method_decorator
from .models import FAQCategory, FAQList
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Q

# # =============================================================================
# # =============================================================================
# # MANAGE FAQ 
# # =============================================================================
# # =============================================================================
@method_decorator(accountant_required, name='dispatch')
class ALLFAQList(ListView):
    paginate_by = 5
    template_name = './template/FAQ/faqSTATUS.html'
    ordering = ['id'] 
    context_object_name = 'FAQList'
    extra_context = { 'FAQManager':'menu-open', 'allFAQ':'active'}
    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_active = self.request.GET.get('is_active', 'is_active')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')
        search = self.request.GET.get('search')  

        if(is_draft=='True'):
            if search:
                return FAQList.objects.filter(is_draft=True).exclude(is_deleted=True).filter(Q(name__icontains=search))
            else:
                return FAQList.objects.filter(is_draft=True).exclude(is_deleted=True)
            
        elif(is_verified=='True'):
            if search:
                return FAQList.objects.filter(is_active=True, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).filter(Q(name__icontains=search))
            else:
                return FAQList.objects.filter(is_active=True, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True)
            
        elif(is_active=='False'):
            if search:
                return FAQList.objects.filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_active=True).exclude(is_deleted=True).filter(Q(name__icontains=search))
            else:
                return FAQList.objects.filter(is_active=False, is_verified=True).exclude(is_draft=True).exclude(is_active=True).exclude(is_deleted=True)

        elif(is_deleted=='True'):
            if search:
                return FAQList.objects.filter(is_deleted=True).filter(Q(name__icontains=search))
            else:
                return FAQList.objects.filter(is_deleted=True)
            
    def get_paginate_by(self, queryset):
        filter = self.request.GET.get('filter')
        if filter:
            return self.request.GET.get("paginate_by", filter)
        else:            
            return self.request.GET.get("paginate_by", self.paginate_by)

# # =============================================================================
# # =============================================================================
# # CREATE FAQ
# # =============================================================================
# # =============================================================================
@accountant_required
def createFAQ(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            if request.method == "POST":
                mainCat = request.POST.get('mainCat')
                name = request.POST.get('name')
                description = request.POST.get('description')
                if name and description:
                    FAQList.objects.create(mainCat_id=mainCat, name=name, description=description)
                    messages.success(request, 'FAQ Created')
                    base_url = reverse('FAQList')  
                    query_string =  urlencode({'is_draft': True}) 
                    url = '{}?{}'.format(base_url, query_string) 
                    return redirect(url)
            
                else:
                    messages.error(request, 'Input Filed Required*')
                    return redirect(request.META.get('HTTP_REFERER'))
            context = {
                    'FAQManager':'menu-open', 
                    'createFAQ': 'active',
                    'FAQCats': FAQCategory.objects.filter(is_active=True)
            }
            return render(request,"./template/FAQ/createFAQ.html", context)
        else:
            messages.error(request, 'Login First')
            return redirect('AdminLogOut')
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')
# # =============================================================================
# # =============================================================================
# # UPDATE FAQ
# # =============================================================================
# # =============================================================================
@accountant_required
def updateFAQ(request, slug=None):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:            
            try:
                faq = FAQList.objects.get(slug=slug)
                if request.method == "POST":
                    mainCat = request.POST.get('mainCat')

                    name = request.POST.get('name')
                    description = request.POST.get('description')
                    
                    if mainCat:
                        faq.mainCat_id = mainCat
                        faq.save()
                    
                    if name:
                        faq.name = name
                        faq.save()

                    if description:
                        faq.description = description
                        faq.save()

                    messages.success(request, 'Updated Created')
                    base_url = reverse('FAQList')  
                    query_string =  urlencode({'is_draft': True}) 
                    url = '{}?{}'.format(base_url, query_string) 
                    return redirect(url)
            
                context = {
                        'FAQManager':'menu-open', 
                        'updateFAQ': 'active',
                        'faq':faq,
                }
                return render(request,"./template/FAQ/updateFAQ.html", context)
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
# # VIEW FAQ
# # =============================================================================
@accountant_required
def viewFAQ(request, slug=None):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:            
            try:
                faq = FAQList.objects.get(slug=slug)
                context = {
                        'FAQManager':'menu-open', 
                        'ViewFAQ': 'active',
                        'faq':faq,
                }
                return render(request,"./template/FAQ/viewFAQ.html", context)
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
# # MOVE TO TRASH FAQ
# # =============================================================================
# # =============================================================================
@superadmin_required
def DeleteFAQ(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                faq = FAQList.objects.get(pk=pk)
                faq.is_deleted = True
                faq.is_active = False
                faq.save()
                messages.success(request, 'Delete Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except FAQList.DoesNotExist:
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
# # RESTORE FAQ FROM TRASH
# # =============================================================================
# # =============================================================================
@accountant_required
def RestoreFAQ(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                faq = FAQList.objects.get(pk=pk)
                faq.is_deleted = False
                faq.save()
                messages.success(request, 'Delete Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except FAQList.DoesNotExist:
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
# # PERMANENTLY DELETE FAQ
# # =============================================================================
# # =============================================================================
@accountant_required
def deletePermanentlyFAQ(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                FAQList.objects.get(pk=pk, is_active=True)
                messages.error(request, 'Live FAQ Can Not Be Delete')
                return redirect(request.META['HTTP_REFERER'])
            except FAQList.DoesNotExist:
                FAQList.objects.get(pk=pk).delete()
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
# # ACTIVATED FAQ
# # =============================================================================
# # =============================================================================
@accountant_required
def ActivateFAQ(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            FAQ = FAQList.objects.get(pk=pk)
            FAQ.is_draft = False
            FAQ.is_active = True
            FAQ.is_verified = True
            FAQ.save()
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
# # DEACTIVEATED FAQ
# # =============================================================================
# # =============================================================================
@accountant_required
def DeactivateFAQ(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            FAQ = FAQList.objects.get(pk=pk)
            FAQ.is_active = False
            FAQ.save()
            messages.error(request, 'FAQ Deactivated Successfully')
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

