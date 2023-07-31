
from SALESManager.models import ProductOrderList
from CommonModules.models import REGIONList, SHIPPINGList
from PRODUCTManager.models import ProductList, ProductMyCart
import requests
import json


def getGST(pCode, product, qty):
    response = requests.get(f"https://api.postalpincode.in/pincode/{pCode}/")
    pinCode_Info = json.loads(response.text)
    try:
        GST = ProductList.objects.get(pk=product)
        if(pinCode_Info[0]['Status']== 'Success'):
            localSTATE = pinCode_Info[0]['PostOffice'][0]['State']
            try:
                REGIONList.objects.get(pcode=pCode)
                GST = ProductList.objects.get(pk=product)
                return ((GST.sp*GST.igst)/100)*qty            
            except REGIONList.DoesNotExist:
                GST = ProductList.objects.get(pk=product)
                if(localSTATE == 'Delhi'):
                    totalGST = GST.cgst + GST.sgst
                    print("totalGST", totalGST)
                    print("qty", qty)
                    print("SP", GST.sp)
                    print("Cal GST", ((GST.sp*totalGST)/100)*qty)
                    return ((GST.sp*totalGST)/100)*qty
                
                elif(localSTATE != 'Delhi'):
                    return ((GST.sp*GST.igst)/100)*qty
                else:
                    return ((GST.sp*GST.igst)/100)*qty
        elif pinCode_Info[0]['Status']== 'Error':
            return ((GST.sp*18)/100)*qty
        else:
            return ((GST.sp*18)/100)*qty
    except ProductList.DoesNotExist:
        return ((GST.sp*18)/100)*qty

