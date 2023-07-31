
from AdminAuthentication.decorators import superadmin_required
from AdminAuthentication.models import AdminRegistration
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib import messages
from django.http import Http404
from django.db.models import Q
# ==============================================================
# CHAPTER LIST CLASS
# ==============================================================
@method_decorator(superadmin_required, name='dispatch')
class ALLUSERList(ListView):
    paginate_by = 5
    template_name = './template/user/userSTATUS.html'
    ordering = ['id'] 
    context_object_name = 'USERList'
    extra_context = { 'USERManager':'menu-open', 'ALLUSER': 'active'}
    def get_queryset(self, *args, **kwargs):
        is_draft = self.request.GET.get('is_draft', 'is_draft')
        is_verified = self.request.GET.get('is_verified', 'is_verified')
        is_login = self.request.GET.get('is_login', 'is_login')
        is_deleted = self.request.GET.get('is_deleted', 'is_deleted')
        
        search = self.request.GET.get('search')

        if is_draft == 'True':
            if search:
                return AdminRegistration.objects.filter(is_draft=True).exclude(is_deleted=True).exclude(is_accountant=True).filter(Q(email__icontains=search))
            else:
                return AdminRegistration.objects.filter(is_draft=True).exclude(is_deleted=True).exclude(is_accountant=True)

        elif is_verified == 'True':
            if search:
                return AdminRegistration.objects.filter(is_active=True, is_verified=True, is_draft=False, is_deleted=False).exclude(is_accountant=True).filter(Q(email__icontains=search))
            else:
                return AdminRegistration.objects.filter(is_active=True, is_verified=True, is_draft=False, is_deleted=False).exclude(is_accountant=True)
        
        elif is_login == 'True':
            if search:
                return AdminRegistration.objects.filter(is_active=False, is_verified=True, is_draft=False, is_login=True).exclude(is_deleted=True).exclude(is_accountant=True).filter(Q(email__icontains=search))
            else:
                return AdminRegistration.objects.filter(is_active=False, is_verified=True, is_draft=False, is_login=True).exclude(is_deleted=True).exclude(is_accountant=True)
                
        elif is_deleted == 'True':
            if search:
                return AdminRegistration.objects.filter(is_deleted=True).exclude(is_accountant=True).filter(Q(email__icontains=search))
            else:
                return AdminRegistration.objects.filter(is_deleted=True).exclude(is_accountant=True)
        else:
            return AdminRegistration.objects.filter().exclude(is_accountant=True)

    def get_paginate_by(self, queryset):
        filter = self.request.GET.get('filter')
        if filter:
            return self.request.GET.get("paginate_by", filter)
        else:            
            return self.request.GET.get("paginate_by", self.paginate_by)


# ==============================================================
# MOVE TO BIN USER
# ==============================================================
@superadmin_required
def deleteUSER(request, pk):
    if request.user.token == request.session['token']:
        try:
            USER = AdminRegistration.objects.get(pk=pk)
            USER.is_draft=False
            USER.is_active = False
            USER.is_deleted = True
            USER.save()
            messages.success(request, 'Move to Bin Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# RESTORE USER FROM BIN
# ==============================================================
@superadmin_required
def restoreUSER(request, pk):
    if request.user.token == request.session['token']:
        try:
            USER = AdminRegistration.objects.get(pk=pk)
            USER.is_deleted = False
            USER.is_draft = True
            USER.is_active = False
            USER.save()
            messages.success(request, 'Restore Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# PERMANENT DELETE USER
# ==============================================================
@superadmin_required
def PermanentDeleteUSER(request, pk):
    if request.user.token == request.session['token']:
        try:
            USER = AdminRegistration.objects.get(pk=pk)
            USER.delete()
            messages.success(request, 'Permanent Deleted Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# ACTIVATED USER
# ==============================================================
@superadmin_required
def activateUSER(request, pk):
    if request.user.token == request.session['token']:
        try:
            USER = AdminRegistration.objects.get(pk=pk)
            USER.is_draft = False
            USER.is_active = True
            USER.is_verified = True
            USER.save()
            messages.success(request, 'Activate Successfully')
            return redirect(request.META['HTTP_REFERER'])
        except Exception:
            messages.error(request, 'Error Occured')
            return redirect(request.META['HTTP_REFERER'])
    else:
        raise Http404
# ==============================================================
# DEACTIVATED USER
# ==============================================================
@superadmin_required
def deactivateUSER(request, pk):
    if request.user.token == request.session['token']:
        try:
            USER = AdminRegistration.objects.get(pk=pk)
            USER.is_draft = True
            USER.is_active = False
            USER.save()
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
