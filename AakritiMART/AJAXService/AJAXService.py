import re
from django.contrib.auth.decorators import login_required
from AdminAuthentication.decorators import accountant_required
from AdminAuthentication.models import AdminRegistration
from PRODUCTManager.models import COMPAREProducts, PRODUCTAList, PRODUCTQList, ProductMyWishlist, ProductMyCart, ProductRatting
from django.http import HttpResponse, JsonResponse

valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

# ==============================================================================
# PRODUCT ADD Wishlist 
# ==============================================================================
@login_required
def addToCart(request):
    target = request.POST.get('targetVAL')
    if(target == ""):
        return JsonResponse({'status':0, 'message':'Target Required*'})
    else:
        try:            
            qty = request.POST.get('qty')
            mrp = request.POST.get('total_mrp')
            sp = request.POST.get('total_sp')
            attribute_name = request.POST.get('attribute_name')
            if ProductMyCart.objects.filter(user_id=request.user.pk, product_id=target).exists():
                return JsonResponse({'status':0, 'message':'This Product Already Exists'})
            else:
                AFTERTask = f"{request.META.get('HTTP_REFERER')}"
                ProductMyCart.objects.create(user_id=request.user.pk, product_id=target, qty=qty) 
                return JsonResponse({'status':1, 'message':'Added To Cart ',  "AFTERTask":AFTERTask })
        except Exception as e:
            print(e)
            return JsonResponse({'status':0, 'message':f'{e} Error Occured'})

@login_required
def deleteCart(request):
    target = request.POST.get('getOBJ')    
    if(target == ""):
        return JsonResponse({'status':0, 'message':'Target Required*'})
    else:
        try:
            ProductMyCart.objects.get( pk=target, user_id=request.user.pk).delete()
            AFTERTask = f"{request.META.get('HTTP_REFERER')}"
            return JsonResponse({"status":1, "message":"Deleted Successfully", "AFTERTask":AFTERTask,})
        except Exception:
            return JsonResponse({'status':0, 'message':f'Error Occured'})
# ==============================================================================

@login_required
def updateCART(request):
    target = request.POST.get('targetVAL')    
    qty = request.POST.get('qty')    
    if(target == ""):
        return JsonResponse({'status':0, 'message':'Target Required*'})
    else:
        try:
            ProductMyCart.objects.filter(user_id=request.user.pk, product_id=target).update(qty=qty)
            AFTERTask = f"{request.META.get('HTTP_REFERER')}"
            return JsonResponse({"status":1, "message":"Cart Update Successfully", 'AFTERTask':AFTERTask})
        except Exception:
            return JsonResponse({'status':0, 'message':f'Error Occured'})
# ==============================================================================





# ==============================================================================
# PRODUCT ADD Wishlist 
# ==============================================================================
@login_required
def addToWishlist(request):
    target = request.POST.get('targetVAL')
    if(target == ""):
        return JsonResponse({'status':0, 'message':'Target Required*'})
    else:
        try:
            if ProductMyWishlist.objects.filter(user_id=request.user.pk, product_id=target).exists():
                return JsonResponse({'status':0, 'message':'Already Exists Wishlist'})
            else:
                ProductMyWishlist.objects.create(user_id=request.user.pk, product_id=target) 
                return JsonResponse({'status':1, 'message':'Added To Wishlist '})
        except Exception:
            return JsonResponse({'status':0, 'message':f'Error Occured'})

@login_required
def deleteWishlistProduct(request):
    target = request.POST.get('targetVAL')    
    pk = request.POST.get('pk')
    if(target == ""):
        return JsonResponse({'status':0, 'message':'Target Required*'})
    else:
        try:
            ProductMyWishlist.objects.get(pk=pk, user_id=request.user.pk, product_id=target).delete()
            AFTERTask = f"{request.META.get('HTTP_REFERER')}"
            return JsonResponse({"status":1, "message":"Successfully Deleted", "AFTERTask":AFTERTask,})
        except Exception:
            return JsonResponse({'status':0, 'message':f'Error Occured'})
# ==============================================================================

# ==============================================================================
# ==============================================================================
# PRODUCT Compare Product
# ==============================================================================
@login_required
def COMPAREProduct(request):
    target = request.POST.get('targetVAL')
    if(target == ""):
        return JsonResponse({'status':0, 'message':'Target Required*'})
    else:
        try:
            if COMPAREProducts.objects.filter(user_id=request.user.pk, product_id=target).exists():
                return JsonResponse({'status':0, 'message':'Already Exists'})
            else:
                COMPAREProducts.objects.create(user_id=request.user.pk, product_id=target) 
                return JsonResponse({'status':1, 'message':'Added To Compare'})
        except Exception:
            return JsonResponse({'status':0, 'message':f'Error Occured'})
