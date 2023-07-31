from AdminAuthentication.decorators import superadmin_required
from django.shortcuts import render, redirect



@superadmin_required
def GeneralSettings(request):
    if request.user.token == request.session['token']:
        context = {
            'extraSettings': 'menu-open', 
            'GeneralSettings': 'active'
        }
        return render(request,"./template/generalSettings.html", context)
    else:
        return redirect("AdminLogOut")

@superadmin_required
def EmailTemplateConfigs(request):
    if request.user.token == request.session['token']:
        context = {
            'extraSettings': 'menu-open', 
            'EmailTemplateConfig': 'active'
        }
        return render(request,"./template/email-template-config.html", context)
    else:
        return redirect("AdminLogOut")

@superadmin_required
def Notifications(request):
    if request.user.token == request.session['token']:
        context = {
            'extraSettings': 'menu-open', 
            'Notification': 'active'
        }
        return render(request,"./template/contact-us-list.html", context)
    else:
        return redirect("AdminLogOut")

@superadmin_required
def NewsletterList(request):
    if request.user.token == request.session['token']:
        context = {
            'extraSettings': 'menu-open', 
            'Newsletter': 'active'
            }
        return render(request,"./template/newsletter.html", context)
    else:
        return redirect("AdminLogOut")





