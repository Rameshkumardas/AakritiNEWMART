from SALESManager.HELPERS import ORDER_WITH_LOGIN, ORDER_WITHOUT_LOGIN, SYSTEMGENERATEORDERID
from Accounts.HELPERS import GENERATE_ONE_TIME_VERIFICATION_CODE, GENERATEOTP, USER_ACCESS_GRANTED, SYSTEMGENERATEPASSWORD
from Accounts.models import  shippingADDRESS
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY
from django.contrib.auth import authenticate, login, logout
from PRODUCTManager.models import ProductList, ProductMyCart
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.models import ST_PP_COMPLETED
from ExtraSettings.models import PROJECTInformation
from django.template.loader import render_to_string
from AdminAuthentication.Thread import EmailThread
from SALESManager.models import ProductOrderList
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from decouple import config
import razorpay
import requests
import uuid
import json
import re 

PRODUCT = razorpay.Client(auth=(config("RAZORPAY_API_KEY"), config("RAZORPAY_API_SECRET")))
valid_email= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
valid_phone = '^\\+?[1-9][0-9]{7,14}$'
# ==============================================================================
# COD VERIFICATION CODE
compiled_email = re.compile(valid_email)
compiled_phone = re.compile(valid_phone)
# ==============================================================================
# ==============================================================================
# ==============================================================================
# COD ORDER GENERATE
# ==============================================================================
def COD_ORDER_GENERATE(request):
    jsonOBJ = request.POST.get('jsonOBJ')
    obj = json.loads(jsonOBJ)
    if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):        
        is_generated = GENERATE_ONE_TIME_VERIFICATION_CODE(request, obj['email'])
        if is_generated:
            return JsonResponse({'status':1, 'message': 'Sent Verification Code'})
        else:
            return JsonResponse({'status':0, 'message': 'Email Not Valid'})  
    else:
        is_generated = GENERATE_ONE_TIME_VERIFICATION_CODE(request, obj['email'])
        if is_generated:
            return JsonResponse({'status':1, 'message': 'Sent Verification Code'})
        else:
            return JsonResponse({'status':0, 'message': 'Email Not Valid'})
# ==============================================================================
# CONFIRM AND VERIFY COD ORDER 
# ==============================================================================
def COD_ORDER_CONFIRM_AND_VERIFY(request): 
    vCode = request.POST.get('onetime_verification_code')
    if vCode == request.session['OneTimeVerificationCode']:  
        jsonOBJ = request.POST.get('jsonOBJ')    
        if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
            try:
               orderId, Created = ORDER_WITH_LOGIN(request, jsonOBJ) 
               if Created:
                    AFTERTask = f"{orderId}"
                    return JsonResponse({'status':1, 'message': 'Order Confirmed', 'AFTERTask':f'{AFTERTask}'})
               else:
                    return JsonResponse({'status':0, 'message': f'Error Occured'})      
            except Exception as e:
                print("Error", e)
                return JsonResponse({'status':0, 'message': f'{e} Error Occured'})      
        else:          
            try:
                orderId, Created = ORDER_WITHOUT_LOGIN(request, jsonOBJ) 
                if Created:
                    AFTERTask = f"{orderId}"
                    return JsonResponse({'status':1, 'message': 'Order Confirmed', 'AFTERTask':f'{AFTERTask}'})
                else:
                    return JsonResponse({'status':0, 'message': f'{Created} Error Occured'})      
            except Exception as e:
                print("Error", e)
                return JsonResponse({'status':0, 'message': f'{e} Error Occured'})      
    else:
        return JsonResponse({'status':0, 'message':'OTP Not Valid*'})      
