from django.conf import settings
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY, CONFIG_SMTP_SUPPORT
from AdminAuthentication.decorators import accountant_required, superadmin_required
from django.template.loader import render_to_string
from AdminAuthentication.models import AdminActivity
from BULKEMAILManager.BULKEMAILThread import EmailThread
from .models import EMAILList, EMAILTEMPLATEList
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import urlencode
from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from django.db.models import Q
from decouple import config

valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

    
# ==============================================================
# CHAPTER LIST CLASS
# ==============================================================
@method_decorator(accountant_required, name='dispatch')
class ALLEMAILTEMPLATEList(ListView):
    paginate_by = 15
    template_name = './template/EMAILTEMPLATESTATUS.html'
    context_object_name = 'EMAILTEMPLATEList'
    extra_context = { 'EMAILMarketing':'menu-open', 'allEMAILTEMPLATEList': 'active'}
    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_active = self.request.GET.get('is_active', 'is_active')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')          
        search = self.request.GET.get('search')  
        if is_draft == 'True':
            if search:
                return EMAILTEMPLATEList.objects.select_related('author').filter(Q(subject__icontains=search)).order_by('-id')
            else:
                return EMAILTEMPLATEList.objects.select_related('author').all().order_by('-id')

        elif is_verified == 'True':
            if search:
                return EMAILTEMPLATEList.objects.select_related('author').filter(Q(subject__icontains=search)).order_by('-id')
            else:
                return EMAILTEMPLATEList.objects.select_related('author').all().order_by('-id')
            
        elif is_active == 'False':
            if search:
                return EMAILTEMPLATEList.objects.select_related('author').filter(Q(subject__icontains=search)).order_by('-id')
            else:
                return EMAILTEMPLATEList.objects.select_related('author').all().order_by('-id')
            
        elif is_deleted == 'True':
            if search:
                return EMAILTEMPLATEList.objects.select_related('author').filter(Q(subject__icontains=search)).order_by('-id')
            else:            
                return EMAILTEMPLATEList.objects.select_related('author').all().order_by('-id')
        else:
            if search:
                return EMAILTEMPLATEList.objects.select_related('author').filter(Q(subject__icontains=search)).order_by('-id')
            else:
                return EMAILTEMPLATEList.objects.select_related('author').all().order_by('-id')
                
    def get_paginate_by(self, queryset):
        filter = self.request.GET.get('filter')
        if filter:
            return self.request.GET.get("paginate_by", filter)
        else:            
            return self.request.GET.get("paginate_by", self.paginate_by)
        


