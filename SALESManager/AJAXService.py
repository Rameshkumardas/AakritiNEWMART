from SALESManager.HELPERS import ORDER_WITH_LOGIN, ORDER_WITHOUT_LOGIN, SYSTEMGENERATEORDERID
from Accounts.HELPERS import GENERATE_ONE_TIME_VERIFICATION_CODE, GENERATEOTP, USER_ACCESS_GRANTED, SYSTEMGENERATEPASSWORD
from Accounts.models import billingADDRESS, shippingADDRESS
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
            print(is_success)
            if (is_success):
                try:                    
                    jsonOBJ = request.POST.get('jsonOBJ')    
                    if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
                        try:
                            orderId, Created = ORDER_WITH_LOGIN(request, jsonOBJ) 
                            print(Created)
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
# ==============================================================================
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ==============================================================================
# ==============================================================================
# GENERATE  NEW ORDER USING PAYPAL
# ==============================================================================
# ==============================================================================
def ORDER_GENERATE_WITH_PAYPAL(request):
    host = request.get_host()
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('your-return-view')),
        "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }
       
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the `business` field. (The user could tamper with
        # that fields on the payment form before it goes to PayPal)
        if ipn_obj.receiver_email != "receiver_email@example.com":
            # Not a valid payment
            return
        # ALSO: for the same reason, you need to check the amount
        # received, `custom` etc. are all what you expect or what
        # is allowed.

        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "premium_plan":
            price = 234
        else:
            price = 23
        if ipn_obj.mc_gross == price and ipn_obj.mc_currency == 'USD':
            pass
    else:
        pass
        #...
        
    # if request.method == 'POST':
    #     amount = request.POST.get('amount')
    #     netAmount = float(amount)*100
    #     if netAmount == '' or netAmount == None:
    #         return JsonResponse({'status':0, 'message': 'Please Add Amount'})
    #     else:
    #         try:
    #             payment_order = PRODUCT.order.create(dict(amount=netAmount, currency= "INR", payment_capture=1))
    #             order_id = payment_order['id']
    #             context = {
    #                 'status':1,
    #                 'message':'Order Created', 
    #                 'amount':netAmount,
    #                 "currency": "INR", 
    #                 'order_id':order_id,
    #             }
    #             return JsonResponse(context)    
    #         except Exception as e:
    #             print(e)
    #             return JsonResponse({'status':0, 'message': f'{e} - Error Occured'})
# ==============================================================================
# PAYMENT VERIFICATION WITH RAZORPAY
# ==============================================================================
def PAYMENT_VERIFICATION_WITH_PAYPAL(request):
    if request.method == 'POST':
        try:
            jsonOBJ = request.POST.get('jsonOBJ')    
            obj = json.loads(jsonOBJ)
            razorpay_order_id = obj['razorpay_order_id']
            razorpay_payment_id = obj['razorpay_payment_id']
            razorpay_signature = obj['razorpay_signature']
            params_dict = {
                        'razorpay_order_id': razorpay_order_id,
                        'razorpay_payment_id': razorpay_payment_id,
                        'razorpay_signature': razorpay_signature,
                    }
            is_success = PRODUCT.utility.verify_payment_signature(params_dict)
            if (is_success and is_success == True):
                try:                    
                    jsonOBJ = request.POST.get('jsonOBJ')    
                    if request.session.has_key('AakritiMARTusername') or request.session.has_key('SUPERADMIN'):
                        try:
                            Created = ORDER_WITH_LOGIN(request, jsonOBJ) 
                            if Created:
                                AFTERTask = f"{request.META.get('HTTP_REFERER')}"
                                return JsonResponse({'status':1, 'message': 'Order Confirmed', 'AFTERTask':f'{AFTERTask}'})
                            else:
                                return JsonResponse({'status':0, 'message': f'Error Occured'})      
                        except Exception as e:
                            print("Error", e)
                            return JsonResponse({'status':0, 'message': f'{e} Error Occured'})      
                    else:          
                        try:
                            Created = ORDER_WITHOUT_LOGIN(request, jsonOBJ) 
                            if Created:
                                AFTERTask = f"{request.META.get('HTTP_REFERER')}"
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
# ==============================================================================
# ==============================================================================
# END RAZORPAY OPERATION 
# ==============================================================================
# ==============================================================================
# ==============================================================================

# PAYMENT VERIFICATION WITH RAZORPAY
# ==============================================================================
def PAYMENT_SUCCESS_WITH_PAYPAL(request):
    if request.session.has_key('KHANTAILORusername') or request.session.has_key('SUPERADMIN'):
        if request.method == 'POST':
            try:
                billing = request.POST.get('billing')     
                print(billing);       
                if (billing):
                    try:
                        billingAddress = billingADDRESS.objects.get(pk=int(billing))              
                        billing_pinCode = billingAddress.bcode
                        billing_houseNo = billingAddress.bhouse_no
                        billing_landmark = billingAddress.blandmark
                        billing_city = billingAddress.bcity
                        billing_state = billingAddress.bstate
                        billing_country = billingAddress.bcountry
                    except Exception:
                        pass
                    
                shipping = request.POST.get('shipping')
                print(shipping);       

                if (shipping):
                    try:
                        shippingAddres = shippingADDRESS.objects.get(pk=int(2))
                        shipping_pinCode = shippingAddres.scode
                        shipping_houseNo = shippingAddres.shouse_no
                        shipping_landmark = shippingAddres.slandmark
                        shipping_city = shippingAddres.scity
                        shipping_state = shippingAddres.sstate
                        shipping_country = shippingAddres.scountry
                        shipping_more = shippingAddres.more
                    except Exception:
                        pass
                else:
                    shipping_pinCode = billingAddress.bcode
                    shipping_houseNo = billingAddress.bhouse_no
                    shipping_landmark = billingAddress.blandmark
                    shipping_city = billingAddress.bcity
                    shipping_state = billingAddress.bstate
                    shipping_country = billingAddress.bcountry
                    shipping_more = 'No Thanks'

                qty = request.POST.get('qty')
                color = request.POST.get('color')
                properties = request.POST.get('properties')
                subTotal = request.POST.get('subtotal')
                GSTTotal = request.POST.get('gst')
                ShippingTotal = request.POST.get('shipping')
                discount = request.POST.get('discount')
                total = request.POST.get('total')
                orderId = SYSTEMGENERATEORDERID(request)
                project = PROJECTInformation.objects.last()

                context = {
                    'user':request.user
                }
                checkoutFor = request.POST.get('checkoutFor')
                if checkoutFor != 'myCartList' and checkoutFor =='singleProduct':
                    slug = request.POST.get('product')
                    if(slug and slug !='' and slug !="undefine"):
                        product = ProductList.objects.get(is_active=True, slug=slug)
                        ProductOrderList.objects.create(user_id=request.user.pk, product_id=product.pk, orderId=orderId, amount=product.sp, discount=discount, qty=qty, color=color,  shipping=ShippingTotal, total=total, scode=shipping_pinCode, shouse_no=shipping_houseNo, slandmark=shipping_landmark, scity=shipping_city, sstate=shipping_state, scountry=shipping_country, more=shipping_more, bcode=billing_pinCode, bhouse_no=billing_houseNo, blandmark=billing_landmark, bcity=billing_city, bstate=billing_state, bcountry=billing_country, payMethod="Online", is_payment=True, is_otp=000000)
                elif checkoutFor == 'myCartList':
                    productList = ProductMyCart.objects.filter(user_id=request.user.pk)
                    for product in productList:
                        ProductOrderList.objects.create(user_id=request.user.pk, product_id=product.product.pk, orderId=orderId, amount=product.product.sp, discount=discount, qty=product.qty, color=product.color,  total=total, shipping=ShippingTotal, scode=shipping_pinCode, shouse_no=shipping_houseNo, slandmark=shipping_landmark, scity=shipping_city, sstate=shipping_state, scountry=shipping_country, more=shipping_more, bcode=billing_pinCode, bhouse_no=billing_houseNo, blandmark=billing_landmark, bcity=billing_city, bstate=billing_state, bcountry=billing_country, payMethod="Online", is_payment=True, is_otp=00000)

                    ProductMyCart.objects.filter(user_id=request.user.pk).delete()
                
                CONFIG_SMTP_NO_REPLY()
                html_content = render_to_string("template/email/orderConfirmation.html", context)
                recipient_list = [request.user.email, ]
                EmailThread(f'Order Confirmation || {config("PROJECT_NAME")}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()  
                return JsonResponse({'status':1, 'message': 'Order Successfully Confirmed', 'OrderId':orderId})                
            except Exception as e:
                print(e)
                return JsonResponse({'status':0, 'message': f'{e} Error Occured'})                           
    else:
        return JsonResponse({'status':0, 'message': f'Plz Login First'})












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