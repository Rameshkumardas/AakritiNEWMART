from django.shortcuts import render
from django.views import View

# Error Handler
def error404(request, exception):
    context = {'exception':exception}
    return render(request, './templates/error/404.html', context)

def error500(request, *args, **argv):
    return render(request, './templates/error/500.html', status=500)

def error403(request, exception):

        return render(request,'./templates/error/403.html')

def error400(request,  exception):
        return render(request,'./templates/error/400.html')  

def check(request):
    pass
