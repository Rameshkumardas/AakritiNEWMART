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
class ALLREPLACEMENTList(ListView):
    paginate_by = 20
    template_name = './template/REPLACEMENTSTATUS.html'
    context_object_name = 'REPLACEMENTList'
    extra_context = { 'RCRManager':'menu-open', 'allREPLACEMENTS': 'active'}
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
# MOVE TO BIN REPLACEMENT
# ==============================================================
@accountant_required
def deleteREPLACEMENT(request, pk):
    if request.user.token == request.session['token']:
        try:
            REPLACEMENT = RCRREQUESTList.objects.get(pk=pk)
            REPLACEMENT.is_deleted = True
            REPLACEMENT.is_active = False
            REPLACEMENT.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {REPLACEMENT.product.name} ] - REPLACEMENT Deleted<span>')
            messages.success(request, 'Move to Bin Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# RESTORE REPLACEMENT FROM BIN
# ==============================================================
@accountant_required
def restoreREPLACEMENT(request, pk):
    if request.user.token == request.session['token']:
        try:
            REPLACEMENT = RCRREQUESTList.objects.get(pk=pk)
            REPLACEMENT.is_deleted = False
            REPLACEMENT.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {REPLACEMENT.product.name} ] - REPLACEMENT Restored<span>')
            messages.success(request, 'Restore Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# PERMANENT DELETE REPLACEMENT
# ==============================================================
@superadmin_required
def PermanentDeleteREPLACEMENT(request, pk):
    if request.user.is_admin:
        try:
            REPLACEMENT = RCRREQUESTList.objects.get(pk=pk)
            REPLACEMENT.delete()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {REPLACEMENT.product.name} ] - REPLACEMENT Deleted<span>')
            messages.success(request, 'Permanent Deleted Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        messages.error(request, 'Error Occured')
        return redirect(request.META['HTTP_REFERER'])

# ==============================================================
# ACTIVATED REPLACEMENT
# ==============================================================
@accountant_required
def activateREPLACEMENT(request, pk):
    if request.user.token == request.session['token']:
        try:
            REPLACEMENT = RCRREQUESTList.objects.get(pk=pk)
            REPLACEMENT.is_draft = False
            REPLACEMENT.is_active = True
            REPLACEMENT.is_verified = True
            REPLACEMENT.last_update = timezone.now()
            REPLACEMENT.date = timezone.now()
            REPLACEMENT.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ {REPLACEMENT.product.name} ] - REPLACEMENT Activated<span>')
            messages.success(request, 'Activate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# DEACTIVATED REPLACEMENT
# ==============================================================
@accountant_required
def deactivateREPLACEMENT(request, pk):
    if request.user.token == request.session['token']:
        try:
            REPLACEMENT = RCRREQUESTList.objects.get(pk=pk)
            REPLACEMENT.is_draft = False
            REPLACEMENT.is_active = False
            REPLACEMENT.last_update = timezone.now()
            REPLACEMENT.save()
            AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ {REPLACEMENT.product.name} ] - REPLACEMENT Deactivated<span>')
            messages.success(request, 'Deactivate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404

