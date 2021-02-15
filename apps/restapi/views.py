from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, views, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.restapi import serializers as rest_serializers
from apps.products import models as product_models
from apps.users import models as user_models
from apps.users import serializers as user_serializers
from apps.users.models import User


class CategoryListView(generics.ListAPIView):
    """ Для получения списка всех категориев """
    serializer_class = rest_serializers.CategoryListSerializer
    queryset = product_models.Category.objects.all()


class ProductListView(generics.ListAPIView):
    """ Для получения списка всех товаров """
    serializer_class = rest_serializers.ProductListSerializer
    queryset = product_models.Product.objects.all()


class ProductDetailView(generics.RetrieveAPIView):
    """ Для получения полной информации по конкретному товару """
    serializer_class = rest_serializers.ProductDetailSerializer
    queryset = product_models.Product.objects.all()
    lookup_field = 'id'


class SupplierListView(generics.ListAPIView):
    """ Для получения списка всех поставщиков """
    serializer_class = rest_serializers.SupplierSerializer
    queryset = product_models.Supplier.objects.all()


class CustomerCartItemsView(generics.RetrieveAPIView):
    """ Для получения всех товаров в корзине пользователя """
    serializer_class = rest_serializers.UserCartItemsSerializer
    queryset = user_models.User.objects.all()
    # lookup_field = 'user_id'

    def get_object(self):
        return self.request.user


class CustomerCartItemAddView(generics.CreateAPIView):
    """ Добавление товара в корзину """
    serializer_class = rest_serializers.CartItemSerializer
    queryset = user_models.CartItem.objects.all()
    # http_method_names = ['POST']

    # def post(self, request, *args, **kwargs):
    #     print(request.user)
    #     return self.create(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     data['user'] = self.request.user.id
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = user_serializers.UserRegistrationSerializer
    queryset = user_models.User.objects.all()


class SendCodeView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = user_serializers.PhoneCodeSerializer

    # def post(self, request, format=None):
    #     serializer = user_serializers.PhoneCodeSerializer()
    #     return Response({})

    def get_queryset(self):
        return self.request

    def post(self, request, *args, **kwargs):
        # print(request.data)
        # user = self.create(request, *args, **kwargs)
        # print(user.data)
        phone = request.data['phone']
        code = request.data['code']
        user = User.objects.get(phone=phone)
        if user.code == code:
            user.phone_verified = True
            user.save(update_fields=['phone_verified'])
            token, _ = Token.objects.get_or_create(user_id=user.id)
            print(token)
            data = {'token': token.key}
            return Response(data, status=201)
        return {'ok': False}


@csrf_exempt
@api_view(['POST'])
def send_code_view(request):
    pass
