from AdminAuthentication.decorators import accountant_required, superadmin_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from AdminAuthentication.models import AdminActivity, AdminRegistration
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.http import Http404

@accountant_required(login_url='AdminLogOut')
def AdminProfile(request):
    if request.user.token == request.session['token']:
        if request.method=="POST":
            ADMIN = AdminRegistration.objects.get(pk=request.user.pk)
            fullname = request.POST.get('fullname')
            if (fullname !='' and fullname!=ADMIN.name):
                ADMIN.name=fullname
                ADMIN.save()
                AdminActivity.objects.create(admin_id=request.user.pk, log="Full Name Updated")

            designation = request.POST.get('designation')
            if (designation !='' and designation != ADMIN.designation):
                ADMIN.designation=designation
                ADMIN.save()
                AdminActivity.objects.create(admin_id=request.user.pk, log="Designation Updated")

            img = request.FILES.get('img')
            if (img):
                ADMIN.img=img
                ADMIN.save()
                AdminActivity.objects.create(admin_id=request.user.pk, log="IMG Updated")

            
            experience = request.POST.get('experience')
            if (experience !='' and experience != ADMIN.experience):
                ADMIN.experience=experience
                ADMIN.save()
                AdminActivity.objects.create(admin_id=request.user.pk, log="Experience Updated")

            education = request.POST.get('education')
            if (education !='' and experience != ADMIN.experience):
                ADMIN.education=education
                ADMIN.save()
                AdminActivity.objects.create(admin_id=request.user.pk, log="Education Updated")

            address = request.POST.get('address')
            if (address !='' and address !=ADMIN.address):
                ADMIN.address=address
                ADMIN.save()
                AdminActivity.objects.create(admin_id=request.user.pk, log="Address Updated")
            
            skills = request.POST.get('skills')
            if (skills !='' and experience !=ADMIN.experience):
                ADMIN.skills=skills
                ADMIN.save()
                AdminActivity.objects.create(admin_id=request.user.pk, log="Skills Updated")

                    
            note = request.POST.get('note')
            if (note !='' and note!=ADMIN.note):
                ADMIN.note=note
                ADMIN.save()
                AdminActivity.objects.create(admin_id=request.user.pk, log="Notes Updated")


            oldpassword = request.POST.get('oldpassword')
            newpassword = request.POST.get('newpassword')
            repassword = request.POST.get('repassword')
            if (oldpassword !='' and newpassword !='' and repassword !=''):
                if newpassword == repassword:
                    matchCheck = check_password(newpassword, ADMIN.password)
                    if matchCheck:
                        ADMIN.password = make_password(newpassword)
                        ADMIN.save()
                        AdminActivity.objects.create(admin_id=request.user.pk, log="Password Updated")
                else:
                    messages.error(request, 'Password Not Match')
                    return redirect(request.META.get('HTTP_REFERER'))   
        
        page = request.GET.get('page', 1)
        try:
            log_list = AdminActivity.objects.select_related('admin').filter(admin_id=request.user.pk).order_by('-date')
            paginator = Paginator(log_list, 20)
            adminACTIVITY = paginator.page(page) 
        except PageNotAnInteger:
            adminACTIVITY = paginator.page(1)
        except EmptyPage:
            adminACTIVITY = paginator.page(paginator.num_pages)

        context = {
            'activityList': adminACTIVITY,
        }
        return render(request,"./template/admin/profile/adminPROFILE.html", context)
    else:   
        raise Http404


@superadmin_required
def deleteLOG(request, pk):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                AdminActivity.objects.filter(pk=pk).delete()
                AdminActivity.objects.create(admin=request.user, log='<span class="text-success">Deleted Single Log<span>')
                messages.success(request, 'Deleted Successfully')
                return redirect(request.META.get('HTTP_REFERER'))            
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))            
        else:   
            raise Http404
    else:   
        raise Http404

@superadmin_required
def deleteALLLOGS(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.token == request.session['token']:
            try:
                AdminActivity.objects.all().delete()
                AdminActivity.objects.create(admin=request.user, log='<span class="text-success">Deleted All Logs<span>')
                messages.success(request, 'All Activity Deleted')
                return redirect(request.META.get('HTTP_REFERER'))            
            except Exception:
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))            
        else:   
            raise Http404
    else:   
        raise Http404
