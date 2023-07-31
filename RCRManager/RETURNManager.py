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
class ALLRETURNList(ListView):
    paginate_by = 20
    template_name = './template/RETURNSTATUS.html'
    context_object_name = 'RETURNList'
    extra_context = { 'RCRManager':'menu-open', 'allRETURNS': 'active'}
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
# MOVE TO BIN RETURN
# ==============================================================
@accountant_required
def deleteRETURN(request, pk):
    if request.user.token == request.session['token']:
        try:
            RETURN = RCRREQUESTList.objects.get(pk=pk)
            RETURN.is_deleted = True
            RETURN.is_active = False
            RETURN.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {RETURN.product.name} ] - RETURN Deleted<span>')
            messages.success(request, 'Move to Bin Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# RESTORE RETURN FROM BIN
# ==============================================================
@accountant_required
def restoreRETURN(request, pk):
    if request.user.token == request.session['token']:
        try:
            RETURN = RCRREQUESTList.objects.get(pk=pk)
            RETURN.is_deleted = False
            RETURN.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {RETURN.product.name} ] - RETURN Restored<span>')
            messages.success(request, 'Restore Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# PERMANENT DELETE RETURN
# ==============================================================
@superadmin_required
def PermanentDeleteRETURN(request, pk):
    if request.user.is_admin:
        try:
            RETURN = RCRREQUESTList.objects.get(pk=pk)
            RETURN.delete()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {RETURN.product.name} ] - RETURN Deleted<span>')
            messages.success(request, 'Permanent Deleted Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, 'Error Occured')
        return redirect(request.META['HTTP_REFERER'])

# ==============================================================
# ACTIVATED RETURN
# ==============================================================
@accountant_required
def activateRETURN(request, pk):
    if request.user.token == request.session['token']:
        try:
            RETURN = RCRREQUESTList.objects.get(pk=pk)
            RETURN.is_draft = False
            RETURN.is_active = True
            RETURN.is_verified = True
            RETURN.last_update = timezone.now()
            RETURN.date = timezone.now()
            RETURN.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {RETURN.product.name} ] - RETURN Activated<span>')
            messages.success(request, 'Activate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# DEACTIVATED RETURN
# ==============================================================
@accountant_required
def deactivateRETURN(request, pk):
    if request.user.token == request.session['token']:
        try:
            RETURN = RCRREQUESTList.objects.get(pk=pk)
            RETURN.is_draft = False
            RETURN.is_active = False
            RETURN.last_update = timezone.now()
            RETURN.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {RETURN.product.name} ] - RETURN Deactivated<span>')
            messages.success(request, 'Deactivate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404

