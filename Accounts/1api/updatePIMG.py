from Accounts.models import UserRegistration, UserIMG
from Accounts.api.serializers import USERPIMGSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import datetime
from Message.models import EmailNewslatters
   

class updatePIMG(APIView):    
    def patch(self, request, format=None):
        mobileN= request.data.get('pNumber').replace('"', '')
        try:
            user = UserRegistration.objects.get(pNumber=mobileN)
            targetModel = UserIMG.objects.get(user_id=user.pk)
            serializer = USERPIMGSerializer(targetModel, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                                "Status" : status.HTTP_200_OK,
                                "message":"Profile IMG Updated",
                                'profileIMG':serializer.data,
                            })
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except UserRegistration.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"User DoesNotExist",
                        }) 
