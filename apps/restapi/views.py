from rest_framework import generics

from apps.restapi import serializers as rest_serializers
from apps.products import models as product_models
from apps.users import models as user_models


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
    serializer_class = rest_serializers.CartItemSerializer
    queryset = user_models.CartItem.objects.all()
    # http_method_names = ['POST']

    def get_object(self):
        return self.request.user
