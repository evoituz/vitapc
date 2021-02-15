from rest_framework import serializers

from apps.products import models as product_models


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_models.Category
        fields = '__all__'


class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_models.ProductPrice
        # fields = '__all__'
        exclude = ['product']


class ProductImageSerializer(serializers.ModelSerializer):
    # images = serializers.JSONField(source='get_image_sizes')

    class Meta:
        model = product_models.ProductImage
        fields = ['image']
        # exclude = ['product']


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_models.ProductTag
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_models.Supplier
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    prices = ProductPriceSerializer(many=True)
    poster = serializers.SerializerMethodField()

    class Meta:
        model = product_models.Product
        fields = ['id', 'name', 'description', 'prices', 'poster']

    @staticmethod
    def get_poster(obj):
        # TODO: нужна логика для определения постера из изображений
        data = dict()
        for img in obj.images.all():
            data['small'] = img.image.url
            data['big'] = img.image.url
        return data


class ProductDetailSerializer(serializers.ModelSerializer):
    prices = ProductPriceSerializer(many=True)
    images = serializers.SerializerMethodField()
    tags = ProductTagSerializer(many=True)

    class Meta:
        model = product_models.Product
        fields = ['id', 'name', 'extra', 'created_dt', 'updated_dt', 'prices', 'images', 'tags']

    @staticmethod
    def get_images(obj):
        # TODO: сделать несколько видов размера изображений
        result = []
        for img in obj.images.all():
            data = {
                'small': img.image.url,
                'big': img.image.url
            }
            result.append(data)
        return result