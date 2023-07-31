from django.shortcuts import render
from CATEGORYManager.models import SubCategory, SubSubCategory



def LoadSubCatList(request):
    context = {
        'subCats': SubCategory.objects.filter(mainCat_id=request.POST['mainCat'], is_active=True)
        }
    print(context)
    return render(request, './template/subCatDropdownList.html', context)

def LoadSubSubCatList(request):
    context = {
        'subCats': SubSubCategory.objects.filter(subCat_id=request.POST['subCat'], is_active=True)
        }
    return render(request, './template/subCatDropdownList.html', context)
