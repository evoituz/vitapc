from rest_framework import generics
from rest_framework import permissions

from apps.restapi import serializers as rest_serializers
from apps.products import models as product_models


class CategoryListView(generics.ListAPIView):
    serializer_class = rest_serializers.CategoryListSerializer
    queryset = product_models.Category.objects.all()


class ProductDetailView(generics.ListAPIView):
    serializer_class = rest_serializers.ProductDetailSerializer
    queryset = product_models.Product.objects.all()
