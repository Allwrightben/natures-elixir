from django.contrib import admin
from .models import Product, Category, Vote
from django.db import models  # noqa


class ProductAdmin(admin.ModelAdmin):
    """
    Customizes the display of the Product model in the Django admin interface.

    - Displays specific fields in the product list view, including SKU, name,
    category, price, thumbs up and down counts, and image.
    - Orders the products by SKU.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'thumbs_up_count',
        'thumbs_down_count',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Customizes the display of the Category model in the Django admin interface.

    - Displays the friendly name and the name of each category.
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vote)
