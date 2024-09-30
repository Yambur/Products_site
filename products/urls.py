from products.apps import ProductsConfig
from django.urls import path
from .views import ProductListCreateView, index

app_name = ProductsConfig

urlpatterns = [
    path('products/', ProductListCreateView.as_view()),
    path('', index, name='index'),
]

