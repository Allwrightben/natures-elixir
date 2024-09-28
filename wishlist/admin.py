from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """Admin for the Wishlist model."""
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
