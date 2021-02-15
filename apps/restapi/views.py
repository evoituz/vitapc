from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.products import models as product_models
from apps.products import serializers as product_serializers
from apps.restapi import views_logics
from apps.users import models as user_models
from apps.users import serializers as user_serializers


class CategoryListView(generics.ListAPIView):
    """ Для получения списка всех категориев """
    serializer_class = product_serializers.CategoryListSerializer
    queryset = product_models.Category.objects.all()


class ProductListView(generics.ListAPIView):
    """ Для получения списка всех товаров """
    serializer_class = product_serializers.ProductListSerializer
    queryset = product_models.Product.objects.all()


class ProductDetailView(generics.RetrieveAPIView):
    """ Для получения полной информации по конкретному товару """
    serializer_class = product_serializers.ProductDetailSerializer
    queryset = product_models.Product.objects.all()
    lookup_field = 'id'


class SupplierListView(generics.ListAPIView):
    """ Для получения списка всех поставщиков """
    serializer_class = product_serializers.SupplierSerializer
    queryset = product_models.Supplier.objects.all()


class CustomerCartItemsView(generics.RetrieveAPIView):
    """ Для получения всех товаров в корзине пользователя """
    serializer_class = user_serializers.UserCartItemsSerializer
    queryset = user_models.User.objects.all()

    def get_object(self):
        return self.request.user


class CustomerCartItemAddView(generics.CreateAPIView):
    """ Добавление товара в корзину """
    serializer_class = user_serializers.CartItemSerializer
    queryset = user_models.CartItem.objects.all()


class UserRegistrationView(generics.CreateAPIView):
    """ Регистрация аккаунта """
    serializer_class = user_serializers.UserRegistrationSerializer
    queryset = user_models.User.objects.all()


class SendCodeView(generics.CreateAPIView):
    """ Верификация номер телефона """
    permission_classes = [permissions.AllowAny]
    serializer_class = user_serializers.PhoneCodeSerializer

    def post(self, request, *args, **kwargs):
        data, status = views_logics.account_verification(request.data)
        return Response(data, status=status)


class UserDeliveryAddressView(generics.RetrieveAPIView):
    """ Для получения всех адресов доставки """
    serializer_class = user_serializers.UserDeliveryAddressSerializer
    queryset = user_models.User.objects.all()

    def get_object(self):
        return self.request.user
