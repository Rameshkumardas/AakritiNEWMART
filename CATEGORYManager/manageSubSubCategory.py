from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from CATEGORYManager.models import MainCategory, SubSubCategory
from AdminAuthentication.decorators import accountant_required, superadmin_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.db.models import Q

import datetime
import random
# ==============================================================================
# CREATE SUB CATEGORY  
# ==============================================================================
@accountant_required
def CreateSubSubCategory(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            
            q = request.GET.get('search')
            if q:
                posts_list = SubSubCategory.objects.select_related('subCat').filter(Q(name__icontains=q))
            else:
                posts_list = SubSubCategory.objects.select_related('subCat').filter().order_by('-date')
            
            mainCatList = MainCategory.objects.filter(is_active=True)
            if request.method=="POST":
                try:
                    if request.POST['SubCat']!='':
                        subcat_id = request.POST['SubCat']
                    else:
                        messages.error(request, 'Main Category Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    if request.POST['SubSubCat']!='':
                        name = request.POST['SubSubCat']
                    else:
                        messages.error(request, 'Sub Category Name Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    img = request.FILES.get('img')
                    if img:
                        img = img
                    else:
                        img = ''
                
                    SubSubCategory.objects.create(subCat_id=subcat_id, name=name, img=img)
                    messages.success(request, 'Sub Sub Cat Created')
                    return redirect(request.META.get('HTTP_REFERER'))
                
                except Exception:
                    messages.success(request,'Error Occured')
                    return redirect(request.META.get('HTTP_REFERER'))
            
            try:
                page = request.GET.get('page', 1)
                filter = request.GET.get('filter')
                if filter:
                    paginator = Paginator(posts_list, filter)
                else:
                    paginator = Paginator(posts_list, 5)
                    
                SubSubCats = paginator.page(page)
            except PageNotAnInteger:
                SubSubCats = paginator.page(1)
            except EmptyPage:
                SubSubCats = paginator.page(paginator.num_pages)
            
            context = {
                'CATEGORYManager':'menu-open', 
                'SubSubCategory': 'active', 
                'mainCatList':mainCatList,

                'SubSubCats':SubSubCats,
            }
            return render(request,"./template/SubSubCategory.html", context)            
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# UPDATE SUB CATEGORY  
# ==============================================================================
@accountant_required
def UpdateSubSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        mainCat = MainCategory.objects.filter(is_active=True)
        if request.user.token == request.session['token']:
            data = SubSubCategory.objects.get(pk=pk)
            if request.method=="POST":
                try:
                    obj = SubSubCategory.objects.get(pk=pk)
                    if request.POST['SubCat'] !='':
                        obj.subCat_id = request.POST['SubCat']
                        obj.save()
                    else:
                        messages.error(request, 'Main Category Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    img = request.FILES.get('img')
                    if img:
                        obj.img = request.FILES.get('img')
                        obj.save()
                    
                    if request.POST['name']!='':
                        if len(request.POST['name'])<50:
                            name = request.POST['name']
                            obj.name = name
                            obj.last_update = datetime.date.today()
                            obj.save()
                            messages.success(request, 'Successfully Updated')
                            return redirect(request.META.get('HTTP_REFERER'))
                        else:
                            messages.error(request, 'Category Name Less 50 Char')
                            return redirect(request.META.get('HTTP_REFERER'))
                    else:
                        messages.error(request, 'Category Name Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                except Exception as e:
                    print(e)
                    obj.name = request.POST['name']
                    obj.last_update = datetime.date.today()
                    obj.save()
                    messages.success(request, 'Successfully Updated')
                    return redirect(request.META.get('HTTP_REFERER'))
                    # return redirect(request.META.get('HTTP_REFERER'))
            context = {
                'CATEGORYManager':'menu-open', 
                'updateSubSubCat': 'active', 
                'mainCat':mainCat, 
                'data':data
                }
            return render(request,"./template/updateSubSubCat.html", context)
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DELETE SUB CATEGORY  
# ==============================================================================
@accountant_required
def DeleteSubSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                obj = SubSubCategory.objects.get(pk=pk)
                obj.delete()
                messages.success(request, 'Delete Successfuly')
                return redirect(request.META['HTTP_REFERER'])
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# COPY SUB CATEGORY  
# ==============================================================================
@accountant_required
def CopySubSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                subCat = SubSubCategory.objects.get(pk=pk)
                name ='Copy-eMARTSHOP-'+''.join((random.choice('Free') for i in range(4)))+'-'+subCat.name
                slug  ='Copy-eMARTSHOP-'+''.join((random.choice('Free') for i in range(4)))+'-'+subCat.slug
                img = subCat.img
                SubSubCategory.objects.create(mainCat=subCat.mainCat, name=name, slug=slug, img=img)
                messages.success(request, 'Copy Successfuly')
                return redirect(request.META['HTTP_REFERER'])
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# ACTIVATED SUB CATEGORY  
# ==============================================================================
@accountant_required
def ActivatedSubSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                obj = SubSubCategory.objects.get(pk=pk)
                obj.is_active = True
                obj.save()
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
# DEACTIVATED SUB CATEGORY  
# ==============================================================================
@accountant_required
def DeactivatedSubSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                obj = SubSubCategory.objects.get(pk=pk)
                obj.is_active = False
                obj.save()
                messages.success(request, 'Deactivated successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# CREATE SUB CATEGORY  
# ==============================================================================
# # ==============================================================================
# DELETE MAIN CATEGORY USING AJAX
# ==============================================================================
@superadmin_required
def DELETESubSubCat(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                if request.POST.get('targetOBJ'):
                    obj = SubSubCategory.objects.get(pk=request.POST.get('targetOBJ'))
                    obj.delete()
                    return JsonResponse({'status':1, 'message':'Permanently Deleted Successfully', 'Reload':request.META.get('HTTP_REFERER')})
                else:
                    return JsonResponse({'status':0, 'message':'Target Required*'})
            except Exception as e:
                print(e)
                messages.error(request, 'Error Occured')
                return JsonResponse({'status':0, 'message':'Error Occured'})
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# MORE ACCTIONS
# ==============================================================================