# ==============================================================================
# ==============================================================================
# ==============================================================================
# DELETE COMPARE PRODUCT
# ==============================================================================
@login_required
def deleteCOMPAREProduct(request):
    target = request.POST.get('targetVAL')    
    pk = request.POST.get('pk')
    if(target == ""):
        return JsonResponse({'status':0, 'message':'Target Required*'})
    else:
        try:
            COMPAREProducts.objects.get(pk=pk, user_id=request.user.pk, product_id=target).delete()
            AFTERTask = f"{request.META.get('HTTP_REFERER')}"
            return JsonResponse({"status":1, "message":"Successfully Deleted", "AFTERTask":AFTERTask,})
        except Exception:
            return JsonResponse({'status':0, 'message':f'Error Occured'})
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# DELETE COMPARE PRODUCT
# ==============================================================================
def WRITEREVIEWRequest(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        Ratting = request.POST.get('ratting')
        message = request.POST.get('message')
        product_id = request.POST.get('product_id')
        print("fname", fname) 
        AFTERTask = f"{request.META.get('HTTP_REFERER')}"
        check_email = re.compile(valid_email)
        if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
            ProductRatting.objects.create(product_id=int(product_id), user_id=request.user.pk, Ratting=Ratting, message=message)
            return JsonResponse({"status":1, "message":"Thanks For Review", "AFTERTask":AFTERTask,})
        else:
            if(re.search(check_email, email)):
                try:
                    user = AdminRegistration.objects.get(email=email)
                except Exception:
                    user = AdminRegistration.objects.create(email=email, fname=fname, lname=lname,)
                    
                ProductRatting.objects.create(product_id=int(product_id), user_id=user.pk, Ratting=Ratting, message=message)
                return JsonResponse({"status":1, "message":"Thanks For Review", "AFTERTask":AFTERTask,})
            else:                
                return JsonResponse({"status":0, "message":"Email Not Valid"})

# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ASK QUESTION PRODUCT
# ==============================================================================
def ASKQuestion(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        product_id = request.POST.get('product_id')
        AFTERTask = f"{request.META.get('HTTP_REFERER')}"
        check_email = re.compile(valid_email)

        if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
            PRODUCTQList.objects.create(product_id=int(product_id), user_id=request.user.pk, message=message)
            return JsonResponse({"status":1, "message":"Thanks For Ask Question", "AFTERTask":AFTERTask,})
        else:
            if(re.search(check_email, email)):
                try:
                    user = AdminRegistration.objects.get(email=email)
                except Exception:
                    user = AdminRegistration.objects.create(email=email, fname=fname, lname=lname,)
                PRODUCTQList.objects.create(product_id=int(product_id), user_id=user.pk, message=message)
                return JsonResponse({"status":1, "message":"Thanks For Ask Question", "AFTERTask":AFTERTask,})
            else:                
                return JsonResponse({"status":0, "message":"Email Not Valid"})


# 

# ==============================================================================
# ==============================================================================
# ASK QUESTION PRODUCT
# ==============================================================================
@login_required
def QUICKASKQuestion(request):
    if request.method == "POST":
        message = request.POST.get('message')
        product_id = request.POST.get('product_id')
        AFTERTask = f"{request.META.get('HTTP_REFERER')}"

        if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
            PRODUCTQList.objects.create(product_id=int(product_id), user_id=request.user.pk, message=message)
            return JsonResponse({"status":1, "message":"Thanks For Ask Question", "AFTERTask":AFTERTask,})
        else:                
            return JsonResponse({"status":0, "message":"Not Valid Request"})
    else:                
        return JsonResponse({"status":0, "message":"Not Valid Request"})


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ASK QUESTION PRODUCT
# ==============================================================================
@accountant_required
def ReplyQuestionWithAnswer(request):
    if request.method == "POST":
        question_id = request.POST.get('question')
        message = request.POST.get('message')
        AFTERTask = f"{request.META.get('HTTP_REFERER')}"
        PRODUCTAList.objects.create(q_id=question_id, user_id=request.user.pk, message=message)
        return JsonResponse({"status":1, "message":"Thanks For Ask Question", "AFTERTask":AFTERTask,})
    else:                
        return JsonResponse({"status":0, "message":"Not Valid Request"})
        
# ==============================================================================
# MORE ACCTIONS
# ==============================================================================
@accountant_required
def DELETEQA(request):
    try:                   
        if request.method == "POST":
            qa_for = request.POST.get('_for')
            qa_id = request.POST.get('qa_id') 
            if qa_for == "q":
                try:
                    obj = PRODUCTQList.objects.get(pk=qa_id)
                    obj.delete()
                    return JsonResponse({'status':1, 'message':'Delete Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
                except Exception as e:
                    return JsonResponse({'status':0, 'message':f'{e} Error Occured'})
            elif qa_for == "a":
                try:
                    obj = PRODUCTAList.objects.get(pk=qa_id)
                    obj.delete()
                    return JsonResponse({'status':1, 'message':'Delete Successfully', 'AFTERTask':request.META.get('HTTP_REFERER')})
                except Exception as e:
                    return JsonResponse({'status':0, 'message':f'Error Occured'})
            else:
                return JsonResponse({'status':0, 'message':'Not Valid Request'})         
        else:
            return JsonResponse({'status':0, 'message':'Not Valid Request'})
    except Exception:
        return JsonResponse({'status':0, 'message':'BError Occured'})


import requests
import json

def CheckShipping(request):    
    pinCode = request.POST.get('pinCode')    
    if(pinCode == ""):
        return JsonResponse({'status':0, 'message':'PinCode Required*'})
    else:
        try:            
            response = requests.get(f"https://api.postalpincode.in/pincode/{pinCode}/")
            pinCode_Info = json.loads(response.text)
            if(pinCode_Info[0]['Status']== 'Success'):
                City_Name = pinCode_Info[0]['PostOffice'][0]['Name']
                request.session['PinCode'] = pinCode
                request.session['city'] = City_Name
                
                AFTERTask = f"{request.META.get('HTTP_REFERER')}"
                return JsonResponse({"status":1, "message":"Let Me Check Shipping", "AFTERTask":AFTERTask,})

            elif pinCode_Info[0]['Status']== 'Error':
                return JsonResponse({'status':0, 'message':f'Not Valid PinCode'})
            else:
                return JsonResponse({'status':0, 'message':f'Not Valid Request'})
        except Exception as e:
            print(e)
            return JsonResponse({'status':0, 'message':f'{e} Error Occured'})
