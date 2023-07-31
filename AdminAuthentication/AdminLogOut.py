from AdminAuthentication.decorators import accountant_required
from AdminAuthentication.models import AdminActivity, AdminRegistration
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY
from django.views.decorators.http import require_GET
from django.template.loader import render_to_string
from ExtraSettings.models import PROJECTInformation
from AdminAuthentication.Thread import EmailThread
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.utils import timezone
from django.conf import settings

valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
password_validator = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

@accountant_required
def AdminLogOut(request):
    try:
        admin = AdminRegistration.objects.get(email = request.user.email)
        admin.is_login = False
        admin.save()
        project = PROJECTInformation.objects.last()
        context = {
            'user':admin,
            'date': timezone.now(),
            'PROJECT':project,
        } 
        # ==================================================================================
        CONFIG_SMTP_NO_REPLY()
        html_content = render_to_string("./template/admin/email/adminLOGOUTSUSSCESS.html", context)
        recipient_list = [request.user.email, ]            
        EmailThread(f'Hi [ {request.user.name} ] - LOGOUT SUCCESS  || {project.name}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()
        # ==================================================================================
        AdminActivity.objects.create(admin_id=request.user.pk, log='<span class="text-danger">LogOut Success<span>')
        messages.success(request, f'Hi [ {admin.name} ] - LOGOUT SUCCESS')
        logout(request)
        return redirect('/')
    except Exception(AdminRegistration.DoesNotExist, PROJECTInformation.DoesNotExist):
        messages.success(request, f'Hi, Admin - LOGOUT SUCCESS')
        AdminActivity.objects.create(admin_id=request.user.pk, log='<span class="text-danger">LogOut Success<span>')
        logout(request)
        return redirect('/')

