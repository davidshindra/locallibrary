from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('username', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('email', 'username')
    ordering = ('username',)

    fieldsets = (
        (None, {
            "fields": ('username', 'email', 'first_name', 'middle_name', 'last_name'),
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Others', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )