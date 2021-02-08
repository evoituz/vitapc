from django.contrib import admin

from apps.products import models as product_models


admin.site.register(product_models.Category)
admin.site.register(product_models.ProductTag)
admin.site.register(product_models.Product)
admin.site.register(product_models.ProductPrice)
admin.site.register(product_models.ProductImage)
