import email
from Accounts.models import USERINFORMATIONS, USERbillingADDRESS, USERshippingADDRESS, UserRegistration, UserIMG
from KYCmanager.models import KYC
from rest_framework import serializers



#Serializer to Get UserRegistration Details using Django
class USERRegistrationSerializer(serializers.ModelSerializer):

  class Meta:
    model = UserRegistration
    # fields = ['pNumber']
    fields = "__all__"

  def create(self, validated_data):
    return UserRegistration.objects.create(**validated_data)
  
# =========================ALL USER LIST ===========================
class USERPIMGSerializer(serializers.ModelSerializer):  
  class Meta:
    model = UserIMG
    fields = ['pimg']
    
    def update(self, instance, validated_data):
      instance.pimg = validated_data.get('pimg', instance.pimg)
      instance.save()
      return instance 



#Serializer to ShippingAddressSerializer using Django
#Serializer to ShippingAddressSerializer using Django
#Serializer to ShippingAddressSerializer using Django
#Serializer to ShippingAddressSerializer using Django
class ShippingAddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = USERshippingADDRESS
    fields = ('id','user','pCode','house_no','landmark','colony','city','state')

  def create(self, validated_data):
    return USERshippingADDRESS.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.pCode = validated_data.get('pCode', instance.pCode)
    instance.house_no = validated_data.get('house_no', instance.house_no)
    instance.landmark = validated_data.get('landmark', instance.landmark)
    instance.colony = validated_data.get('colony', instance.colony)
    instance.city = validated_data.get('city', instance.city)
    instance.state = validated_data.get('state', instance.state)
    instance.save()
    return instance

#Serializer to BillingAddressSerializer using Django
#Serializer to BillingAddressSerializer using Django
#Serializer to BillingAddressSerializer using Django
#Serializer to BillingAddressSerializer using Django
class BillingAddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = USERbillingADDRESS
    fields = ('id', 'user','pCode','house_no','landmark','colony','city','state')
    
  def create(self, validated_data):
    return USERbillingADDRESS.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.pCode = validated_data.get('pCode', instance.pCode)
    instance.house_no = validated_data.get('house_no', instance.house_no)
    instance.landmark = validated_data.get('landmark', instance.landmark)
    instance.colony = validated_data.get('colony', instance.colony)
    instance.city = validated_data.get('city', instance.city)
    instance.state = validated_data.get('state', instance.state)
    instance.save()
    return instance
  
  
class getUSERStatusSerializer(serializers.ModelSerializer):
  
  pimg = serializers.SerializerMethodField('get_pimg')
  firstName = serializers.SerializerMethodField('get_firstName')
  lastName = serializers.SerializerMethodField('get_lastName')
  firmName = serializers.SerializerMethodField('get_firmName')  
  email = serializers.SerializerMethodField('get_email')
  approval_status = serializers.SerializerMethodField('get_approval_status')
  
  def get_pimg(self, obj):
    try:
        return UserIMG.objects.get(user_id=obj.pk).pimg.url
    except UserIMG.DoesNotExist:
        return 'ramesh.jpg'
  
  def get_firstName(self, obj):
    return KYC.objects.get(user_id=obj.pk).firstName
  
  def get_lastName(self, obj):
    return KYC.objects.get(user_id=obj.pk).lastName

  def get_firmName(self, obj):
    return KYC.objects.get(user_id=obj.pk).firmName
  
  def get_email(self, obj):
    return KYC.objects.get(user_id=obj.pk).email
  
  def get_approval_status(self, obj):
    return KYC.objects.get(user_id=obj.pk).approval_status
  
  class Meta:
    model = UserRegistration
    fields = ['pNumber', 'pimg', 'firstName', 'lastName', 'firmName', 'email', 'approval_status']
