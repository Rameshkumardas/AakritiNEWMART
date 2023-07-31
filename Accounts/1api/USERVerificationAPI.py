from rest_framework.views import APIView
from rest_framework.response import Response
from Accounts.models import UserRegistration, mobileOTP
from rest_framework import status
from Message.models import MobileNewslatters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token



class USERVerification(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        userOTP = int(request.data.get('Vcode'))
        try:
            dbOTP = mobileOTP.objects.get(Vcode=userOTP).Vcode
            dBNumber = mobileOTP.objects.get(Vcode=userOTP).pNumber
            if(dbOTP==userOTP and dBNumber==request.data.get('pNumber')):
                usedOTP = mobileOTP.objects.get(Vcode=userOTP)
                usedOTP.delete()
                user = UserRegistration.objects.get(pNumber=dBNumber)
                user.status =1
                user.login_status =1
                user.save()
                UserRegistration.objects.filter(pNumber=dBNumber).update(is_verified=True)
                if(MobileNewslatters.objects.filter(number=dBNumber).exists()):
                    UserRegistration.objects.filter(pNumber=dBNumber).update(is_active=True)
                    return Response({"pNumber": dBNumber, "status":status.HTTP_200_OK, "message": "LogIn Success",})
                else:
                    MobileNewslatters.objects.create(number=dBNumber)
                    UserRegistration.objects.filter(pNumber=dBNumber).update(is_verified=True, is_active=True)
                    return Response({"pNumber": dBNumber, "status":status.HTTP_200_OK, "message": "USER VERIFIED", })
            else:
                return Response({"status":status.HTTP_400_BAD_REQUEST, "message": "OTP is Not Valid!", })
            
        except mobileOTP.DoesNotExist:
                return Response({"status":status.HTTP_400_BAD_REQUEST, "message": "OTP Not Exist!",})
