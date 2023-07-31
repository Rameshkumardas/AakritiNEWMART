from rest_framework.views import APIView
from rest_framework.response import Response
from Accounts.models import UserRegistration
from django.contrib.auth import logout
from rest_framework import status
import datetime

class USERLogOut(APIView):
    def patch(self, request):
        pNumber = request.data.get('pNumber')
        try:
            UserRegistration.objects.filter(pNumber__iexact= pNumber).update(login_status=0, logout_date=datetime.datetime.now().strftime("%d, %B - %Y"))
            return Response({
                    "status":status.HTTP_200_OK,
                    "message": "LogOut Success", 
                })
        except UserRegistration.DoesNotExist:
            return Response({
                    "status":status.HTTP_400_BAD_REQUEST,
                    "message": "USER NOT DoseNotExist", 
                })
