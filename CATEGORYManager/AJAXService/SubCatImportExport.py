from AdminAuthentication.decorators import admin_required, manager_required
from AdminAuthentication.models import AdminActivity
from ..utils import SubCatListResource
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from tablib import Dataset
@manager_required
def SubCatImport(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_accountant and request.user.token == request.session['token']:
            try:
                if request.method == 'POST':
                    file_format = request.POST.get('fileformatIMPORT')
                    subCat = SubCatListResource()                
                    dataset = Dataset()
                    getIMPORT_DATA = request.FILES.get('importData')                
                    if file_format == 'CSV':
                        data = dataset.load(getIMPORT_DATA.read().decode('utf-8'), format='csv')
                        subCat.import_data(data, dry_run=False)  
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ CSV  SUB CAT LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'CSV Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                    elif file_format == 'JSON':
                        getJSON = dataset.load(getIMPORT_DATA.read().decode('utf-8'),format='json')
                        subCat.import_data(getJSON, dry_run=False) 
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ JSON  SUB CAT LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'JSON Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                    elif file_format == 'XLS (Excel)':
                        data = dataset.load(getIMPORT_DATA.read())
                        subCat.import_data(data, dry_run=False) 
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ EXCEL  SUB CAT LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'Excel Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})
                    else:
                        getJSON = dataset.load(getIMPORT_DATA.read().decode('utf-8'),format='json')
                        subCat.import_data(getJSON, dry_run=False) 
                        AdminActivity.objects.create(admin=request.user, log=f'<span class="text-success"> [ JSON  SUB_CAT LIST ] - Imported<span>')
                        return JsonResponse({'status':1, 'message':'JSON Successfully Import', 'Reload':request.META.get('HTTP_REFERER')})



                else:
                    return JsonResponse({'status':0, 'message':'Bad Request'})
            except Exception:
                    return JsonResponse({'status':0, 'message':'Error Occured'})
        else:
            return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Acceess'})

@admin_required
def SubCatExport(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.user.is_admin and request.user.token == request.session['token']:
            dataset = SubCatListResource().export()
            if request.method == 'POST':
                file_format = request.POST['fileformat']
                if file_format == 'CSV':
                    response = HttpResponse(dataset.csv, content_type='text/csv')
                    response['Content-Disposition'] = f'attachment; filename="CSV__SUB_CAT_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.csv"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ CSV  SUB_CAT LIST ] - Exported<span>')
                    return response

                elif file_format == 'JSON':
                    response = HttpResponse(dataset.json, content_type='application/json')
                    response['Content-Disposition'] = f'attachment; filename="JSON__SUB_CAT_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ JSON  SUB_CAT LIST ] - Exported<span>')
                    return response                
                elif file_format == 'XLS (Excel)':
                    response = HttpResponse(dataset.xls, content_type='application/ms-excel')
                    response['Content-Disposition'] = f'attachment; filename="EXCEL__SUB_CAT_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.xls"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ EXCEL  SUB_CAT LIST ] - Exported<span>')
                    return response   
                else:
                    response = HttpResponse(dataset.json, content_type='application/json')
                    response['Content-Disposition'] = f'attachment; filename="JSON__SUB_CAT_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                    AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ JSON  SUB_CAT LIST ] - Exported<span>')
                    return response                
            else:
                response = HttpResponse(dataset.json, content_type='application/json')
                response['Content-Disposition'] = f'attachment; filename="JSON__SUB_CAT_LIST-{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}.json"'
                AdminActivity.objects.create(admin=request.user, log=f'<span class="text-danger"> [ JSON  SUB_CAT LIST ] - Exported<span>')
                return response                
        else:
            return HttpResponse({'status':0, 'message':'You Dont Have Access'})
    else:
        return HttpResponse({'status':0, 'message':'Bad Request'})
    



