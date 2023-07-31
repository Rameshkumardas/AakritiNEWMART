from AdminAuthentication.decorators import accountant_required, superadmin_required
from AdminAuthentication.models import AdminActivity
from .models import REFUNDREQUESTList
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
class ALLREFUNDList(ListView):
    paginate_by = 20
    template_name = './template/REFUNDSTATUS.html'
    context_object_name = 'REFUNDList'
    extra_context = { 'REFUNDManager':'menu-open', 'allREFUNDS': 'active'}
    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_active = self.request.GET.get('is_active', 'is_active')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')        
        if is_draft == 'True':
            return REFUNDREQUESTList.objects.select_related('product').select_related('user').filter(is_draft=True).exclude(is_deleted=True).order_by('-id')
        elif is_verified == 'True':
            return REFUNDREQUESTList.objects.select_related('product').select_related('user').filter(is_active=True, is_verified=True, is_draft=False, is_deleted=False)
        elif is_active == 'False':
            return REFUNDREQUESTList.objects.select_related('product').select_related('user').filter(is_active=False, is_verified=True, is_draft=False).exclude(is_deleted=True)
        elif is_deleted == 'True':
            return REFUNDREQUESTList.objects.select_related('product').select_related('user').filter(is_deleted=True)
        else:
            return REFUNDREQUESTList.objects.select_related('product').select_related('user').all()
        

# ==============================================================
# MOVE TO BIN REFUND
# ==============================================================
@accountant_required
def deleteREFUND(request, pk):
    if request.user.token == request.session['token']:
        try:
            REFUND = REFUNDREQUESTList.objects.get(pk=pk)
            REFUND.is_deleted = True
            REFUND.is_active = False
            REFUND.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {REFUND.product.name} ] - REFUND Deleted<span>')
            messages.success(request, 'Move to Bin Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# RESTORE REFUND FROM BIN
# ==============================================================
@accountant_required
def restoreREFUND(request, pk):
    if request.user.token == request.session['token']:
        try:
            REFUND = REFUNDREQUESTList.objects.get(pk=pk)
            REFUND.is_deleted = False
            REFUND.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {REFUND.product.name} ] - REFUND Restored<span>')
            messages.success(request, 'Restore Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# PERMANENT DELETE REFUND
# ==============================================================
@superadmin_required
def PermanentDeleteREFUND(request, pk):
    if request.user.is_admin:
        try:
            REFUND = REFUNDREQUESTList.objects.get(pk=pk)
            REFUND.delete()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {REFUND.product.name} ] - REFUND Deleted<span>')
            messages.success(request, 'Permanent Deleted Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, 'Error Occured')
        return redirect(request.META['HTTP_REFERER'])

# ==============================================================
# ACTIVATED REFUND
# ==============================================================
@accountant_required
def activateREFUND(request, pk):
    if request.user.token == request.session['token']:
        try:
            REFUND = REFUNDREQUESTList.objects.get(pk=pk)
            REFUND.is_draft = False
            REFUND.is_active = True
            REFUND.is_verified = True
            REFUND.last_update = timezone.now()
            REFUND.date = timezone.now()
            REFUND.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {REFUND.product.name} ] - REFUND Activated<span>')
            messages.success(request, 'Activate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# DEACTIVATED REFUND
# ==============================================================
@accountant_required
def deactivateREFUND(request, pk):
    if request.user.token == request.session['token']:
        try:
            REFUND = REFUNDREQUESTList.objects.get(pk=pk)
            REFUND.is_draft = False
            REFUND.is_active = False
            REFUND.last_update = timezone.now()
            REFUND.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {REFUND.product.name} ] - REFUND Deactivated<span>')
            messages.success(request, 'Deactivate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404

