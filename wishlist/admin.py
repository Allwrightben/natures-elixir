from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Wishlist instances.

    This class customizes the admin interface for the Wishlist model,
    allowing administrators to view, filter, and search through wishlists.

    Attributes:
        list_display: A tuple specifying fields to display in the list view.
        list_filter: A tuple specifying fields to filter the results by.
        search_fields: A tuple specifying fields to include in the search.
        raw_id_fields: A tuple for fields that should
        be displayed as a raw ID input.
        readonly_fields: A tuple specifying fields are read-only in the form.

    Methods:
        product_count: Returns the number of products in the wishlist.
        clear_products: Action to remove all products from selected wishlists.
    """
    list_display = (
        'user',
        'created_at',
        'product_count',
    )
    list_filter = (
        'user',
    )
    search_fields = (
        'user__username',
        'products__name',
        'created_at',
    )
    raw_id_fields = ('user',)
    readonly_fields = ('created_at',)

    def product_count(self, obj):
        return obj.products.count()

    product_count.short_description = 'Number of Products'

    def clear_products(modeladmin, request, queryset):
        for wishlist in queryset:
            wishlist.products.clear()

    actions = ['clear_products']
