# permissions.py (or inside access_accounts.py if not separated)

from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    """
    Allows users only to users with role='admin' or is_superuser.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
                request.user.role == 'admin' or request.user.is_superuser
        )


class IsInventoryManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'inventory'


class IsBillingStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'staff'
