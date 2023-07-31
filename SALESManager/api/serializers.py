import array
import email
import json
import random
from traceback import print_tb
from Accounts.models import USERINFORMATIONS, USERbillingADDRESS, USERshippingADDRESS, UserRegistration, UserIMG
from CommonModules.models import BrandName, ShippingList
from KYCmanager.models import KYC
from Payments.models import ProductConfirmWITHcod, ProductOrderList, ProductOrderPaymentStatus
from Products.models import GoodsandServicesTax, ProductBrandName, ProductEstimateShippingTime, ProductIMG, ProductList, ProductShippingManagement
from rest_framework import serializers
from Payments.api.genrateID import GENERATEEVENTID


class generateORDERIDSerializer(serializers.ModelSerializer):
  orderID = serializers.SerializerMethodField('get_orderID')
  firmName = serializers.SerializerMethodField('get_firmName')
  email = serializers.SerializerMethodField('get_email')
  pimg = serializers.SerializerMethodField('get_pimg')

  def get_orderID(self, obj):
    # maximum length of password needed
    # this can be changed to suit your password length
    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS 
    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_EVENTID = rand_digit + rand_upper 
    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(8):
        temp_EVENTID = temp_EVENTID + random.choice(COMBINED_LIST)
        # convert temporary password into array and shuffle to
        # prEVENT it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_EVENTID_list = array.array('u', temp_EVENTID)
        random.shuffle(temp_EVENTID_list)
    # traverse the temporary password array and append the chars
    # to form the password
    genrateEVENTID = ""
    for x in temp_EVENTID_list:
            genrateEVENTID = genrateEVENTID + x
            
    return genrateEVENTID
  

  def get_pimg(self, obj): 
    try:
        return UserIMG.objects.get(user_id=obj.pk).pimg.url
    except UserIMG.DoesNotExist:
        return 'ramesh-ramesh.jpg'
  
  def get_firmName(self, obj): 
    try:
        return KYC.objects.get(user_id=obj.pk).firmName
    except KYC.DoesNotExist:
        return 'Mr Unknown'
  
  def get_email(self, obj): 
    try:
        return KYC.objects.get(user_id=obj.pk).email
    except KYC.DoesNotExist:
        return 'example@gmail.com'

  class Meta:
    model = UserRegistration
    fields = ['orderID', 'firmName', 'email', 'pimg']


class getLOCALGSTSerializer(serializers.ModelSerializer):
  sgst = serializers.SerializerMethodField('get_sgst')
  def get_sgst(self, obj): 
    try:
        return GoodsandServicesTax.objects.get(pk=obj.pk).sgst
    except GoodsandServicesTax.DoesNotExist:
        return 18
  class Meta:
    model = GoodsandServicesTax
    fields = ['product', 'HSNCode', 'cgst', 'sgst']
    

class getGSTSerializer(serializers.ModelSerializer):
  def get_sgst(self, obj): 
    try:
        return GoodsandServicesTax.objects.get(pk=obj.pk).igst
    except GoodsandServicesTax.DoesNotExist:
        return 18
  class Meta:
    model = GoodsandServicesTax
    fields = ['product', 'HSNCode', 'igst']


class getProductShippingManagementSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductShippingManagement
    fields = ['product', 'local', 'regional', 'national','special','estimate_shipping_time',]
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
class getLocalGSTANDSHIPPINGSerializer(serializers.ModelSerializer):
  estimate_shipping_time = serializers.SerializerMethodField('get_estimate_shipping_time')
  def get_estimate_shipping_time(self, obj): 
    try:
        return ProductShippingManagement.objects.get(product=obj.product).estimate_shipping_time
    except ProductShippingManagement.DoesNotExist:
        return 18

  shipping_charge = serializers.SerializerMethodField('get_shipping_charge')
  def get_shipping_charge(self, obj): 
    try:
      shippingAttr = ProductShippingManagement.objects.get(product=obj.product)
      if (shippingAttr.status=='Dimensions'):
        QTY = self.context['QTY']
        productLengthCM = shippingAttr.length
        productWithCM = shippingAttr.width
        productHightCM = shippingAttr.hight
        Kg = ((productLengthCM*productWithCM*productHightCM)/4750)*int(QTY)
        shippingOBJ = ShippingList.objects.filter(is_active=True, type='Dimensions')
        for obj in shippingOBJ:
          dBVal0 = obj.kg_range.replace("(", '')
          dBVal1 = dBVal0.replace(")", "")
          dBVal2 = dBVal1.replace("'", "")
          dBVal3 = dBVal2.replace(" ", "")
          dBVal = dBVal3.split(',')
          if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
            shippingCharge = obj.local
            break
          else:
            shippingCharge = 200.0
        return shippingCharge
      
      elif (shippingAttr.status=='Weight'):
        QTY = self.context['QTY']
        productWeightGRM = shippingAttr.weight
        Kg = int(productWeightGRM*1000)*int(QTY)
        shippingOBJ = ShippingList.objects.filter(is_active=True, type='Weight')
        for obj in shippingOBJ:
          dBVal0 = obj.kg_range.replace("(", '')
          dBVal1 = dBVal0.replace(")", "")
          dBVal2 = dBVal1.replace("'", "")
          dBVal3 = dBVal2.replace(" ", "")
          dBVal = dBVal3.split(',')
          if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
            shippingCharge = obj.local
            break
          else:
            shippingCharge = 200.0

        return shippingCharge
      else:
        return 'Not Found'
    except ProductShippingManagement.DoesNotExist:
      return "Not Found"
     
  class Meta:
    model = GoodsandServicesTax
    fields = ['product', 'cgst', 'sgst','shipping_charge', 'estimate_shipping_time']

class getRegionGSTANDSHIPPINGSerializer(serializers.ModelSerializer):
  
  estimate_shipping_time = serializers.SerializerMethodField('get_estimate_shipping_time')
  def get_estimate_shipping_time(self, obj): 
    try:
        return ProductShippingManagement.objects.get(product=obj.product).estimate_shipping_time
    except ProductShippingManagement.DoesNotExist:
        return 18

  shipping_charge = serializers.SerializerMethodField('get_shipping_charge')
  def get_shipping_charge(self, obj): 
    try:
      shippingAttr = ProductShippingManagement.objects.get(product=obj.product)
      if (shippingAttr.status=='Dimensions'):
        QTY = self.context['QTY']
        productLengthCM = shippingAttr.length
        productWithCM = shippingAttr.width
        productHightCM = shippingAttr.hight
        Kg = ((productLengthCM*productWithCM*productHightCM)/4750)*int(QTY)
        print(Kg)
        shippingOBJ = ShippingList.objects.filter(is_active=True, type='Dimensions')
        for obj in shippingOBJ:
          dBVal0 = obj.kg_range.replace("(", '')
          dBVal1 = dBVal0.replace(")", "")
          dBVal2 = dBVal1.replace("'", "")
          dBVal3 = dBVal2.replace(" ", "")
          dBVal = dBVal3.split(',')
          if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
            shippingCharge = obj.regional
            break
          else:
            shippingCharge = 250.0
        return shippingCharge

      elif (shippingAttr.status=='Weight'):
        QTY = self.context['QTY']
        productWeightGRM = shippingAttr.weight
        Kg = int(productWeightGRM*1000)*int(QTY)
        shippingOBJ = ShippingList.objects.filter(is_active=True, type='Weight')
        for obj in shippingOBJ:
          dBVal0 = obj.kg_range.replace("(", '')
          dBVal1 = dBVal0.replace(")", "")
          dBVal2 = dBVal1.replace("'", "")
          dBVal3 = dBVal2.replace(" ", "")
          dBVal = dBVal3.split(',')
          if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
            shippingCharge = obj.regional
            break
          else:
            shippingCharge = 250.0
        return shippingCharge
      else:
        return 'Not Found'
    except ProductShippingManagement.DoesNotExist:
      return "Not Found"
        
  class Meta:
    model = GoodsandServicesTax
    fields = ['product','igst', 'shipping_charge', 'estimate_shipping_time']

