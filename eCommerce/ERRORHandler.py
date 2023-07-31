from django.shortcuts import render
from django.views import View

def ERROR404(request, exception):
    context = {'exception':exception}
    return render(request, './template/error/404.html', context)

def ERROR500(request, *args, **argv):
    return render(request, './template/error/500.html', status=500)

def ERROR403(request, exception):
    return render(request,'./template/error/403.html')

def ERROR400(request,  exception):
    return render(request,'./template/error/400.html')  

def check(request):
    pass
