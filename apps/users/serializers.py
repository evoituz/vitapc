import pdb

from rest_framework import serializers

from apps.users import models as user_models


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.CartItem
        exclude = ['user']

    def create(self, validated_data):
        # ==== Если потребуется обновление уже имеющегося товара в корзине ====
        # instance, created = user_models.CartItem.objects.update_or_create(
        #     user=self.context.get('request').user,
        #     product=validated_data.get('product'),
        #     product_price=validated_data.get('product_price'),
        #     defaults={
        #         'quantity': validated_data.get('quantity'),
        #         'extra': validated_data.get('extra')
        #     }
        # )
        # =======================================================================
        instance = user_models.CartItem.objects.create(
            user=self.context.get('request').user,
            product=validated_data.get('product'),
            product_price=validated_data.get('product_price'),
            quantity=validated_data.get('quantity'),
            extra=validated_data.get('extra')
        )
        return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ['username', 'email', 'password',
                  'avatar', 'name', 'birthday',
                  'gender', 'city',
                  'phone']

    def create(self, validated_data):
        # TODO: подключить смс-сервис
        validated_data['code'] = '12345'
        return user_models.User.objects.create(**validated_data)


class PhoneCodeSerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.CharField()

    def create(self, validated_data):
        """ Для подтверждения смс-кода """
        phone = validated_data['phone']
        code = validated_data['code']
        user = user_models.User.objects.get(phone=phone)
        if user.code == code:
            user.phone_verified = True
            user.save(update_fields=['phone_verified'])
            return user
        return {'ok': False}


class UserCartItemSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()
    stock = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = user_models.CartItem
        fields = ['product', 'name', 'value', 'stock', 'price', 'quantity', 'extra']

    @staticmethod
    def get_product(obj):
        return {
            'name': obj.product.name,
            'value': obj.product_price.value,
            'stock': obj.product_price.quantity,
            'price': obj.product_price.price,
        }

    @staticmethod
    def get_name(obj):
        return obj.product.name

    @staticmethod
    def get_value(obj):
        return obj.product_price.value

    @staticmethod
    def get_stock(obj):
        return obj.product_price.quantity

    @staticmethod
    def get_price(obj):
        return obj.product_price.price


class UserCartItemsSerializer(serializers.ModelSerializer):
    cart_items = UserCartItemSerializer(many=True)

    class Meta:
        model = user_models.User
        fields = ['cart_items']


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.DeliveryAddress
        # fields = '__all__'
        exclude = ['user']


class UserDeliveryAddressSerializer(serializers.ModelSerializer):
    delivery_addresses = DeliveryAddressSerializer(many=True)

    class Meta:
        model = user_models.User
        fields = ['delivery_addresses']
