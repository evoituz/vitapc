from django.contrib import admin

from apps.users.models import User, CartItem

admin.site.register(User)
admin.site.register(CartItem)
