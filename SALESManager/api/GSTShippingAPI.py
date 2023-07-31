from GSTShipping.api.serializers import getLocalGSTANDSHIPPINGSerializer, getNationalGSTANDSHIPPINGSerializer, getRegionGSTANDSHIPPINGSerializer
from GSTShipping.models import GoodsandServicesTax
from rest_framework.decorators import api_view
from rest_framework.response import Response
from CommonModules.models import RegionList
from rest_framework import status
import requests
import json

@api_view(['GET'])
def getGSTANDSHIPPING(request, pinCode=None, product=None, QTY=None, *args, **kwargs):
    response = requests.get(f"https://api.postalpincode.in/pincode/{pinCode}/")
    pinCode_Info = json.loads(response.text)
    if(pinCode_Info[0]['Status']== 'Success'):
        localSTATE = pinCode_Info[0]['PostOffice'][0]['State']
        try:
            targetModel = GoodsandServicesTax.objects.get(product_id=product)
            try:
                RegionList.objects.get(pcode=pinCode)
                serializer = getRegionGSTANDSHIPPINGSerializer(targetModel, context={'QTY':QTY})
                return Response({"status":status.HTTP_200_OK, "message":"Region Area", "GSTSHIPPING":serializer.data})  
            except RegionList.DoesNotExist:
                if(localSTATE == 'Delhi'):
                    serializer = getLocalGSTANDSHIPPINGSerializer(targetModel, context={'QTY':QTY})
                    return Response({"status":status.HTTP_200_OK, "message":"Local Area", "GSTSHIPPING":serializer.data})  
                elif(localSTATE != 'Delhi'):
                    serializer = getNationalGSTANDSHIPPINGSerializer(targetModel, context={'QTY':QTY})
                    return Response({"status":status.HTTP_200_OK, "message":"National Area", "GSTSHIPPING":serializer.data})  
                else:
                    serializer = getLocalGSTANDSHIPPINGSerializer(targetModel, context={'QTY':QTY})
                    return Response({"status":status.HTTP_200_OK, "message":"Out Of Delhi", "GSTSHIPPING":serializer.data})
                
        except Exception as e:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message": f"{e} - Unknown Error",})  
    elif pinCode_Info[0]['Status']== 'Error':
        return Response({"status":status.HTTP_400_BAD_REQUEST,"message": "PinCode Not Valid",})  
    else:
        return Response({"status":status.HTTP_400_BAD_REQUEST,"message": "PinCode Not Valid",})  