@accountant_required
def createEMAILTEMPLATE(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            if request.method=="POST":
                try:
                    target_set = request.POST.get('target_set')
                    if target_set:
                        target_set = int(target_set)
                    else:
                        messages.error(request, 'Target Set Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                    
                    status = request.POST.get('status')
                    
                    if status == 'is_draft':
                        TARGETList = list(EMAILTEMPLATEList.objects.select_related('author').filter(is_draft=True).exclude(is_deleted=True).values_list('email', flat=True)[:target_set])
                        
                    elif status == 'is_verified':
                        TARGETList = list(EMAILTEMPLATEList.objects.select_related('author').filter(is_active=True, is_verified=True, is_draft=False, is_deleted=False).values_list('email', flat=True)[:target_set])

                    elif status == 'is_deactive':
                        TARGETList = list(EMAILTEMPLATEList.objects.select_related('author').filter(is_active=False, is_draft=False).exclude(is_deleted=True).values_list('email', flat=True)[:target_set])

                    elif status == 'is_deleted':                 
                        TARGETList = list(EMAILTEMPLATEList.objects.select_related('author').filter(is_deleted=True).values_list('email', flat=True)[:target_set])
                    else:
                        messages.error(request, 'Send For Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

                    sender = request.POST.get('sender')
                    if sender == 'noreply':
                        CONFIG_SMTP_NO_REPLY()
                    elif sender == 'support':
                        CONFIG_SMTP_SUPPORT()
                    else:
                        messages.error(request, 'Sender Required*')
                        return redirect(request.META.get('HTTP_REFERER'))
                        
                    subject = request.POST.get('subject')
                    if subject:
                        subject = subject
                    else:
                        messages.error(request, 'Subject Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

                    description = request.POST.get('description')
                    if description:
                        description = description
                    else:
                        messages.error(request, 'Description Required*')
                        return redirect(request.META.get('HTTP_REFERER'))

                    context = {
                        'name' : request.user.name,
                        'project':{config("PROJECT_NAME")},
                        'subject':subject,
                        'description':description,
                    }
                    # ==================================================================================
                    html_content = render_to_string("./template/email/bulkEMAILTEMPLATE.html", context)
                    EmailThread(f'{subject}', settings.EMAIL_HOST_USER, html_content, TARGETList).start()
                    # ==================================================================================
                    # author = request.user
                    # EMAILTEMPLATEList.objects.create(name=name, email=email, contact=contact, author=author)
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {target_set} ] - Bulk EMAIL Sent<span>')
                    messages.success(request, 'Task Added Successfully')
                    base_url = reverse('EMAILTEMPLATEList')  
                    query_string =  urlencode({'is_draft': True}) 
                    url = '{}?{}'.format(base_url, query_string) 
                    # return redirect(url)
                    return redirect(request.META.get('HTTP_REFERER'))
                except  Exception as e:
                    print(e)
                    messages.error(request, f'{e}')
                    return redirect(request.META.get('HTTP_REFERER'))
            context = {
                    'EMAILMarketing':'menu-open', 
                    'CreateEMAILs': 'active', 
            }
            return render(request,"./template/createEMAIL.html", context)
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')

@accountant_required
def updateEMAILTEMPLATE(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                obj = EMAILTEMPLATEList.objects.get(pk=pk)
                if request.method=="POST":
                    subject = request.POST.get('subject')
                    if subject:
                        obj.subject = subject
                        obj.save()
                        
                    description = request.POST.get('description')
                    if description:
                        obj.description = description
                        obj.save()
                      
                    
                    messages.success(request, f'Update Successfylly')
                    base_url = reverse('EMAILTEMPLATEList')  
                    query_string =  urlencode({'is_draft': True}) 
                    url = '{}?{}'.format(base_url, query_string) 
                    return redirect(url)
                    # messages.success(request, f'Update Successfylly')
                    # return redirect(request.META.get('HTTP_REFERER'))

                context =  {
                    'EMAILMarketing':'menu-open', 
                    'updateEMAILTEMPLATE': 'active', 
                    'obj':obj,
                }
                return render(request, './template/updateEMAILTEMPLATE.html', context)  
            except Exception:
                messages.error(request, f'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, f'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, f'You Dont Have Access')
        return redirect(request.META.get('HTTP_REFERER'))

# ==============================================================
# SEND BULK EMAIL
# ==============================================================
@accountant_required
def sendEMAILTEMPLATE(request, pk):
    if request.user.token == request.session['token']:
        try:        
            template = EMAILTEMPLATEList.objects.get(pk=pk)    
            TARGETList = list(EMAILList.objects.select_related('author').filter(is_sent=False).values_list('email', flat=True)[:5])
            context = {
                'name' : request.user.name,
                'project':{config("PROJECT_NAME")},
                'subject':template.subject,
                'description':template.description,
            }            
            print("TARGETList", TARGETList)
            # ==================================================================================
            CONFIG_SMTP_NO_REPLY()
            html_content = render_to_string("./template/email/bulkEMAILTEMPLATE.html", context)
            # for email in TARGETList:
            EmailThread(f'{template.subject}', settings.EMAIL_HOST_USER, html_content, TARGETList).start()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ 50 ] - EMAIL Sent<span>')
            messages.success(request, 'Task Added Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404

# ==============================================================
# MOVE TO BIN EMAIL
# ==============================================================
@accountant_required
def deleteEMAILTEMPLATE(request, pk):
    if request.user.token == request.session['token']:
        try:
            EMAIL = EMAILTEMPLATEList.objects.get(pk=pk)
            EMAIL.is_deleted = True
            EMAIL.is_active = False
            EMAIL.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {EMAIL.subject} ] - EMAIL TEMPLATE Deleted<span>')
            messages.success(request, 'Move to Bin Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# RESTORE EMAIL FROM BIN
# ==============================================================
@accountant_required
def restoreEMAILTEMPLATE(request, pk):
    if request.user.token == request.session['token']:
        try:
            EMAIL = EMAILTEMPLATEList.objects.get(pk=pk)
            EMAIL.is_deleted = False
            EMAIL.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {EMAIL.subject} ] - EMAIL TEMPLATE Restored<span>')
            messages.success(request, 'Restore Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# PERMANENT DELETE EMAIL
# ==============================================================
@superadmin_required
def PermanentDeleteEMAILTEMPLATE(request, pk):
    if request.user.is_admin:
        try:
            EMAIL = EMAILTEMPLATEList.objects.get(pk=pk)
            EMAIL.delete()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {EMAIL.subject} ] - EMAIL TEMPLATE Deleted<span>')
            messages.success(request, 'Permanent Deleted Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception as e:
            messages.error(request, f'{e} Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, 'Error Occured')
        return redirect(request.META['HTTP_REFERER'])

# ==============================================================
# ACTIVATED EMAIL
# ==============================================================
@accountant_required
def activateEMAILTEMPLATE(request, pk):
    if request.user.token == request.session['token']:
        try:
            EMAIL = EMAILTEMPLATEList.objects.get(pk=pk)
            EMAIL.is_draft = False
            EMAIL.is_active = True
            EMAIL.is_verified = True
            EMAIL.last_update = timezone.now()
            EMAIL.date = timezone.now()
            EMAIL.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {EMAIL.subject} ] - EMAIL TEMPLATE Activated<span>')
            messages.success(request, 'Activate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# DEACTIVATED EMAIL
# ==============================================================
@accountant_required
def deactivateEMAILTEMPLATE(request, pk):
    if request.user.token == request.session['token']:
        try:
            EMAIL = EMAILTEMPLATEList.objects.get(pk=pk)
            EMAIL.is_draft = False
            EMAIL.is_active = False
            EMAIL.last_update = timezone.now()
            EMAIL.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {EMAIL.subject} ] - EMAIL TEMPLATE Deactivated<span>')
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
def LoadEMAILSubCatLIST(request):
    context = {
        'subCats': EMAILSubCat.objects.filter(mainCat_id=request.POST['mainCat'], is_active=True)
    }
    return render(request, './template/EMAILSubCategoryList.html', context)

