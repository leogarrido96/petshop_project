from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    # Adiciona os novos campos na tela de edição do Admin
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('cpf', 'phone', 'profile_picture')}),
    )
    # Adiciona os campos na tela de criação
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Adicionais', {'fields': ('cpf', 'phone', 'profile_picture')}),
    )
    list_display = ['username', 'email', 'cpf', 'is_staff']


admin.site.register(User, CustomUserAdmin)
