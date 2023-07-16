from django.urls import path
from .views import register, login, get_products, get_product, create_product, update_product, delete_product

urlpatterns = [
    path('api/register', register),
    path('api/login', login),
    path('api/products', get_products),
    path('api/products/<int:id>', get_product),
    path('api/products', create_product),
    path('api/products/<int:id>', update_product),
    path('api/products/<int:id>', delete_product),
]
