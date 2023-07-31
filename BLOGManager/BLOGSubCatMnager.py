from AdminAuthentication.decorators import accountant_required, superadmin_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from AdminAuthentication.models import AdminActivity
from BLOGManager.models import BlogMainCat, BlogSubCat
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.http import Http404
import datetime
import random

# ==============================================================================
# CREATE SUB CATEGORY
# ==============================================================================
@accountant_required
def CreateSubCategory(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            posts_list = BlogSubCat.objects.all().order_by('-last_update')
            
            mainCat = BlogMainCat.objects.filter(is_active=True)
            if request.method=="POST":
                try:
                    if request.POST['mainCat']:
                        cat_id = request.POST['mainCat']
                    else:
                        messages.error(request, 'MainCat Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

                    if request.FILES.get('img'):
                        img = request.FILES['img']
                    else:
                        img = ''
                    
                    if request.POST['subCat']:
                        name = request.POST['subCat']
                    else:
                        messages.error(request, 'Name Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    BlogSubCat.objects.create(mainCat_id=cat_id, name=name, img=img)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {name} ] - BLOGSubCat Created<span>')
                    messages.success(request, 'SubCat Created')
                    return redirect(request.META.get('HTTP_REFERER'))
                except Exception:
                    messages.error(request, f'Error Occured')
                    return redirect(request.META.get('HTTP_REFERER'))
            
            try:
                page = request.GET.get('page', 1)
                filter = request.GET.get('filter')
                if filter:
                    paginator = Paginator(posts_list, filter)
                else:
                    paginator = Paginator(posts_list, 5)
                subCat = paginator.page(page)
            except PageNotAnInteger:
                subCat = paginator.page(1)
            except EmptyPage:
                subCat = paginator.page(paginator.num_pages)

            context ={
                'BLOGManager':'menu-open', 
                'blogSubCat': 'active', 
                'mainCat':mainCat, 
                'subCat':subCat
            }
            return render(request,"./template/blogCategory/BLOGSubCat.html", context)            
        else:
            messages.error(request, 'Please Login First')
            return redirect('AdminLogOut')
    else:
        messages.error(request, 'Please Login First')
        return redirect('AdminLogOut')
# ==============================================================================
# UPDATE SUB CATEGORY
# ==============================================================================
@accountant_required
def UpdateSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        mainCat = BlogMainCat.objects.all()
        if request.user.token == request.session['token']:
            try:
                subCat = BlogSubCat.objects.get(pk=pk)
                if request.method=="POST":
                    if request.POST['mainCat']:
                        subCat.mainCat_id = request.POST['mainCat']
                        subCat.save()
                    else:
                        messages.error(request, 'MainCat Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    img = request.FILES.get('img')
                    if img:
                        subCat.img = img
                        subCat.save()  

                    name = request.POST.get('name')
                    if name:
                        subCat.name = name
                        subCat.save()

                    subCat.last_update = timezone.now()
                    subCat.save()
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {name} ] - BLOGSubCat Created<span>')
                    messages.success(request, 'Update Successed')
                    return redirect('blogSubCategory')
                    # return redirect(request.META.get('HTTP_REFERER'))
                
            except Exception as e:
                messages.error(request, f'{e} Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
            
            context = {
                'BLOGManager':'menu-open', 
                'blogSubCat': 'active', 
                'mainCat':mainCat, 
                'subCat':subCat,
            }
            return render(request,"./template/blogCategory/updateBLOGSubCat.html", context)
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# ACTIVATE SUB CATEGORY
# ==============================================================================
@accountant_required
def activatedSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                subCat = BlogSubCat.objects.get(pk=pk)
                subCat.is_active = True
                subCat.save()
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {subCat.name} ] - BLOGSubCat Activated<span>')
                messages.success(request, 'Activated Successfuly')
                return redirect(request.META['HTTP_REFERER'])
            except BlogSubCat.DoesNotExist:
                messages.error(request, 'BLOGSubCat-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DEACTIVATE SUB CATEGORY
# ==============================================================================
@accountant_required
def deactivatedSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                subCat = BlogSubCat.objects.get(pk=pk)
                subCat.is_active = False
                subCat.save()
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {subCat.name} ] - BLOGSubCat Deactivated<span>')
                messages.success(request, 'Deactivated Successfuly')
                return redirect(request.META['HTTP_REFERER'])
            except BlogSubCat.DoesNotExist:
                messages.error(request, 'BLOGSubCat-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# DELETE SUB CATEGORY
# ==============================================================================
@superadmin_required
def DeleteSubCategory(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                subCat = BlogSubCat.objects.get(pk=pk)
                subCat.delete()
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {subCat.name} ] - BLOGSubCat Deleted<span>')
                messages.success(request, 'SubCat Deleted')
                return redirect(request.META['HTTP_REFERER'])
            except Exception:
                messages.error(request, 'BLOGSubCat-DoesNotExist')
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
                subCat = BlogSubCat.objects.get(pk=pk)
                cat_id = subCat.cat_id
                name = 'Copy-Aakriti-'+''.join((random.choice('Lite') for i in range(4)))+'-'+subCat.name
                slug  = 'Copy-Aakriti-'+''.join((random.choice('Lite') for i in range(4)))+'-'+subCat.slug
                img  = subCat.img
                BlogSubCat.objects.create(mainCat_id= cat_id, name=name, slug=slug, img=img)
                messages.error(request, 'Copy Successed')
                return redirect(request.META['HTTP_REFERER'])
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            raise Http404
    else:
        raise Http404
# ==============================================================================
# MORE FUNCTIONS AND CLASSES
# ==============================================================================
