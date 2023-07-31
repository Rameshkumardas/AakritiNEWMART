from AdminAuthentication.decorators import accountant_required, superadmin_required
from AdminAuthentication.models import AdminActivity
from BLOGManager.models import BLOGList, BlogMainCat, BlogSubCat
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import urlencode
from django.utils import timezone
from django.http import Http404
from django.urls import reverse
# ==============================================================
# CHAPTER LIST CLASS
# ==============================================================
@method_decorator(accountant_required, name='dispatch')
class ALLBLOGList(ListView):
    paginate_by = 1000
    template_name = './template/blogSTATUS.html'
    context_object_name = 'BLOGList'
    extra_context = { 'BLOGManager':'menu-open', 'allBLOGS': 'active'}
    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_active = self.request.GET.get('is_active', 'is_active')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')        
        if is_draft == 'True':
            return BLOGList.objects.select_related('SubCat').select_related('author').filter(is_draft=True).exclude(is_deleted=True).order_by('-id')
        elif is_verified == 'True':
            return BLOGList.objects.select_related('SubCat').select_related('author').filter(is_active=True, is_verified=True, is_draft=False, is_deleted=False)
        elif is_active == 'False':
            return BLOGList.objects.select_related('SubCat').select_related('author').filter(is_active=False, is_verified=True, is_draft=False).exclude(is_deleted=True)
        elif is_deleted == 'True':
            return BLOGList.objects.select_related('SubCat').select_related('author').filter(is_deleted=True)
        else:
            return BLOGList.objects.select_related('SubCat').select_related('author').all()
        
@accountant_required
def CreateBLOG(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            mainCat = BlogMainCat.objects.filter(is_active=True)
            if request.method=="POST":
                try:
                    if request.POST['subCat']!='':
                        SubCat_id = request.POST['subCat']
                    else:
                        messages.error(request, 'SubCat Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

                    if request.POST['name']!='':
                        name = request.POST['name']
                    else:
                        messages.error(request, 'Name Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    img = request.FILES.get('img')
                    if img:
                        img = img
              
                    if request.POST.get('intro')!='':
                        intro = request.POST['intro']
                    else:
                        intro = ''

                    if request.POST.get('summary')!='':
                        summary = request.POST['summary']
                    else:
                        summary = ''

                    if request.POST.get('reference')!='':
                        reference = request.POST['reference']
                    else:
                        reference = ''

                    if request.POST['meta_title']!='':
                        meta_title = request.POST['meta_title']
                    else:
                        meta_title = ''

                    if request.POST['meta_keywords']!='':
                        meta_keywords = request.POST['meta_keywords']
                    else:
                        meta_keywords = ''

                    if request.POST['meta_description']!='':
                        meta_description = request.POST['meta_description']
                    else:
                        meta_description = ''

                    if request.POST['description']!='':
                        description = request.POST['description']
                        author = request.user
                        BLOGList.objects.create(SubCat_id=SubCat_id, name=name, img=img, intro=intro, description=description, summary=summary, reference=reference,  meta_title=meta_title, meta_keywords=meta_keywords, meta_description=meta_description, author=author)
                                            
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {name} ] - BLOG Created<span>')
                        messages.success(request, 'Created Successfully')
                        base_url = reverse('BLOGList')  
                        query_string =  urlencode({'is_draft': True}) 
                        url = '{}?{}'.format(base_url, query_string) 
                        # return redirect(url)
                        return redirect(request.META.get('HTTP_REFERER'))
                    else:
                        messages.error(request, 'Description is Required')
                        return redirect(request.META.get('HTTP_REFERER'))
                        
                except  Exception as e:
                    messages.error(request, f'{e}')
                    return redirect(request.META.get('HTTP_REFERER'))
            
            context = {
                    'BLOGManager':'menu-open', 
                    'CreateBlogs': 'active', 
                    'mainCat':mainCat
            }
            return render(request,"./template/createBLOG.html", context)
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')

@accountant_required
def updateBLOG(request, slug):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            blog = BLOGList.objects.get(slug=slug)
            context =  {
                'BLOGManager':'menu-open', 
                'allblog': 'active', 
                'blog':blog,
            }
            return render(request, './template/updateBLOG.html', context)   
        else:
            messages.error(request, f'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, f'You Dont Have Access')
        return redirect(request.META.get('HTTP_REFERER'))

# ==============================================================
# MOVE TO BIN BLOG
# ==============================================================
@accountant_required
def deleteBLOG(request, pk):
    if request.user.token == request.session['token']:
        try:
            BLOG = BLOGList.objects.get(pk=pk)
            BLOG.is_deleted = True
            BLOG.is_active = False
            BLOG.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {BLOG.name} ] - BLOG Deleted<span>')
            messages.success(request, 'Move to Bin Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# RESTORE BLOG FROM BIN
# ==============================================================
@accountant_required
def restoreBLOG(request, pk):
    if request.user.token == request.session['token']:
        try:
            BLOG = BLOGList.objects.get(pk=pk)
            BLOG.is_deleted = False
            BLOG.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {BLOG.name} ] - BLOG Restored<span>')
            messages.success(request, 'Restore Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# PERMANENT DELETE BLOG
# ==============================================================
@superadmin_required
def PermanentDeleteBLOG(request, pk):
    if request.user.is_admin:
        try:
            BLOG = BLOGList.objects.get(pk=pk)
            BLOG.delete()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {BLOG.name} ] - BLOG Deleted<span>')
            messages.success(request, 'Permanent Deleted Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, 'Error Occured')
        return redirect(request.META['HTTP_REFERER'])

# ==============================================================
# ACTIVATED BLOG
# ==============================================================
@accountant_required
def activateBLOG(request, pk):
    if request.user.token == request.session['token']:
        try:
            BLOG = BLOGList.objects.get(pk=pk)
            BLOG.is_draft = False
            BLOG.is_active = True
            BLOG.is_verified = True
            BLOG.last_update = timezone.now()
            BLOG.date = timezone.now()
            BLOG.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {BLOG.name} ] - BLOG Activated<span>')
            messages.success(request, 'Activate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# DEACTIVATED BLOG
# ==============================================================
@accountant_required
def deactivateBLOG(request, pk):
    if request.user.token == request.session['token']:
        try:
            BLOG = BLOGList.objects.get(pk=pk)
            BLOG.is_draft = False
            BLOG.is_active = False
            BLOG.last_update = timezone.now()
            BLOG.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {BLOG.name} ] - BLOG Deactivated<span>')
            messages.success(request, 'Deactivate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404

# ==============================================================
# MORE OPERATION
# ==============================================================
@accountant_required
def LoadBLOGSubCatLIST(request):
    context = {
        'subCats': BlogSubCat.objects.filter(mainCat_id=request.POST['mainCat'], is_active=True)
    }
    return render(request, './template/blogSubCategoryList.html', context)

