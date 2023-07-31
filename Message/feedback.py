
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from Message.models import Feedback
from django.contrib import messages
# =========================feedbackLIST========================
# =========================feedbackLIST========================
# =========================feedbackLIST========================
# =========================feedbackLIST========================
# =========================feedbackLIST========================
# =========================feedbackLIST========================
# =========================feedbackLIST========================
# =========================feedbackLIST========================
@login_required
def feedbackLIST(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        feedbacklist = Feedback.objects.all().order_by('-id')
        context = {
            'Message': 'menu-open', 
            'feedback': 'active', 
            'feedbacklist':feedbacklist
        }
        return render(request,"./template/feedback/feedbackLIST.html", context)
    else:
        return redirect("AdminLogOut")

# =========================FEEDBACK LIST OPERATION========================
@login_required
def deleteFEEDBACK(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session.has_key('ADMIN-ROLE')==1:
            try:
                deleteFEEDBACK = Feedback.objects.get(pk=pk)
                deleteFEEDBACK.delete()
                messages.success(request, 'Delete successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
            except Feedback.DoesNotExist:
                messages.error(request, 'User-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')

@login_required
def activatedFEEDBACK(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session.has_key('ADMIN-ROLE')==1:
            try:
                action = Feedback.objects.get(pk=pk)
                action.status=1
                action.save()
                messages.success(request, 'Activated successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
            except Feedback.DoesNotExist:
                messages.error(request, 'User-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')

@login_required
def deactivatedFEEDBACK(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session.has_key('ADMIN-ROLE')==1:
            try:
                action = Feedback.objects.get(pk=pk)
                action.status=0
                action.save()
                messages.success(request, 'Deactivated Successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
            except Feedback.DoesNotExist:
                messages.error(request, 'User-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')

@login_required
def rejectedFEEDBACK(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.session.has_key('ADMIN-ROLE')==1:
            try:
                action = Feedback.objects.get(pk=pk)
                action.status=0
                action.save()
                messages.success(request, 'Deactivated Successfully')
                return redirect(request.META.get('HTTP_REFERER'))
            except ValueError as e:
                messages.error(request, f'{e}')
                return redirect(request.META.get('HTTP_REFERER'))
            except Feedback.DoesNotExist:
                messages.error(request, 'User-DoesNotExist')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'You Dont Have Access')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('AdminLogOut')

        