from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Customize the Django admin interface for the CustomUser model.
    """
    model = CustomUser
    # Add 'role' and 'full_name' to the list display
    list_display = ('username', 'email', 'full_name', 'role', 'is_staff')
    # Add 'role' to the fieldsets for editing users
    fieldsets = UserAdmin.fieldsets + (
        ('Role Management', {'fields': ('role', 'full_name')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Management', {'fields': ('role', 'full_name')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)