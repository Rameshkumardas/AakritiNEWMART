from CMSManager.models import PAGEList
from AdminAuthentication.decorators import accountant_required, superadmin_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from .models import BANNERCatList, BANNERList
from django.contrib import messages
from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from urllib.parse import urlencode
# ==============================================================
# CHAPTER LIST CLASS
# ==============================================================
@method_decorator(accountant_required, name='dispatch')
class ALLBANNERList(ListView):
    paginate_by = 5
    template_name = './template/banner/bannerSTATUS.html'
    ordering = ['id'] 
    context_object_name = 'BANNERList'
    extra_context = { 'BANNERManager':'menu-open', 'allBANNERS': 'active'}
    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_active = self.request.GET.get('is_active', 'is_active')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')
        if is_draft == 'True':
            return BANNERList.objects.filter(is_draft=True).exclude(is_deleted=True)
        elif is_verified == 'True':
            return BANNERList.objects.filter(is_active=True, is_verified=True, is_draft=False, is_deleted=False)
        elif is_active == 'False':
            return BANNERList.objects.filter(is_active=False, is_verified=True, is_draft=False).exclude(is_deleted=True)
        elif is_deleted == 'True':
            return BANNERList.objects.filter(is_deleted=True)
        else:
            return BANNERList.objects.all()
        
