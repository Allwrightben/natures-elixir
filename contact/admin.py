from django.contrib import admin
from .models import Contact

"""
Admin configuration for the Contact model.

This module includes the ContactAdmin class, which customizes
the admin interface for managing contact inquiries.
"""


class ContactAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Contact model.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        list_filter (tuple): Fields to filter the list view by.
        search_fields (tuple): Fields to search in the admin interface.
    """
    list_display = ('name', 'email', 'category', 'message_short', 'id')
    list_filter = ('category',)
    search_fields = ('name', 'email', 'message')

    def message_short(self, obj):
        return (
            obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
        )

    message_short.short_description = 'Message'


admin.site.register(Contact, ContactAdmin)
