from decouple import config
from django.shortcuts import render, redirect
from AdminAuthentication.Thread import EmailThread   
from django.contrib import messages
from AdminAuthentication.models import AdminRegistration
def AccountVerification(request, token):
    try:                                
        user = AdminRegistration.objects.get(token=token)
        user.is_user=True
        user.is_active=True
        user.is_verified=True
        user.login_block=False
        user.is_draft=False
        user.save()
        messages.success(request, 'Successfully Activated')
        context = {
            'user':user,
        }
        return render(request, './template/USERVerified.html', context)
    except Exception as e:
        messages.error(request, 'Error Occured')
        return redirect('/')

def CREATE_NEW_USER(request):
    try:                                        
        return render(request, './template/account/sign-up.html', )
    except Exception as e:
        print(e)
        messages.error(request, 'Error Occured')
        return redirect('/')

def FORGOT_USER_ACCOUNT(request):
    try:                                        
        return render(request, './template/account/forgot-password.html', )
    except Exception as e:
        print(e)
        messages.error(request, 'Error Occured')
        return redirect('/')