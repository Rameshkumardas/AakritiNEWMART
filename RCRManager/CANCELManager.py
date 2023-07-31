from AdminAuthentication.decorators import accountant_required, superadmin_required
from AdminAuthentication.models import AdminActivity
from .models import RCRREQUESTList
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
class ALLCANCELList(ListView):
    paginate_by = 20
    template_name = './template/CANCELSTATUS.html'
    context_object_name = 'CANCELList'
    extra_context = { 'RCRManager':'menu-open', 'allCANCELS': 'active'}
    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_active = self.request.GET.get('is_active', 'is_active')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')        
        if is_draft == 'True':
            return RCRREQUESTList.objects.select_related('order').filter(is_draft=True).exclude(is_deleted=True).order_by('-id')
        elif is_verified == 'True':
            return RCRREQUESTList.objects.select_related('order').filter(is_active=True, is_verified=True, is_draft=False, is_deleted=False)
        elif is_active == 'False':
            return RCRREQUESTList.objects.select_related('order').filter(is_active=False, is_verified=True, is_draft=False).exclude(is_deleted=True)
        elif is_deleted == 'True':
            return RCRREQUESTList.objects.select_related('order').filter(is_deleted=True)
        else:
            return RCRREQUESTList.objects.select_related('order').all()
        

# ==============================================================
# MOVE TO BIN CANCEL
# ==============================================================
@accountant_required
def deleteCANCEL(request, pk):
    if request.user.token == request.session['token']:
        try:
            CANCEL = RCRREQUESTList.objects.get(pk=pk)
            CANCEL.is_deleted = True
            CANCEL.is_active = False
            CANCEL.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {CANCEL.product.name} ] - CANCEL Deleted<span>')
            messages.success(request, 'Move to Bin Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# RESTORE CANCEL FROM BIN
# ==============================================================
@accountant_required
def restoreCANCEL(request, pk):
    if request.user.token == request.session['token']:
        try:
            CANCEL = RCRREQUESTList.objects.get(pk=pk)
            CANCEL.is_deleted = False
            CANCEL.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {CANCEL.product.name} ] - CANCEL Restored<span>')
            messages.success(request, 'Restore Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# PERMANENT DELETE CANCEL
# ==============================================================
@superadmin_required
def PermanentDeleteCANCEL(request, pk):
    if request.user.is_admin:
        try:
            CANCEL = RCRREQUESTList.objects.get(pk=pk)
            CANCEL.delete()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {CANCEL.product.name} ] - CANCEL Deleted<span>')
            messages.success(request, 'Permanent Deleted Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, 'Error Occured')
        return redirect(request.META['HTTP_REFERER'])

# ==============================================================
# ACTIVATED CANCEL
# ==============================================================
@accountant_required
def activateCANCEL(request, pk):
    if request.user.token == request.session['token']:
        try:
            CANCEL = RCRREQUESTList.objects.get(pk=pk)
            CANCEL.is_draft = False
            CANCEL.is_active = True
            CANCEL.is_verified = True
            CANCEL.last_update = timezone.now()
            CANCEL.date = timezone.now()
            CANCEL.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {CANCEL.product.name} ] - CANCEL Activated<span>')
            messages.success(request, 'Activate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# DEACTIVATED CANCEL
# ==============================================================
@accountant_required
def deactivateCANCEL(request, pk):
    if request.user.token == request.session['token']:
        try:
            CANCEL = RCRREQUESTList.objects.get(pk=pk)
            CANCEL.is_draft = False
            CANCEL.is_active = False
            CANCEL.last_update = timezone.now()
            CANCEL.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {CANCEL.product.name} ] - CANCEL Deactivated<span>')
            messages.success(request, 'Deactivate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404

