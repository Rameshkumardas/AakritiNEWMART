from AdminAuthentication.decorators import accountant_required, superadmin_required
from BRANDManager.models import BRANDList
from CommonModules.models import COLORList
from AdminAuthentication.models import AdminActivity
from django.utils.decorators import method_decorator
from CATEGORYManager.models import MainCategory, SubCategory, SubSubCategory
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from PRODUCTManager.models import ProductList
from django.contrib import messages
from urllib.parse import urlencode
from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from django.db.models import Q
# ==============================================================
# CHAPTER LIST CLASS
# ==============================================================
@method_decorator(accountant_required, name='dispatch')
class ALLPRODUCTList(ListView):
    paginate_by = 15
    template_name = './template/productSTATUS.html'
    context_object_name = 'PRODUCTList'
    extra_context = { 'PRODUCTManager':'menu-open', 'allPRODUCTS': 'active'}
    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_out_of_stock = self.request.GET.get('is_out_of_stock', 'is_out_of_stock')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')  
        search = self.request.GET.get('search')  
        SubSubCat = self.request.GET.get('SubSubCat')  


        # ProductList.objects.filter().delete()
        # for i in range(1, 100):
        #     product = ProductList.objects.get(slug='iphone-14-pro-max')
        #     ProductList.objects.create(author=product.author, mainCat=product.mainCat, subCat=product.subCat, SubSubCat=product.SubSubCat, brand=product.brand, color=product.color, name=product.name, img=product.img, is_active=True, is_verified=True)
        
        if(is_draft=='True'):
            if search or SubSubCat:
                return ProductList.objects.filter(is_draft=True).exclude(is_deleted=True).filter(SubSubCat=SubSubCat).filter(Q(name__icontains=search))
            else:
                return ProductList.objects.filter(is_draft=True).exclude(is_deleted=True)
            
        elif(is_verified=='True'):
            if search or SubSubCat:
                return ProductList.objects.filter(is_active=True, is_verified=True).filter(SubSubCat=SubSubCat).filter(Q(name__icontains=search)).exclude(is_draft=True).exclude(is_deleted=True).order_by('-last_update')
            else:
                return ProductList.objects.filter(is_active=True, is_verified=True).exclude(is_draft=True).exclude(is_deleted=True).order_by('-last_update')
        elif(is_out_of_stock=='True'):
            if search or SubSubCat:
                return ProductList.objects.filter(is_out_of_stock=False, is_verified=True).filter(SubSubCat=SubSubCat).filter(Q(name__icontains=search)).exclude(is_draft=True).exclude(is_active=True).exclude(is_deleted=True)
            else:
                return ProductList.objects.filter(is_out_of_stock=False, is_verified=True).exclude(is_draft=True).exclude(is_active=True).exclude(is_deleted=True)

        elif(is_deleted=='True'):
            if search or SubSubCat:
                return ProductList.objects.filter(is_deleted=True).filter(SubSubCat=SubSubCat).filter(Q(name__icontains=search))
            else:
                return ProductList.objects.filter(is_deleted=True)
        else:
            return ProductList.objects.all()
            
    def get_paginate_by(self, queryset):
        filter = self.request.GET.get('filter')
        if filter:
            return self.request.GET.get("paginate_by", filter)
        else:            
            return self.request.GET.get("paginate_by", self.paginate_by)

    def get_context_data(self,*args, **kwargs):
        context = super(ALLPRODUCTList, self).get_context_data(*args,**kwargs)
        mainCat = self.request.GET.get('fMainCat')
        subCat = self.request.GET.get('SubCat')
        if mainCat:
            context['FILTERSubCat'] = SubCategory.objects.filter(mainCat_id=mainCat, is_active=True)
        if subCat:
            context['FILTERSubSubCat'] = SubSubCategory.objects.filter(subCat_id=subCat, is_active=True)
        context['mainCatList'] = MainCategory.objects.filter(is_active=True)
        return context
    
@accountant_required
def updatePRODUCT(request, pk=None, slug=None):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            attribute = request.GET.get('attribute', 'attribute')
            mainCatList = MainCategory.objects.filter(is_active=True)
            activeBRNADList = BRANDList.objects.filter(is_active=True)
            activeCOLORList = COLORList.objects.filter(is_active=True)
            # activeATTRIBUTEList = ATTRIBUTEList.objects.filter(is_active=True)

            if (attribute=='default'):
                Products = ProductList.objects.get(pk=pk)
            else:
                Products = ProductList.objects.get(pk=pk)

            context = {
                'PRODUCTManager':'menu-open', 
                'updatePRODUCT': 'active',
                'product':Products,
                'mainCatList':mainCatList,
                'activeCOLORList':activeCOLORList,
                'BRANDList':activeBRNADList,
                # 'activeATTRIBUTEList':activeATTRIBUTEList,
            }
            return render(request,"./template/updateProduct.html", context)
        else:
            messages.error(request, 'You Dont Have Acceess')
            return redirect('AdminLogOut')
    else:
        messages.error(request, 'Login First')
        return redirect('AdminLogOut')

# # =============================================================================
# # =============================================================================
# # MOVE TO TRASH obj
# # =============================================================================
# # =============================================================================
@superadmin_required
def DeletePRODUCT(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                obj = ProductList.objects.get(pk=pk)
                obj.is_deleted = True
                obj.is_active = False
                obj.save()
                messages.success(request, 'Delete Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except ProductList.DoesNotExist:
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
# # RESTORE obj FROM TRASH
# # =============================================================================
# # =============================================================================
@accountant_required
def RestorePRODUCT(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                obj = ProductList.objects.get(pk=pk)
                obj.is_deleted = False
                obj.save()
                messages.success(request, 'Delete Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except ProductList.DoesNotExist:
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
# # PERMANENTLY DELETE obj
# # =============================================================================
# # =============================================================================
@accountant_required
def deletePermanentlyPRODUCT(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                ProductList.objects.get(pk=pk, is_active=True)
                messages.error(request, 'Live Product Can Not Be Delete')
                return redirect(request.META['HTTP_REFERER'])
            except ProductList.DoesNotExist:
                ProductList.objects.get(pk=pk).delete()
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
# # ACTIVATED obj
# # =============================================================================
# # =============================================================================
@accountant_required
def ActivatePRODUCT(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            obj = ProductList.objects.get(pk=pk)
            obj.is_draft = False
            obj.is_active = True
            obj.is_verified = True
            obj.save()
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
# # DEACTIVEATED PRODUCT
# # =============================================================================
# # =============================================================================
@accountant_required
def DeactivatePRODUCT(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            obj = ProductList.objects.get(pk=pk)
            obj.is_active = False
            obj.save()
            messages.error(request, 'Deactivated Successfully')
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