class getNationalGSTANDSHIPPINGSerializer(serializers.ModelSerializer):
  estimate_shipping_time = serializers.SerializerMethodField('get_estimate_shipping_time')
  def get_estimate_shipping_time(self, obj): 
    try:
        return ProductShippingManagement.objects.get(product=obj.product).estimate_shipping_time
    except ProductShippingManagement.DoesNotExist:
        return 18

  shipping_charge = serializers.SerializerMethodField('get_shipping_charge')
  def get_shipping_charge(self, obj): 
    try:
      shippingAttr = ProductShippingManagement.objects.get(product=obj.product)
      if (shippingAttr.status=='Dimensions'):
        QTY = self.context['QTY']
        productLengthCM = shippingAttr.length
        productWithCM = shippingAttr.width
        productHightCM = shippingAttr.hight
        Kg = ((productLengthCM*productWithCM*productHightCM)/4750)*int(QTY)
        print(Kg)
        shippingOBJ = ShippingList.objects.filter(is_active=True, type='Dimensions')
        for obj in shippingOBJ:
          dBVal0 = obj.kg_range.replace("(", '')
          dBVal1 = dBVal0.replace(")", "")
          dBVal2 = dBVal1.replace("'", "")
          dBVal3 = dBVal2.replace(" ", "")
          dBVal = dBVal3.split(',')
          if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
            shippingCharge = obj.national
            break
          else:
            shippingCharge = 500.0
        return shippingCharge
      elif (shippingAttr.status=='Weight'):
        QTY = self.context['QTY']
        productWeightGRM = shippingAttr.weight
        Kg = int(productWeightGRM*1000)*int(QTY)
        shippingOBJ = ShippingList.objects.filter(is_active=True, type='Weight')
        for obj in shippingOBJ:
          dBVal0 = obj.kg_range.replace("(", '')
          dBVal1 = dBVal0.replace(")", "")
          dBVal2 = dBVal1.replace("'", "")
          dBVal3 = dBVal2.replace(" ", "")
          dBVal = dBVal3.split(',')
          if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
            shippingCharge = obj.national
            break
          else:
            shippingCharge = 500.0
        return shippingCharge
      else:
        return 'Not Found'
    except ProductShippingManagement.DoesNotExist:
      return "Not Found"
  
  class Meta:
    model = GoodsandServicesTax
    fields = ['product', 'igst','shipping_charge', 'estimate_shipping_time']


class getSpecialGSTANDSHIPPINGSerializer(serializers.ModelSerializer):
  estimate_shipping_time = serializers.SerializerMethodField('get_estimate_shipping_time')
  def get_estimate_shipping_time(self, obj): 
    try:
        return ProductShippingManagement.objects.get(product=obj.product).estimate_shipping_time
    except ProductShippingManagement.DoesNotExist:
        return 18

  shipping_charge = serializers.SerializerMethodField('get_shipping_charge')
  def get_shipping_charge(self, obj): 
    try:
      shippingAttr = ProductShippingManagement.objects.get(product=obj.product)
      if (shippingAttr.status=='Dimensions'):
        QTY = self.context['QTY']
        productLengthCM = shippingAttr.length
        productWithCM = shippingAttr.width
        productHightCM = shippingAttr.hight
        Kg = ((productLengthCM*productWithCM*productHightCM)/4750)*int(QTY)
        shippingOBJ = ShippingList.objects.filter(is_active=True, type='Dimensions')
        for obj in shippingOBJ:
          dBVal0 = obj.kg_range.replace("(", '')
          dBVal1 = dBVal0.replace(")", "")
          dBVal2 = dBVal1.replace("'", "")
          dBVal3 = dBVal2.replace(" ", "")
          dBVal = dBVal3.split(',')
          if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
            shippingCharge = obj.special
            break
          else:
            shippingCharge = 200.0
        return shippingCharge
      elif (shippingAttr.status=='Weight'):
        QTY = self.context['QTY']
        productWeightGRM = shippingAttr.weight
        Kg = int(productWeightGRM*1000)*int(QTY)
        ShippingList.objects.filter(status=shippingAttr.status)
        shippingOBJ = ShippingList.objects.filter(is_active=True, type='Weight')
        for obj in shippingOBJ:
          dBVal0 = obj.kg_range.replace("(", '')
          dBVal1 = dBVal0.replace(")", "")
          dBVal2 = dBVal1.replace("'", "")
          dBVal3 = dBVal2.replace(" ", "")
          dBVal = dBVal3.split(',')
          if(float(dBVal[0])<=Kg and float(dBVal[1])>=Kg):
            shippingCharge = obj.special
            break
          else:
            shippingCharge = 200.0
        return shippingCharge
      else:
        return 'Not Found'
    except ProductShippingManagement.DoesNotExist:
      return "Not Found"

  class Meta:
    model = GoodsandServicesTax
    fields = ['product', 'igst', 'shipping_charge', 'estimate_shipping_time']
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================
class createORDERwithCODSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductConfirmWITHcod
    fields = ['user','orderID','is_otp']
    
  def create(self, validated_data):
    return ProductConfirmWITHcod.objects.create(**validated_data)
  
  

class createCONFIRMORDERSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductOrderList
    fields = ['user', 'product', 'orderId', 'shipping', 'amount', 'qty', 'color']


class OrderPaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductOrderPaymentStatus
    fields = ['user','order','payMethod', 'is_payment']

class ORDERLISTSerializer(serializers.ModelSerializer):
  img = serializers.SerializerMethodField('get_img')
  name = serializers.SerializerMethodField('get_name')
  date = serializers.SerializerMethodField('get_is_estimate_shipping_time')
  def get_name(self, obj):
    try:
      product = ProductList.objects.get(pk=obj.product_id)
      return product.name
    except ProductList.DoesNotExist:
      return "DoesNotExist"

  def get_img(self, obj):
    try:
      product = ProductIMG.objects.get(product_id=obj.product)
      return product.img.url
    except ProductIMG.DoesNotExist:
      return "DoesNotExist"
  
  def get_is_estimate_shipping_time(self, obj):
    try:
      product = ProductEstimateShippingTime.objects.get(product_id=obj.product)
      return product.is_estimate_shipping_time
    except ProductEstimateShippingTime.DoesNotExist:
      return "DoesNotExist"
  
  class Meta:
    model = ProductOrderList
    fields = ('id', 'name','img', 'orderId', 'date')
    

class OrderPaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductOrderPaymentStatus
    fields = ['user','order','payMethod', 'is_payment']



class getORDERDESCRIPTIONSerializer(serializers.ModelSerializer):
  img = serializers.SerializerMethodField('get_img')
  name = serializers.SerializerMethodField('get_name')

  payMethod = serializers.SerializerMethodField('get_is_payMethod')
  is_payment = serializers.SerializerMethodField('get_is_payment')
  brandName = serializers.SerializerMethodField('get_brandName')

  date = serializers.SerializerMethodField('get_is_estimate_shipping_time')
  def get_name(self, obj):
    try:
      product = ProductList.objects.get(pk=obj.product_id)
      return product.name
    except ProductList.DoesNotExist:
      return "DoesNotExist"

  def get_img(self, obj):
    try:
      product = ProductIMG.objects.get(product_id=obj.product)
      return product.img.url
    except ProductIMG.DoesNotExist:
      return "DoesNotExist"
  
  def get_is_estimate_shipping_time(self, obj):
    try:
      product = ProductEstimateShippingTime.objects.get(product_id=obj.product)
      return product.is_estimate_shipping_time
    except ProductEstimateShippingTime.DoesNotExist:
      return "DoesNotExist"
  
  def get_brandName(self, obj):
    try:
      product = ProductBrandName.objects.get(product_id=obj.product)
      try:
        brand = BrandName.objects.get(pk=product.brandName)
        return brand.name
      except BrandName.DoesNotExist:
        return "RKMFabrics"
    except ProductBrandName.DoesNotExist:
      return "DoesNotExist"
    
  def get_is_payMethod(self, obj):
    try:
      product = ProductOrderPaymentStatus.objects.get(order_id=obj.pk)
      return product.payMethod
    except ProductOrderPaymentStatus.DoesNotExist:
      return "DoesNotExist"
  
  def get_is_payment(self, obj):
    try:
      product = ProductOrderPaymentStatus.objects.get(order_id=obj.pk)
      return product.is_payment
    except ProductOrderPaymentStatus.DoesNotExist:
      return "DoesNotExist"
    
  class Meta:
    model = ProductOrderList
    fields = ('id', 'name','img','brandName','orderId','product', 'amount', 'qty', 'color','is_confirmed', 'is_cancel','is_shipped', 'is_way', 'is_delivered', 'payMethod', 'is_payment', 'date')

    
class orderCANCELSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductOrderList
    fields = "__all__"