# ==============================================================================
# END COD CONFIRM AND VERIFY COD ORDER  
# ==============================================================================
# ==============================================================================
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# GENERATE  NEW ORDER USING RAZORPAY 
# ==============================================================================
def ORDER_GENERATE_WITH_RAZORPAY(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        netAmount = float(amount)*100
        if netAmount == '' or netAmount == None:
            return JsonResponse({'status':0, 'message': 'Please Add Amount'})
        else:
            try:
                payment_order = PRODUCT.order.create(dict(amount=netAmount, currency= "INR", payment_capture=1))
                order_id = payment_order['id']
                context = {
                    'status':1,
                    'message':'Order Created', 
                    'amount':netAmount,
                    "currency": "INR", 
                    'order_id':order_id,
                }
                return JsonResponse(context)    
            except Exception as e:
                print(e)
                return JsonResponse({'status':0, 'message': f'{e} - Error Occured'})
# ==============================================================================
# PAYMENT VERIFICATION WITH RAZORPAY
# ==============================================================================
def PAYMENTVERIFICATIONWITHRAZORPAY(request):
    if request.method == 'POST':
        try:
            jsonOBJ = request.POST.get('jsonOBJ')   
            obj = json.loads(jsonOBJ)
            print("obj", obj['payMethod']) 
            razorpay_order_id = obj['razorpay_order_id']
            razorpay_payment_id = obj['razorpay_payment_id']
            razorpay_signature = obj['razorpay_signature']
            params_dict = {
                        'razorpay_order_id': razorpay_order_id,
                        'razorpay_payment_id': razorpay_payment_id,
                        'razorpay_signature': razorpay_signature,
                    }
            is_success = PRODUCT.utility.verify_payment_signature(params_dict)
            if (is_success):
                try:                    
                    if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
                        try:
                            orderId, Created = ORDER_WITH_LOGIN(request, jsonOBJ) 
                            print(Created)
                            if Created:
                                return JsonResponse({'status':1, 'message': 'Order Confirmed', 'AFTERTask':orderId})
                            else:
                                return JsonResponse({'status':0, 'message': f'Error Occured'})      
                        except Exception as e:
                            print("Error", e)
                            return JsonResponse({'status':0, 'message': f'{e} Error Occured'})      
                    else:          
                        try:
                            orderId, Created = ORDER_WITHOUT_LOGIN(request, jsonOBJ) 
                            if Created:
                                AFTERTask = f"{orderId}"
                                return JsonResponse({'status':1, 'message': 'Order Confirmed', 'AFTERTask':f'{AFTERTask}'})
                            else:
                                return JsonResponse({'status':0, 'message': f'Error Occured'})      
                        except Exception as e:
                            print("Error", e)
                            return JsonResponse({'status':0, 'message': f'{e} Error Occured'})                          
                except Exception as e:
                    return JsonResponse({'status':0, 'message': f'{e} Error Occured'})                           
            else:
                return JsonResponse({'status':0, 'message': 'Payment Not Recived'}) 
        except Exception as e:
            return JsonResponse({'status':0, 'message': f'{e} - Error Occured'})
# =============================================================================
# =============================================================================
# END RAZORPAY PAYMENT VERIFICATION 
# ==============================================================================
# ==============================================================================



# ====================================================================
# =================WORKING FINE=================
# ====================================================================
def SHIPPEDTHISPRODUCT_BY_US(request):
    if request.session.has_key('SUPERADMIN') and request.session.has_key('ADMIN-PASS') and request.session.has_key('ADMIN-ROLE'):
        if request.method == 'POST':            
            order_id = request.POST.get('order_id')
            getTrakingURL = request.POST.get('getTrakingURL')
            if (order_id ==''):
                return JsonResponse({'status':0, 'message':'Order Id Required From Backend*'})   
            if (getTrakingURL ==''):
                return JsonResponse({'status':0, 'message':'Traking Link Required*'}) 
            try:
                order = ProductOrderList.objects.get(pk=order_id)
                if (getTrakingURL):
                    order.is_shipped = True
                    order.track = getTrakingURL
                    order.save()
                    print("After Ship Status Updated", order.is_shipped)
                    print("After Traking Link Status Updated", order.track)
                    AFTERTask = f"{request.META.get('HTTP_REFERER')}"
                return JsonResponse({'status':1, 'message':'Order Successfully Shipped', 'AFTERTask':AFTERTask}) 
            except Exception:
                return JsonResponse({'status':0, 'message':'Error Occured'})      
    else:
        return JsonResponse({'status':0, 'message':'You Dont Have Access'})      
# ======================================================================================
# ======================================================================================
# ======================================================================================
#