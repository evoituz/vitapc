from django.urls import path

from apps.restapi import views as rest_views


app_name = 'swagger'
urlpatterns = [
    path('category/list/', rest_views.CategoryListView.as_view()),
    path('product/list/', rest_views.ProductListView.as_view()),
    path('product/<int:id>/', rest_views.ProductDetailView.as_view()),
    path('supplier/list/', rest_views.SupplierListView.as_view()),

    # user
    path('user/registration/', rest_views.UserRegistrationView.as_view()),
    path('user/registration/send_code/', rest_views.SendCodeView.as_view()),
    path('user/cart/items/', rest_views.CustomerCartItemsView.as_view()),
    path('user/cart/add/', rest_views.CustomerCartItemAddView.as_view()),
    path('user/delivery_addresses/', rest_views.UserDeliveryAddressView.as_view()),
]
