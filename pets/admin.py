from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'species', 'breed', 'birth_date', 'observations', 'created_at', 'updated_at')
    list_filter = ('species', 'owner__username')
    search_fields = ('name', 'breed', 'owner__username')
