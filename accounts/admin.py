# coding: utf-8

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):

    list_display = [
        'username', 'name', 'email', 'is_active', 'is_staff', 'date_joined'
    ]
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email'),
        }),
        ('Informações Básicas',{
            'fields': ('name', 'last_login')
        }),
        ('Permissões', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups',
                'user_permissions'
            )
        }),
    )


admin.site.register(User, UserAdmin)
