from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Just admin users has permission.
    """
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsOwnerOrReadOnly(BasePermission):
    """
    Access to data just for owner or read only ways. (GET, HEAD, OPTIONS).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True  # permission to read data for all users
        return obj.owner == request.user  # Only owner can edit

