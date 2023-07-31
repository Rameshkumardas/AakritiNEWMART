from Accounts.models import UserRegistration, USERINFORMATIONS, UserIMG, USERshippingADDRESS, USERbillingADDRESS
from Accounts.api.serializers import getUSERStatusSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

        
class getUSERProfile(APIView):
    def get(self, request, pNumber, format=None):
        try:
            targetModel = UserRegistration.objects.get(pNumber=pNumber)
            serializer = getUSERStatusSerializer(targetModel)
            return Response({
                            "Status" : status.HTTP_200_OK,
                            "message":"Data Loaded",
                            'userPROFILE':serializer.data
                        })  
        except USERbillingADDRESS.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"User DoesNotExist",
                        }) 