@accountant_required
def CreateBANNER(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            ALLBANNERList = BANNERCatList.objects.filter(is_active=True)
            ALLPAGEList = PAGEList.objects.filter(is_url=False, is_active=True, is_verified=True)
            
            if request.method=="POST":
                try:
                    BANNERCat = request.POST.get('BANNERCat')
                    if BANNERCat:
                        BANNERCat_id = BANNERCat
                    else:
                        BANNERCat_id = ''
                        
                    page = request.POST.get('PAGEList')
                    if page:
                        page_id = page
                    else:
                        page_id = ''
          
                    if request.POST['name']!='':
                        name = request.POST['name']
                    else:
                        name = ''
        
                    if request.POST['title']!='':
                        title = request.POST['title']
                    else:
                        title = ''
                    if request.POST['code']!='':
                        code = request.POST['code']
                    else:
                        code = ''
                        
                    banner_type = request.POST.get('BANNER_TYPE')
                    if banner_type:
                        if banner_type!='' and banner_type=='is_video':
                            is_video = True
                            img = ''
                            VIDEO_TYPE = request.POST.get('VIDEO_TYPE')                            
                            if VIDEO_TYPE == 'youtube':
                                is_youtube = True
                                is_vimeo = False
                                video_url = request.POST.get('youtube')
                            elif VIDEO_TYPE == 'vimeo':
                                is_vimeo = True
                                is_youtube = False
                                video_url = request.POST.get('vimeo')
                            else:
                                video_url = ''
                                is_youtube = False
                                is_vimeo = False
                        else:
                            img = request.FILES.get('img')
                            if img:
                                img = img
                                is_video = False
                                is_youtube = False
                                is_vimeo = False
                                video_url = ''
                            else:
                                img = ''
                                is_video = False
                                is_youtube = False
                                is_vimeo = False
                                video_url = ''
                                
                    else:                        
                        messages.error(request, 'BANNER Type Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    if request.POST['target']!='':
                        target = request.POST['target']
                    else:
                        messages.error(request, 'Redirect To URL Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

              
                    author = request.user
                    BANNERList.objects.create(BANNERCat_id=BANNERCat_id, page_id=page_id, name=name, title=title, code=code, is_video=is_video, is_youtube=is_youtube, is_vimeo=is_vimeo, video_url=video_url, target=target, img=img, author=author)
                                        
                    messages.success(request, 'Created Successfully')
                    base_url = reverse('BANNERList')  
                    query_string =  urlencode({'is_draft': True}) 
                    url = '{}?{}'.format(base_url, query_string) 
                    return redirect(url)
                        
                except  Exception as e:
                    messages.error(request, f'{e}')
                    return redirect(request.META.get('HTTP_REFERER'))
            
            context = {
                'BANNERManager':'menu-open', 
                'CreateBANNERs': 'active', 
                'ALLBANNERList':ALLBANNERList,
                'ALLPAGEList':ALLPAGEList,
            }
            return render(request,"./template/banner/createBANNER.html", context)
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')

@accountant_required
def updateBANNER(request, slug):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            allBANNERList = BANNERCatList.objects.filter(is_active=True)
            BANNER = BANNERList.objects.get(slug=slug)
            ALLPAGEList = PAGEList.objects.filter(is_url=False, is_active=True, is_verified=True)

            if request.method == "POST":
                try:
                    name = request.POST.get('name') 
                    if name:
                        BANNER.name = name
                        BANNER.save()
                    
                    title = request.POST.get('title') 
                    if title:
                        BANNER.title = title
                        BANNER.save()
                        
                    code = request.POST.get('code') 
                    if code:
                        BANNER.code = code
                        BANNER.save()
                        
                    target = request.POST.get('target') 
                    if target:
                        BANNER.target = target
                        BANNER.save()
                        
                    page = request.POST.get('PAGEList')
                    if page:
                        BANNER.page_id = page
                    
                    
                    banner_type = request.POST.get('BANNER_TYPE')
                    if banner_type:
                        if banner_type!='' and banner_type=='is_video':
                            BANNER.is_video = True                            
                            VIDEO_TYPE = request.POST.get('VIDEO_TYPE')                            
                            if VIDEO_TYPE == 'youtube':
                                BANNER.is_youtube = True
                                BANNER.is_vimeo = False
                                BANNER.video_url = request.POST.get('youtube')
                                BANNER.save()
                            elif VIDEO_TYPE == 'vimeo':
                                BANNER.is_vimeo = True
                                BANNER.is_youtube = False
                                BANNER.video_url = request.POST.get('vimeo')
                                BANNER.save()
                            
                            elif VIDEO_TYPE == 'is_local':
                                BANNER.is_vimeo = False
                                BANNER.is_youtube = False
                                BANNER.is_local = True
                                BANNER.video_url = ''
                                BANNER.local_video = request.FILES.get('local_video')
                                BANNER.save()
                            else:
                                pass
                        else:
                            BANNER.is_video = False
                            BANNER.save()
                    else:
                        messages.error(request, 'BANNER Type Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    img = request.FILES.get('img')
                    if img:
                        BANNER.img = img
                        BANNER.save()
                 

                    BANNER.author = request.user
                    BANNER.last_update = timezone.now()
                    BANNER.save()
                    messages.success(request, 'Successfully Updated')
                    base_url = reverse('BANNERList')  
                    query_string =  urlencode({'is_draft': True}) 
                    url = '{}?{}'.format(base_url, query_string) 
                    return redirect(url)
                
                except Exception as e:
                    print(e)
                    messages.error(request, f'Error Occured')
                    return redirect(request.META.get('HTTP_REFERER'))
    
            context =  {
                'BANNERManager':'menu-open', 
                'allBANNER': 'active',
                'ALLPAGEList':ALLPAGEList,
                'ALLBANNERList':allBANNERList,
                'BANNER':BANNER,
            }
            return render(request, './template/banner/updateBANNER.html', context)   
        else:
            messages.error(request, f'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, f'You Dont Have Access')
        return redirect(request.META.get('HTTP_REFERER'))
# ==============================================================
# MOVE TO BIN BANNER
# ==============================================================
@accountant_required
def deleteBANNER(request, pk):
    if request.user.token == request.session['token']:
        try:
            BANNER = BANNERList.objects.get(pk=pk)
            BANNER.is_deleted = True
            BANNER.is_active = False
            BANNER.save()
            messages.success(request, 'Move to Bin Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# RESTORE BANNER FROM BIN
# ==============================================================
@accountant_required
def restoreBANNER(request, pk):
    if request.user.token == request.session['token']:
        try:
            BANNER = BANNERList.objects.get(pk=pk)
            BANNER.is_deleted = False
            BANNER.save()
            messages.success(request, 'Restore Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# PERMANENT DELETE BANNER
# ==============================================================
@superadmin_required
def PermanentDeleteBANNER(request, pk):
    if request.user.is_admin:
        try:
            BANNER = BANNERList.objects.get(pk=pk)
            BANNER.delete()
            messages.success(request, 'Permanent Deleted Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, 'Error Occured')
        return redirect(request.META['HTTP_REFERER'])

# ==============================================================
# ACTIVATED BANNER
# ==============================================================
@accountant_required
def activateBANNER(request, pk):
    if request.user.token == request.session['token']:
        try:
            BANNER = BANNERList.objects.get(pk=pk)
            BANNER.is_draft = False
            BANNER.is_active = True
            BANNER.is_verified = True
            BANNER.save()
            messages.success(request, 'Activate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# DEACTIVATED BANNER
# ==============================================================
@accountant_required
def deactivateBANNER(request, pk):
    if request.user.token == request.session['token']:
        try:
            BANNER = BANNERList.objects.get(pk=pk)
            BANNER.is_draft = False
            BANNER.is_active = False
            BANNER.save()
            messages.success(request, 'Deactivate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404


