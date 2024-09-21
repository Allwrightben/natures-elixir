from django.urls import path
from . import views
from .views import product_vote
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.all_products, name='products'),
    path('products/vote/<int:product_id>/', product_vote, name='product-vote'),
    path('<product_id>', views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)