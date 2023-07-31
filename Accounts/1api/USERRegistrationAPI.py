from rest_framework.views import APIView
from rest_framework.response import Response
from Accounts.models import USERINFORMATIONS, UserIMG, UserRegistration, mobileOTP
from KYCmanager.models import KYC, GSTNumber, PanNumber, panCardIMG, GSTCardIMG, Bank_Account, CancelChequeIMG
from rest_framework import status
from Accounts.api.APIHELPERS import SENDOTPONMOBILE
from Accounts.api.serializers import USERRegistrationSerializer
import datetime
from rest_framework.authtoken.models import Token


class USERRegistration(APIView):
    def post(self, request, *args, **kwargs):
        mobileNumber = request.data.get('pNumber').replace('+', '')
        if mobileNumber:
            mobileN = str(mobileNumber)
            serializer = USERRegistrationSerializer(data=request.data)
            code = SENDOTPONMOBILE(request, mobileN)
            if UserRegistration.objects.filter(pNumber__iexact= mobileN).exists():
                if(mobileOTP.objects.filter(pNumber__iexact=mobileN).exists()):
                    OldOTP = mobileOTP.objects.get(pNumber__iexact=mobileN)
                    OldOTP.delete()
                    mobileOTP.objects.create(pNumber=mobileN, Vcode=code)
                    return Response({"status":status.HTTP_200_OK, "Vcode": code,  "message": "Sent Verification Code", })
                else:
                    mobileOTP.objects.create(pNumber=mobileN, Vcode=code)
                    return Response({"status":status.HTTP_200_OK, "Vcode": code, "message": "Sent Verification Code", })
            else:
                if serializer.is_valid():
                    serializer.save()
                    userID = UserRegistration.objects.get(pNumber__iexact= mobileN).pk
                    # ===========================================
                    UserIMG.objects.create(user_id=userID)
                    USERINFORMATIONS.objects.create(user_id=userID)
                    # =============KYC==============
                    KYC.objects.create(user_id=userID)
                    PanNumber.objects.create(user_id=userID)
                    panCardIMG.objects.create(user_id=userID)
                    GSTNumber.objects.create(user_id=userID)
                    GSTCardIMG.objects.create(user_id=userID)
                    Bank_Account.objects.create(user_id=userID)
                    CancelChequeIMG.objects.create(user_id=userID)
                    # =============KYC==============
                    mobileOTP.objects.create(pNumber=mobileN, Vcode=code)
                    # ===========================================
                    return Response({
                                "status":status.HTTP_200_OK,
                                "code": code,
                                "message": "REGISTERED SUCCESSFULLY", 
                            })
                else:
                    return Response({
                        "Error": serializer.errors,
                        "Status" : status.HTTP_400_BAD_REQUEST,
                        "message":"Data is not Valid!",
                    })  
        else:
            return Response({
                    "status":status.HTTP_400_BAD_REQUEST,
                    "message": "Mobile Number is Empty", 
                })
            