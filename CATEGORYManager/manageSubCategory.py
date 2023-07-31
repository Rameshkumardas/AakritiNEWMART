from django.contrib.auth.decorators import login_required
from AdminAuthentication.decorators import accountant_required, superadmin_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from AdminAuthentication.models import AdminRegistration
from CATEGORYManager.models import MainCategory, SubCategory
from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib import messages
import datetime
import random
from django.db.models import Q

# ==============================================================================
# CREATE SUB CATEGORY  
# ==============================================================================
@accountant_required
def CreateSubCategory(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            q = request.GET.get('search')
            if q:
                posts_list = SubCategory.objects.filter(Q(name__icontains=q))
            else:
                posts_list = SubCategory.objects.all()
                
            mainCat = MainCategory.objects.filter(is_active=True)
            if request.method=="POST":
                try:
                    if request.POST['mainCat']!='':
                        cat_id = request.POST['mainCat']
                    else:
                        messages.error(request, 'Main Category is Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    if request.POST['subCat']!='':
                        name = request.POST['subCat']
                        newsubcat = name.lower()
                        slug = newsubcat.replace(" ", "-")
                    else:
                        messages.error(request, 'Sub Category Name is Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    if request.FILES.get('img')!='':
                        img = request.FILES.get('img')
                    else:
                        messages.error(request, 'Main Category is Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
               
             
                    SubCategory.objects.create(mainCat_id=cat_id, name=name, img=img, slug=slug)
                    messages.success(request, 'Sub Category Created')
                    return redirect(request.META.get('HTTP_REFERER'))
                except Exception:
                    messages.success(request, 'Error Occured')
                    return redirect(request.META.get('HTTP_REFERER'))
            
            
            try:
                page = request.GET.get('page', 1)
                filter = request.GET.get('filter')
                if filter:
                    paginator = Paginator(posts_list, filter)
                else:
                    paginator = Paginator(posts_list, 15)

                subCat = paginator.page(page)
            except PageNotAnInteger:
                subCat = paginator.page(1)
            except EmptyPage:
                subCat = paginator.page(paginator.num_pages)

            


            context = {
                'CATEGORYManager':'menu-open', 
                'SubCategory': 'active', 
                'mainCat':mainCat, 
                'subCat':subCat
            }
            return render(request,"./template/subCategory.html", context)            
        
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# UPDATE SUB CATEGORY  
# ==============================================================================
@accountant_required
def UpdateSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        mainCat = MainCategory.objects.filter(is_active=True)
        if request.user.token == request.session['token']:
            data = SubCategory.objects.get(pk=pk)
            if request.method=="POST":
                try:
                    obj = SubCategory.objects.get(pk=pk)
                    if request.POST['mainCat'] !='':
                        obj.mainCat_id = request.POST['mainCat']
                        obj.save()
                    else:
                        messages.error(request, 'Main Category is Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    img = request.FILES.get('img')
                    if img:
                        obj.img = img
                        obj.save()
     
                    slug = request.POST.get('slug')
                    if slug:
                        if not SubCategory.objects.filter(slug=slug).exists():
                            obj.slug = request.POST.get('slug')
                            obj.save()


                    if request.POST['name']!='':
                        if len(request.POST['name'])<50:
                            name = request.POST['name']
                            obj.name = name
                            obj.last_update = datetime.date.today()
                            obj.save()
                            messages.success(request, 'Sub Category Updated')
                            return redirect(request.META.get('HTTP_REFERER'))
                        else:
                            messages.error(request, 'Category Name Less 50 Char')
                            return redirect(request.META.get('HTTP_REFERER'))
                    else:
                        messages.error(request, 'Category Name is Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                except Exception:
                    obj.img = SubCategory.objects.get(pk=pk).img
                    obj.name = request.POST['name']
                    obj.last_update = datetime.date.today()
                    obj.save()
                    messages.success(request, 'Sub Category Updated')
                    return redirect(request.META.get('HTTP_REFERER'))
            context = {
                'CATEGORYManager':'menu-open', 
                'updateSubCat': 'active', 
                'mainCat':mainCat, 
                'data':data
                }
            
            return render(request,"./template/update-subCategory.html", context)
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DELETE SUB CATEGORY  
# ==============================================================================
@accountant_required
def DeleteSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                SubCategory.objects.get(pk=pk).delete()
                messages.success(request, 'Delete Successfuly')
                return redirect(request.META['HTTP_REFERER'])
            except Exception:
                messages.error(request, f'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# COPY SUB CATEGORY  
# ==============================================================================
@accountant_required
def CopySubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                subCat = SubCategory.objects.get(pk=pk)
                name ='Copy-ozymed-'+''.join((random.choice('cms') for i in range(4)))+'-'+subCat.name
                slug  ='Copy-ozymed-'+''.join((random.choice('cms') for i in range(4)))+'-'+subCat.slug
                img = subCat.imgozymed
                SubCategory.objects.create(mainCat=subCat.mainCat, name=name, slug=slug, img=img)
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
def ActivatedSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                mainCat = SubCategory.objects.get(pk=pk)
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
# DEACTIVATED SUB CATEGORY  
# ==============================================================================
@accountant_required
def DeactivatedSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                mainCat = SubCategory.objects.get(pk=pk)
                mainCat.is_active = False
                mainCat.save()
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
def DELETESubCat(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                if request.POST.get('targetSubCat'):
                    mainCat = SubCategory.objects.get(pk=request.POST.get('targetSubCat'))
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
