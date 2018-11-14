from django.urls import path
from .views import list_products
# , create_product, update_product, delete_product

urlpatterns = [
    path('', list_products, name='list_products')
]