def getSHIPPING(pCode, product, qty):
    try:
        shippingAttr = ProductList.objects.get(pk=product)
        response = requests.get(f"https://api.postalpincode.in/pincode/{pCode}/")
        pinCode_Info = json.loads(response.text)
        if(pinCode_Info[0]['Status']== 'Success'):
            localSTATE = pinCode_Info[0]['PostOffice'][0]['State']
            shippingCharge = 200
            try:
                REGIONList.objects.get(pcode=pCode)
                if (shippingAttr.dimension=='Dimensions'):
                    productLengthCM = shippingAttr.length
                    productWithCM = shippingAttr.width
                    productHightCM = shippingAttr.hight
                    Kg = ((productLengthCM*productWithCM*productHightCM)/4750)*int(qty)
                    shippingOBJ = SHIPPINGList.objects.filter(is_active=True, type='Dimensions')
                    for obj in shippingOBJ:
                        dBVal0 = obj.kg_range.replace("(", '')
                        dBVal1 = dBVal0.replace(")", "")
                        dBVal2 = dBVal1.replace("'", "")
                        dBVal3 = dBVal2.replace(" ", "")
                        dBVal = dBVal3.split(',')
                        if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
                            shippingCharge = obj.regional
                            break

                    return shippingCharge
                
                elif(shippingAttr.dimension=='Weight'):
                    productWeightGRM = shippingAttr.weight
                    Kg = int(productWeightGRM*1000)*int(qty)
                    shippingOBJ = SHIPPINGList.objects.filter(is_active=True, type='Weight')
                    for obj in shippingOBJ:
                        dBVal0 = obj.kg_range.replace("(", '')
                        dBVal1 = dBVal0.replace(")", "")
                        dBVal2 = dBVal1.replace("'", "")
                        dBVal3 = dBVal2.replace(" ", "")
                        dBVal = dBVal3.split(',')
                        if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
                            shippingCharge = obj.regional
                            break
                        
                    return shippingCharge
                else:
                    return 250.0  

            except REGIONList.DoesNotExist:
                if(localSTATE == 'Delhi'):
                    if (shippingAttr.dimension=='Dimensions'):
                        productLengthCM = shippingAttr.length
                        productWithCM = shippingAttr.width
                        productHightCM = shippingAttr.hight
                        Kg = ((productLengthCM*productWithCM*productHightCM)/4750)*int(qty)

                        shippingOBJ = SHIPPINGList.objects.filter(is_active=True, type='Dimensions')
                        for obj in shippingOBJ:
                            dBVal0 = obj.kg_range.replace("(", '')
                            dBVal1 = dBVal0.replace(")", "")
                            dBVal2 = dBVal1.replace("'", "")
                            dBVal3 = dBVal2.replace(" ", "")
                            dBVal = dBVal3.split(',')
                            if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
                                shippingCharge = obj.local
                                break
                        return shippingCharge
                    
                    elif(shippingAttr.dimension=='Weight'):
                        productWeightGRM = shippingAttr.weight
                        Kg = int(productWeightGRM*1000)*int(qty)
                        shippingOBJ = SHIPPINGList.objects.filter(is_active=True, type='Weight')
                        for obj in shippingOBJ:
                            dBVal0 = obj.kg_range.replace("(", '')
                            dBVal1 = dBVal0.replace(")", "")
                            dBVal2 = dBVal1.replace("'", "")
                            dBVal3 = dBVal2.replace(" ", "")
                            dBVal = dBVal3.split(',')
                            if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
                                shippingCharge = obj.local
                                break
                        return shippingCharge
                    else:
                        return 250.0  
                
                elif(localSTATE != 'Delhi'):
                    if (shippingAttr.dimension=='Dimensions'):
                        productLengthCM = shippingAttr.length
                        productWithCM = shippingAttr.width
                        productHightCM = shippingAttr.hight
                        Kg = ((productLengthCM*productWithCM*productHightCM)/4750)*int(qty)

                        shippingOBJ = SHIPPINGList.objects.filter(is_active=True, type='Dimensions')
                        for obj in shippingOBJ:
                            dBVal0 = obj.kg_range.replace("(", '')
                            dBVal1 = dBVal0.replace(")", "")
                            dBVal2 = dBVal1.replace("'", "")
                            dBVal3 = dBVal2.replace(" ", "")
                            dBVal = dBVal3.split(',')
                            if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
                                shippingCharge = obj.national
                                break
                        return shippingCharge
                    
                    elif(shippingAttr.dimension=='Weight'):
                        productWeightGRM = shippingAttr.weight
                        Kg = int(productWeightGRM*1000)*int(qty)
                        shippingOBJ = SHIPPINGList.objects.filter(is_active=True, type='Weight')
                        for obj in shippingOBJ:
                            dBVal0 = obj.kg_range.replace("(", '')
                            dBVal1 = dBVal0.replace(")", "")
                            dBVal2 = dBVal1.replace("'", "")
                            dBVal3 = dBVal2.replace(" ", "")
                            dBVal = dBVal3.split(',')
                            if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
                                shippingCharge = obj.national
                                break
                        return shippingCharge
                    else:
                        return 250.0          
                
                else:                    
                    if (shippingAttr.dimension=='Dimensions'):
                        productLengthCM = shippingAttr.length
                        productWithCM = shippingAttr.width
                        productHightCM = shippingAttr.hight
                        Kg = ((productLengthCM*productWithCM*productHightCM)/4750)*int(qty)

                        shippingOBJ = SHIPPINGList.objects.filter(is_active=True, type='Dimensions')
                        for obj in shippingOBJ:
                            dBVal0 = obj.kg_range.replace("(", '')
                            dBVal1 = dBVal0.replace(")", "")
                            dBVal2 = dBVal1.replace("'", "")
                            dBVal3 = dBVal2.replace(" ", "")
                            dBVal = dBVal3.split(',')
                            if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
                                shippingCharge = obj.special
                                break
                        return shippingCharge
                    
                    elif(shippingAttr.dimension=='Weight'):
                        productWeightGRM = shippingAttr.weight
                        Kg = int(productWeightGRM*1000)*int(qty)
                        shippingOBJ = SHIPPINGList.objects.filter(is_active=True, type='Weight')
                        for obj in shippingOBJ:
                            dBVal0 = obj.kg_range.replace("(", '')
                            dBVal1 = dBVal0.replace(")", "")
                            dBVal2 = dBVal1.replace("'", "")
                            dBVal3 = dBVal2.replace(" ", "")
                            dBVal = dBVal3.split(',')
                            if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
                                shippingCharge = obj.special
                                break
                        return shippingCharge
                    else:
                        return 250.0  
        
        elif pinCode_Info[0]['Status']== 'Error':
            return 50.00
        else:
            return 50.00
        
    except ProductList.DoesNotExist:
        return  250.0
