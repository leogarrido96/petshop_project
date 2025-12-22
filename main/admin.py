from django.contrib import admin
from .models import ContactMessage, NewsletterSubscriber, SiteConfiguration

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')

admin.site.register(NewsletterSubscriber)

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    # Trava a adição se já existir 1 registro
    def has_add_permission(self, request):
        if SiteConfiguration.objects.exists():
            return False
        return True

    # Trava a exclusão (para ninguém deletar o site por engano)
    def has_delete_permission(self, request, obj=None):
        return False