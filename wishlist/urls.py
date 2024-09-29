from django.urls import path
from . import views

app_name = "wishlist"

urlpatterns = [
    path(
        '<int:product_id>/add/',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),
    path(
        'move/<int:product_id>/',
        views.move_to_bag, name='move_to_bag'
    ),
    path(
        'remove/<int:product_id>/',
        views.remove_from_wishlist,
        name='remove_from_wishlist'),
    path('', views.view_wishlist, name='view_wishlist'),
]
