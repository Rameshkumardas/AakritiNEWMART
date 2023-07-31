from Accounts.api.serializers import BillingAddressSerializer, ShippingAddressSerializer
from Accounts.models import USERbillingADDRESS, USERshippingADDRESS, UserRegistration
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#Serializer to createBillingAddress using Django
#Serializer to createBillingAddress using Django
#Serializer to createBillingAddress using Django
#Serializer to createBillingAddress using Django
#Serializer to createBillingAddress using Django
class getBillingAddress(APIView):
    def get(self, request, user=None, pk=None, format=None):
        try:
            targetModel = USERbillingADDRESS.objects.get(user_id=user, pk=pk)
            serializer = BillingAddressSerializer(targetModel)
            return Response({
                            "Status" : status.HTTP_200_OK,
                            "message":"Data Sent Success",
                            'billingaddress':serializer.data
                        })  
        except USERbillingADDRESS.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"User DoesNotExist",
                        }) 

class createBillingAddress(APIView):
    def get(self, request, pNumber=None, format=None):
        try:
            user = UserRegistration.objects.get(pNumber=pNumber)
            targetModel = USERbillingADDRESS.objects.filter(user_id=user.pk)
            serializer = BillingAddressSerializer(targetModel, many=True)
            return Response({
                            "Status" : status.HTTP_200_OK,
                            "message":"Data Sent Success",
                            'billingaddress':serializer.data
                        })  
        except UserRegistration.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"User DoesNotExist",
                        }) 
            
                        
    def post(self, request, *args, **kwargs):
        pNumber = request.data.get('pNumber')
        pCode = request.data.get('pCode')        
        house_no = request.data.get('house_no')
        landmark = request.data.get('landmark')
        colony = request.data.get('colony')
        city = request.data.get('city')
        state = request.data.get('state')
        print(pNumber)
        print(pCode)
        print(house_no)
        print(landmark)
        print(colony)
        print(city)
        print(state)
        try:
            pNumber = request.data.get('pNumber')
            user = UserRegistration.objects.get(pNumber=pNumber)
            request.data._mutable = True
            request.data['user'] = user.pk
            request.data._mutable = False
            serializer = BillingAddressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                                "Status" : status.HTTP_200_OK,
                                "message":"Address Added",
                                'billingaddress':serializer.data
                                })
            else:
                return Response({
                                "Error": serializer.errors,
                                "Status" : status.HTTP_400_BAD_REQUEST,
                                "message":"Data is not Valid!",
                            })  

        except UserRegistration.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"User DoesNotExist",
                        }) 
            
    def patch(self, request, format=None):
        user = request.data.get('user')
        pk = request.data.get('pk')
        print(user)
        print(pk)

        try:
            targetModel = USERbillingADDRESS.objects.get(pk=pk, user_id=user)
            serializer = BillingAddressSerializer(targetModel, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                                "Status" : status.HTTP_200_OK,
                                "message":"Billing Address Updated",
                            })
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except USERbillingADDRESS.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"Billing Address DoesNotExist",
                        }) 
    
    def delete(self, request,user, pk, format=None):
        try:
            targetModel = USERbillingADDRESS.objects.filter(pk=pk, user_id=user)
            targetModel.delete()
            return Response({
                            "Status" : status.HTTP_204_NO_CONTENT,
                            "message":"Billing Address Deleted",
                        })

        except USERbillingADDRESS.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"Billing Address DoesNotExist",
                        }) 
#Serializer to createShippingAddress using Django
#Serializer to createShippingAddress using Django
#Serializer to createShippingAddress using Django
#Serializer to createShippingAddress using Django
class getShippingAddress(APIView):
    def get(self, request, user=None, pk=None, format=None):
        try:
            targetModel = USERshippingADDRESS.objects.get(user_id=user, pk=pk)
            serializer = ShippingAddressSerializer(targetModel)
            return Response({
                            "Status" : status.HTTP_200_OK,
                            "message":"Data Sent Success",
                            'billingaddress':serializer.data
                        })  
        except USERbillingADDRESS.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"User DoesNotExist",
                        }) 


class createShippingAddress(APIView):
    def get(self, request, pNumber=None, format=None):
        try:
            user = UserRegistration.objects.get(pNumber=pNumber)
            targetModel = USERshippingADDRESS.objects.filter(user_id=user.pk)
            serializer = ShippingAddressSerializer(targetModel, many=True)
            return Response({
                            "Status" : status.HTTP_200_OK,
                            "message":"Data Sent Success",
                            'billingaddress':serializer.data
                        })  
        except UserRegistration.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"User DoesNotExist",
                        }) 
    def post(self, request, *args, **kwargs):
        pNumber = request.data.get('pNumber')
        user = UserRegistration.objects.get(pNumber=pNumber)
        request.data._mutable = True
        request.data['user'] = user.pk
        request.data._mutable = False
        serializer = ShippingAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                        "status":status.HTTP_200_OK,
                        "message": "Billing Address Create Success", 
                        'billingaddress':serializer.data

                    })
        else:
            return Response({
                "Error": serializer.errors,
                "Status" : status.HTTP_400_BAD_REQUEST,
                "message":"Data is not Valid!",
            })  

    def patch(self, request, format=None):
        user = request.data.get('user')
        pk = request.data.get('pk')
        print(user)
        print(pk)
        try:
            targetModel = USERshippingADDRESS.objects.get(user_id=user, pk=pk)
            serializer = ShippingAddressSerializer(targetModel, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                                "Status" : status.HTTP_200_OK,
                                "message":"Address Updated",
                                'billingaddress':serializer.data
                            })
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except USERshippingADDRESS.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"Billing Address DoesNotExist",
                        }) 
    
    def delete(self, request, user, pk, format=None):
        try:
            targetModel = USERshippingADDRESS.objects.get(user_id=user, pk=pk)
            targetModel.delete()
            return Response({
                            "Status" : status.HTTP_204_NO_CONTENT,
                            "message":"Billing Address Deleted",
                        })

        except USERshippingADDRESS.DoesNotExist:
            return Response({
                            "Status" : status.HTTP_400_BAD_REQUEST,
                            "message":"Billing Address DoesNotExist",
                        }) 
            







            





            