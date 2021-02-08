from django.urls import path

from apps.restapi import views as rest_views


app_name = 'swagger'
urlpatterns = [
    path('category/list/', rest_views.CategoryListView.as_view()),
    path('product/list/', rest_views.ProductDetailView.as_view()),
]
