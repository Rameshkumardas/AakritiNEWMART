from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, OperationalError
from django.shortcuts import render, redirect
from Message.models import ContactUS
from django.contrib import messages
# =========================CONTACTED LIST========================
# =========================CONTACTED LIST========================
# =========================CONTACTED LIST========================
# =========================CONTACTED LIST========================
# =========================CONTACTED LIST========================
# =========================CONTACTED LIST========================
# =========================CONTACTED LIST========================
# =========================CONTACTED LIST========================
@login_required
def ContactedList(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        ContactedList = ContactUS.objects.filter(is_received=False)
        context = {
            'Message': 'menu-open',
            'Contacted': 'active', 
            'recivePendingContactedList':ContactedList
            
        }
        return render(request,"./template/contactedUS/contactedLISTSTATUS.html", context)
    else:
        return redirect("AdminLogOut")

@login_required
def ActiveContactedList(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        ContactedList = ContactUS.objects.filter(is_received=True, is_verified=True).order_by('-id')
        context = {
            'Message': 'menu-open',
            'Contacted': 'active', 
            'recivedContactedList':ContactedList
            
        }
        return render(request,"./template/contactedUS/contactedLISTSTATUS.html",context)
    else:
        return redirect("AdminLogOut")

@login_required
def DeactiveContactedList(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        ContactedList = ContactUS.objects.filter(is_rejected=True).order_by('-id')
        context = {
            'Message': 'menu-open', 
            'Contacted': 'active', 
            'rejectedContactedList':ContactedList
            }
        return render(request,"./template/contactedUS/contactedLISTSTATUS.html", context)
    else:
        return redirect("AdminLogOut")
# =========================CONTACTED LIST OPERATION========================
# =========================CONTACTED LIST OPERATION========================
# =========================CONTACTED LIST OPERATION========================
# =========================CONTACTED LIST OPERATION========================
# =========================CONTACTED LIST OPERATION========================
# =========================CONTACTED LIST OPERATION========================
# =========================CONTACTED LIST OPERATION========================
# =========================CONTACTED LIST OPERATION========================
@login_required
def deleteCONTACTED(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session.has_key('ADMIN-ROLE')==1:
            try:
                deleteCONTACTED = ContactUS.objects.get(pk=pk)
                deleteCONTACTED.delete()
                messages.success(request, 'Delete successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
            except ContactUS.DoesNotExist:
                messages.error(request, 'User-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')
    
@login_required
def activatedCONTACTED(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session.has_key('ADMIN-ROLE')==1:
            try:
                action = ContactUS.objects.get(pk=pk)
                action.is_received=True
                action.is_verified=True
                action.save()
                messages.success(request, 'Activated successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
            except ContactUS.DoesNotExist:
                messages.error(request, 'User-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')

@login_required
def deactivatedCONTACTED(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session.has_key('ADMIN-ROLE')==1:
            try:
                action = ContactUS.objects.get(pk=pk)
                action.is_received=False
                action.save()
                messages.success(request, 'Deactivated Successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
            except ContactUS.DoesNotExist:
                messages.error(request, 'User-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')

@login_required
def rejectedCONTACTED(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session.has_key('ADMIN-ROLE')==1:
            try:
                action = ContactUS.objects.get(pk=pk)
                action.is_rejected=False
                action.is_verified=False
                action.save()
                messages.success(request, 'Deactivated Successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
            except ContactUS.DoesNotExist:
                messages.error(request, 'User-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')

        

