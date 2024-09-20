from django.urls import path
from . import views
from .views import all_products, product_vote

urlpatterns = [
    path('', views.all_products, name='products'),
    path('products/vote/<int:product_id>/', product_vote, name='product-vote'),
    path('<product_id>', views.product_detail, name='product_detail'),
]