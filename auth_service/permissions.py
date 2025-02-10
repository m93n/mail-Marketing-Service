from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Just admin users has permission.
    """
    def has_permission(self, request, view):
        return request.user.role == 'admin'
