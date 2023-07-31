from AdminAuthentication.decorators import accountant_required, superadmin_required 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from AdminAuthentication.models import AdminActivity
from django.shortcuts import render, redirect
from BLOGManager.models import BlogMainCat
from django.contrib import messages
from urllib.parse import urlencode
from django.utils import timezone
from django.urls import reverse
import random
# ==============================================================================
# CREATE BLOG MAIN CATEGORY
# ==============================================================================
@accountant_required
def CreateBLOGMainCat(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            posts_list = BlogMainCat.objects.all().order_by('-last_update')
            if request.method=="POST":
                try:
                    if request.POST['mainCat']:
                        name = request.POST['mainCat']
                    else:
                        messages.error(request, 'Name Required*')
                        return redirect('blogMainCategory')
                        
                    if request.FILES.get('img'):
                        img = request.FILES['img']
                    else:
                        img = ''
                    BlogMainCat.objects.create(name=name, img=img)
                    messages.success(request, f'{name} - Created')
                    base_url = reverse('blogMainCategory')  
                    query_string =  urlencode({'page': 1}) 
                    url = '{}?{}'.format(base_url, query_string)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {name} ] - BLOGMainCat Created<span>')
                    return redirect(url)

                except Exception:
                    messages.error(request, 'Error Occured')
                    return redirect('blogMainCategory')  

            
            try:
                page = request.GET.get('page', 1)
                filter = request.GET.get('filter')
                if filter:
                    paginator = Paginator(posts_list, filter)
                else:
                    paginator = Paginator(posts_list, 5)

                blogMainCat = paginator.page(page)  
            except PageNotAnInteger:
                blogMainCat = paginator.page(1)
            except EmptyPage:
                blogMainCat = paginator.page(paginator.num_pages)

            context = {
                'BLOGManager':'menu-open', 
                'blogMainCatActive': 'active', 
                'blogMainCat':blogMainCat,
            }
            return render(request,"./template/blogCategory/blogMainCategory.html", context)

        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    else:
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")
# ==============================================================================
# UPDATE BLOG MAIN CATEGORY
# ==============================================================================
@accountant_required
def UpdateBLOGMainCat(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            data = BlogMainCat.objects.get(pk=pk)
            if request.method=="POST":
                try:
                    mainCat = BlogMainCat.objects.get(pk=pk)
                    if request.POST['mainCat']:
                        mainCat.name = request.POST['mainCat']
                    else:
                        messages.error(request, 'Name Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

                    if request.FILES.get('img'):
                        mainCat.img = request.FILES['img']
                        mainCat.save()

                    mainCat.last_update = timezone.now()
                    mainCat.save()
                    messages.success(request, 'Update Successfully')
                    base_url = reverse('blogMainCategory')  
                    query_string =  urlencode({'page': 1}) 
                    url = '{}?{}'.format(base_url, query_string) 
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {request.POST["mainCat"]} ] - BLOGMainCat Updated<span>')
                    return redirect(url)            
                    # return redirect(request.META.get('HTTP_REFERER'))
                except Exception:
                    messages.error(request, 'Error Occured')
                    return redirect(request.META.get('HTTP_REFERER'))
                
            context = {
                'BLOGManager':'menu-open', 
                'blogMainCat': 'active', 
                'data':data,
            }             
            return render(request,"./template/blogCategory/updateBLOGMainCat.html", context)
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    else:
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")

# ==============================================================================
# ACTIVATED BLOG MAIN CATEGORY
# ==============================================================================
@accountant_required
def ActivatedBLOGMainCat(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                BlogMainCat.objects.filter(pk=pk).update(is_active=True)
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {BlogMainCat.objects.get(pk=pk).name} ] - BLOGMainCat Activated<span>')
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
# DEACTIVATED BLOG MAIN CATEGORY
# ==============================================================================
@accountant_required
def DeactivatedBLOGMainCat(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                BlogMainCat.objects.filter(pk=pk).update(is_active=False)
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {BlogMainCat.objects.get(pk=pk).name} ] - BLOGMainCat Deactivated<span>')
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
# COPY BLOG MAIN CATEGORY
# ==============================================================================
@accountant_required
def CopyBLOGMainCat(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                mainCat = BlogMainCat.objects.get(pk=pk)
                name =f'aakriticms'+''.join((random.choice('.com') for i in range(4)))+'-'+mainCat.name
                img  = mainCat.img
                BlogMainCat.objects.create(name=name, img=img)
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {name} ] - BLOGMainCat Created<span>')
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
# DELETE BLOG MAIN CATEGORY
# ==============================================================================
@superadmin_required
def DeleteBLOGMainCat(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            try:
                BlogMainCat.objects.filter(pk=pk).delete()
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {BlogMainCat.objects.get(pk=pk).name} ] - BLOGMainCat Deleted<span>')
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