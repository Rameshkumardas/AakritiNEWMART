import datetime
from Accounts.HELPERS import GENERATEOTP, USER_ACCESS_GRANTED, SYSTEMGENERATEPASSWORD
from django.contrib.auth.decorators import login_required
from Accounts.models import shippingADDRESS
from AdminAuthentication.HELPER import CONFIG_SMTP_NO_REPLY
from django.contrib.auth import authenticate, login, logout
from PRODUCTManager.models import ProductList, ProductMyCart
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.models import ST_PP_COMPLETED
from django.urls import reverse
from django.shortcuts import render
from AdminAuthentication.models import AdminRegistration
from django.template.loader import render_to_string
from AdminAuthentication.Thread import EmailThread
from SALESManager.models import ProductOrderList
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from django.conf import settings
from decouple import config
import requests
import razorpay
import json
import re 
from SALESManager.models import ProductOrderList
from django.contrib.auth import logout
import array
import random
import uuid
from datetime import date

# ==============================================================================
# ==============================================================================
def SYSTEMGENERATEORDERID(request):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    #                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
    #                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    #                     'z']

    # UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    #                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
    #                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
    #                     'Z']


    # COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS
    COMBINED_LIST = DIGITS 

    rand_digit = random.choice(DIGITS)
    # rand_upper = random.choice(UPCASE_CHARACTERS)
    # rand_lower = random.choice(LOCASE_CHARACTERS)
    temp_ORDER_ID = rand_digit

    for x in range(4):
        temp_ORDER_ID = temp_ORDER_ID + random.choice(COMBINED_LIST)

        temp_ORDER_ID_list = array.array('u', temp_ORDER_ID)
        random.shuffle(temp_ORDER_ID_list)

    OrderId = config("PROJECT_NAME")+""

    for x in temp_ORDER_ID_list:
        OrderId = OrderId + x
        
    try:
        ProductOrderList.objects.get(orderId=OrderId)
        return SYSTEMGENERATEORDERID(request)
    except Exception:
        return OrderId

def get_orders(request, orderId):
    try:
        order = ProductOrderList.objects.get(user=request.user, orderId=orderId)
        return "single", order
    except Exception:
        all_orders = ProductOrderList.objects.filter(user=request.user, orderId=orderId)
        return "multiple", all_orders


def OrderPriceDetails(request, objs):
    SubTotal = []
    grandSHIPING = []
    grandGST = []
    grandDISCOUNT = []
    for order in objs:
        # print("ordered", order)
        # print("SubTotal.append((order.product.sp)*int(order.qty))", SubTotal.append((order.product.sp)*int(order.qty)))
        SubTotal.append((int(order.product.sp))*int(order.qty))
        totalSHIPPING = 20
        totalGST = 20
        grandSHIPING.append(totalSHIPPING)            
        grandGST.append(totalGST)
        grandDISCOUNT.append(((order.product.mrp)*int(order.qty))-((order.product.sp)*int(order.qty)))
    return sum(SubTotal), sum(grandSHIPING), sum(grandDISCOUNT), sum(SubTotal+grandSHIPING), objs
        



