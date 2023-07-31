from AdminAuthentication.decorators import accountant_required, superadmin_required 
from AdminAuthentication.models import AdminActivity
from ExtraSettings.models import PROJECTInformation
from django.shortcuts import render, redirect
from ExtraSettings.models import PROJECTInformation
from django.conf import settings

from django.contrib import messages
import subprocess
import os

path = settings.BASE_DIR

file = '../requirements.txt'
FilePath = os.path.join(settings.BASE_DIR, file)
isPath = os.path.isfile(FilePath)
# ==============================================================================
# DEACTIVATED BLOG MAIN CATEGORY
# ==============================================================================
@superadmin_required
def CREATEREQUIRMENT_TXTSettings(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_superadmin and request.user.token == request.session['token']:
            # cmd = f'source /home/developer/SARAJ/EducationOZYMed/Education/OZYMedCMS/Venv/bin/activate; pip freeze > {FilePath}'
            cmd = f'pip freeze > {FilePath}'
            try:
                if isPath:
                    subprocess.call(cmd, shell=True)
                else:
                    f = open(FilePath, "x")
                    subprocess.call(cmd, shell=True)
                    f.close()   
                messages.success(request, 'Requirements.txt Created Successfully')
                return redirect(request.META['HTTP_REFERER'])
            except Exception as e:
                f = open(FilePath, "x")
                subprocess.call(f"pip freeze > {FilePath}", shell=True)
                f.close()   
                messages.error(request, 'Error Occured')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    else:
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")