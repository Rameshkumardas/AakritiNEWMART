
# from django import template
# from SEALSManager.models import ProductOrderList
# from CommonModules.models import REGIONList
# from PRODUCTManager.models import ProductList, ProductMyCart
# import requests
# import json


# register = template.Library()
# # ============INVOICE Manager================
# # ============INVOICE Manager================
# @register.simple_tag
# def orderPRICE(pk):
#     order = ProductOrderList.objects.get(pk=pk)
#     return order.amount
    

# @register.simple_tag
# def orderGST(pCode, product, order):
#     response = requests.get(f"https://api.postalpincode.in/pincode/{pCode}/")
#     pinCode_Info = json.loads(response.text)
#     if(pinCode_Info[0]['Status']== 'Success'):
#         localSTATE = pinCode_Info[0]['PostOffice'][0]['State']
#         try:
#             REGIONList.objects.get(pcode=pCode)
#             GST = GoodsandServicesTax.objects(product_id=product)
#             return GST.igst
            
#         except REGIONList.DoesNotExist:
#             if(localSTATE == 'Delhi'):
#                 try:
#                     GST = GoodsandServicesTax.objects.get(product_id=product)
#                     orderINVOICE = ProductOrderList.objects.get(pk=order)
#                     totalGST = float(GST.cgst+GST.sgst)
#                     subtotal = float(orderINVOICE.pricelist)
                    
#                     onlyGST = (subtotal/100)*totalGST

#                     GSTonly = round(onlyGST, 2)


#                     return f"CGST: {GST.cgst} % - SGST: {GST.sgst}% \n\n Total GST: {GSTonly}"
#                 except GoodsandServicesTax.DoesNotExist:
#                     return 'Error'
#             elif(localSTATE != 'Delhi'):

#                 try:
                    
#                     GST = GoodsandServicesTax.objects.get(product_id=product)
#                     orderINVOICE = ProductOrderList.objects.get(pk=order)
#                     totalGST = float(GST.igst)
#                     subtotal = float(orderINVOICE.pricelist)
#                     onlyGST = (subtotal/100)*totalGST

#                     GSTonly = round(onlyGST, 2)
#                     return f"IGST: {GoodsandServicesTax.objects.get(product_id=product).igst} % \n Total IGST: {GSTonly}"
#                 except GoodsandServicesTax.DoesNotExist:
#                     return 'Error'
#             else:
#                 try:
#                     return f"IGST: {GoodsandServicesTax.objects.get(product_id=product).igst} %"
#                 except GoodsandServicesTax.DoesNotExist:
#                     return 'Error'

#     elif pinCode_Info[0]['Status']== 'Error':
#         return 'Error'
#     else:
#         return 'Error'
        


# @register.simple_tag
# def getGST(orderId):
#     order = ProductOrderList.objects.filter(orderId=orderId)
#     return order

    

# @register.simple_tag
# def invoiceGST(orderId):
#     order = ProductOrderList.objects.filter(orderId=orderId)
#     return order


# @register.simple_tag
# def SHIPPING(orderId):
#     order = ProductOrderList.objects.filter(orderId=orderId)
#     return order
    

# @register.simple_tag
# def TOTAL(orderId):
#     order = ProductOrderList.objects.filter(orderId=orderId)
#     return order