# ==============================================================================
# ==============================================================================
def ORDER_WITHOUT_LOGIN(request, jsonOBJ):
    orderId = SYSTEMGENERATEORDERID(request)
    obj = json.loads(jsonOBJ)
    try:
        user = AdminRegistration.objects.get(email=obj['email'])
    except Exception as e:
        user = AdminRegistration.objects.create(email=obj['email'], phone=obj['contact'], fname=obj['fname'], lname=obj['lname'], login_block=False, is_verified=True, is_active=True, is_login=True)

    if not billingADDRESS.objects.filter(user_id=user.pk, bcode=obj['pinCode']).exists():
        billing = billingADDRESS(user_id=user.pk, bcode=obj['pinCode'], bhouse_no=obj['house_no'], blandmark=obj['land_mark'], bcity=obj['city'], bstate=obj['state'], bcountry=obj['country'], more=obj['optional'])
        billing.save()  
    
    if not shippingADDRESS.objects.filter(user_id=user.pk, scode=obj['pinCode']).exists():
        shipping = shippingADDRESS(user_id=user.pk, scode=obj['pinCode'], shouse_no=obj['house_no'], slandmark=obj['land_mark'], scity=obj['city'], sstate=obj['state'], scountry=obj['country'], more=obj['optional'])
        shipping.save()

    if obj['payMethod'] == "COD":
        is_payment = False
    else:
        request.session['OneTimeVerificationEmail'] = obj['email']
        is_payment = True
        
    ProductOrderList.objects.create(user_id=user.pk, product_id=obj['product'], invoice=str(uuid.uuid4()), orderId=orderId, qty=obj['qty'], color=obj['color'], amount=int(obj['subtotal']), subtotal=int(obj['subtotal']), shipping=int(obj['shipping']), gst=int(obj['gst']), discount=int(obj['discount']), total=int(obj['total']),  bcode=obj['pinCode'], bhouse_no=obj['house_no'], blandmark=obj['land_mark'], bcity=obj['city'], bstate=obj['state'], bcountry=obj['country'], scode=obj['pinCode'], shouse_no=obj['house_no'], slandmark=obj['land_mark'], scity=obj['city'], sstate=obj['state'], scountry=obj['country'], more=obj['optional'], payMethod=obj["payMethod"], is_payment=is_payment, jsonOBJ=jsonOBJ)
    context = {
    
    }

    # CONFIG_SMTP_NO_REPLY()
    # requests.get(f"http://www.smsalert.co.in/api/push.json?apikey=62b2af4c1a5d7&route=transactional&sender=VOFREE&mobileno={contact}&text=Thanks%20for%20choosing%20Voicefreedom%20{orderId}%20Click%20Here.")
    # html_content = render_to_string("./template/account/email/OneTimeVerificationCode.html", context)
    # recipient_list = [obj['email'], ]
    # EmailThread(f'Order Confirmation || {config("PROJECT_NAME")}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()                
    
    is_login = USER_ACCESS_GRANTED(request)
    if is_login:
        return orderId, True    
    else:
        return False
# ==============================================================================
# ==============================================================================
@login_required
def ORDER_WITH_LOGIN(request, jsonOBJ):
    try:       
        orderId = SYSTEMGENERATEORDERID(request)
        obj = json.loads(jsonOBJ)
        if obj['payMethod'] == "COD":
            is_payment = False
            is_otp = 9999
        else:
            is_otp = 0000
            is_payment = True
        
        shipping_address = shippingADDRESS.objects.get(pk=int(obj['shipping_address']))
        
            
        print("obj", obj)

        if obj['checkout_for'] == "myCartList":
            productList = ProductMyCart.objects.filter(user_id=request.user.pk)
            invoice=str(uuid.uuid4())
            for cart in productList:   
                try:
                    ProductOrderList.objects.create(user_id=request.user.pk, product_id=cart.product.pk, invoice=invoice, orderId=orderId, qty=int(cart.qty), amount=cart.product.sp, subtotal=float(obj['subtotal']), shipping=float(obj['shipping']), gst=float(obj['gst']), discount=float(obj['discount']), total=float(obj['total']), code=shipping_address.code, house_no=shipping_address.house_no, landmark=shipping_address.landmark, city=shipping_address.city, state=shipping_address.state, country=shipping_address.country, fname=shipping_address.fname,lname=shipping_address.lname,email=shipping_address.email,contact=shipping_address.contact, payMethod=obj['payMethod'], is_payment=is_payment, is_otp=is_otp, jsonOBJ=jsonOBJ)
                except Exception:
                    return False
            ProductMyCart.objects.filter(user_id=request.user.pk).delete()            
        else:
            return False
        
        context = {
            "orders": ProductOrderList.objects.filter(orderId=orderId),
            'address':shipping_address,
            "OrderId":orderId,
            'invoice_date': date.today(),
            "fname":request.user.fname,
            "discount": obj['discount'],
            "subtotal": obj['subtotal'],
            "gst": float(obj['gst']),            
            "shipping": float(obj['shipping']),
            "total": float(obj['total']),

        }
        CONFIG_SMTP_NO_REPLY()
        html_content = render_to_string("./template/email/orderConfirmation.html", context)
        recipient_list = [request.user.email, ]
        EmailThread(f'Order Confirmation | {config("PROJECT_NAME")}', settings.EMAIL_HOST_USER, html_content, recipient_list).start()                
        return orderId, True
    except Exception as e:
        print(e)
        return False
# ==============================================================================
# ==============================================================================