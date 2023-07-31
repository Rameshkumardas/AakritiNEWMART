
from AdminAuthentication.decorators import superadmin_required
from django.shortcuts import render, redirect

@superadmin_required
def CMSSettings(request):
    if request.user.token == request.session['token']:
        context = {
            'CMSManager': 'menu-open', 
            'CMSSettings': 'active'
        }
        return render(request,"./template/manageMCS.html", context)
    else:
        return redirect("AdminLogOut")
