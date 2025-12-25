from django.contrib import admin

from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'city', 'state', 'zip_code', 'is_main', 'created_at', 'updated_at')
    list_filter = ('city', 'state', 'is_main', 'user__username')
    search_fields = ('user__username', 'street', 'city', 'zip_code')
