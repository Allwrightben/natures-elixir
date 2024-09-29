from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'category', 'message_short', 'id')
    list_filter = ('category',)
    search_fields = ('name', 'email', 'message')

    def message_short(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message

    message_short.short_description = 'Message'

admin.site.register(Contact, ContactAdmin)
