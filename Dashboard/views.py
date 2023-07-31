
from AdminAuthentication.decorators import accountant_required
from django.shortcuts import render, redirect
from django.contrib import messages


@accountant_required()
def DefaultDashboard(request):
    try:
        if request.user.token == request.session['token']:
            context = {
                'dashboard':'menu-open', 
                'default': 'active'
            }
            return render(request,"./template/defaultDashboard.html", context )
        else:
            messages.error(request, 'Please Login First')
            return redirect("AdminLogOut")
    
    except Exception as e:
        print(e)
        messages.error(request, 'Please Login First')
        return redirect("AdminLogOut")