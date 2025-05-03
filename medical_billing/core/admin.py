from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Medicine, Bill

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Role Info'), {'fields': ('role',)}),  # Add this line to show role
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'role')
    ordering = ('username',)


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'stock_quantity',
        'expiry_date',
        'price_piece',
        'price_strip',
        'price_pack',
        'price_box',
    )
    search_fields = ('name', 'category')
    list_filter = ('category', 'expiry_date')


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'medicine', 'quantity', 'packaging_type', 'total_price', 'created_at')
    search_fields = ('staff__username', 'medicine__name', 'packaging_type')
    list_filter = ('packaging_type', 'created_at')
    ordering = ('-created_at',)
