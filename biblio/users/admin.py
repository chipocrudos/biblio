from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import UserProfile


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser',
    ]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Groups'), {'fields': ('groups', )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Imporant Dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 
                'fields': ('email', 'password1', 'password2')}),
    )


admin.site.register(UserProfile, UserAdmin)
