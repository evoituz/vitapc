from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    """ Список категорий """
    image = models.ImageField(
        'Изображение категория', upload_to='images/categories/', blank=True)
    name = models.CharField(
        'Имя категория', max_length=250)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'product_categories'

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']


class ProductTag(models.Model):
    """ Теги товара """
    name = models.CharField(
        'Имя тега', max_length=250, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        db_table = 'product_tags'


class Product(models.Model):
    """ Список товаров """
    name = models.CharField(
        'Имя товара', max_length=250)

    tags = models.ManyToManyField(
        ProductTag, verbose_name='Теги', related_name='tags', blank=True, null=True)
    extra = models.JSONField(
        'Доп. инф.', blank=True)

    created_dt = models.DateTimeField(auto_now=True)
    updated_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product_items'


class ProductVariationName(models.Model):
    """ Ключ вариации товара
    Цвет/Размер/Гб/Бренд """
    product = models.ForeignKey(
        Product, verbose_name='Товар', related_name='variations', on_delete=models.PROTECT)
    name = models.CharField(
        'Имя', max_length=250, unique=True)

    class Meta:
        verbose_name = 'Атрибут товара'
        verbose_name_plural = 'Атрибуты товаров'
        db_table = 'product_variations'


class ProductVariationValue(models.Model):
    """ Значение ключа вариации товара
    Красный/32/8/MSI """
    product = models.ForeignKey(
        Product, verbose_name='Товар', related_name='variation_items', on_delete=models.PROTECT)
    variation = models.ForeignKey(
        ProductVariationName, verbose_name='Имя вариации', related_name='items', on_delete=models.PROTECT)
    value = models.CharField(
        'Значение', max_length=250)

    class Meta:
        verbose_name = 'Значение атрибута'
        verbose_name_plural = 'Значения атрибутов'
        db_table = 'product_variation_items'


class ProductVariationPrice(models.Model):
    """Видеокарта Цвет: Красный - Размер: 32см. = 200.000 сум """
    product = models.ForeignKey(
        Product, verbose_name='Товар', related_name='prices', on_delete=models.PROTECT)
    variation = models.ManyToManyField(
        ProductVariationValue, validators='Вариации', related_name='prices', blank=True, null=True)
    quantity = models.IntegerField(
        'Количество', default=1)
    price = models.DecimalField(
        'Цена', decimal_places=0, max_digits=12, default=0)

    class Meta:
        verbose_name = 'Цена вариации товара'
        verbose_name_plural = 'Цены вариации товаров'
        db_table = 'product_variation_prices'


class ProductVariationImage(models.Model):
    """ Изображения вариации товара """
    product = models.ForeignKey(
        Product, verbose_name='Товар', related_name='images', on_delete=models.PROTECT)
    variation = models.ManyToManyField(
        ProductVariationPrice, verbose_name='Вариация', related_name='images', blank=True, null=True)
    image = models.ImageField(
        'Изображение', upload_to='images/products/%Y/%m/%d/')

    class Meta:
        db_table = 'product_images'


class ProductPriceHistory(models.Model):
    """
    :extra = {'name': 'nVidia Geforce 1660 super', 'Производитель': 'MSI', 'Объём': 6гб}
    """
    product = models.ForeignKey(
        Product, verbose_name='ID товара', related_name='histories', on_delete=models.SET_NULL)
    extra = models.JSONField(
        'Вариация', default={})
    price = models.DecimalField(
        'Цена', max_digits=12, decimal_places=0)
    created_dt = models.DateTimeField(
        'Дата изменения цены', auto_now=True)

    class Meta:
        verbose_name = 'История изменения цены товара'
        verbose_name_plural = 'Истории изменений цен товаров'
        db_table = 'product_price_histories'
