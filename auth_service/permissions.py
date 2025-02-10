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

class IsSubscriptionActive(BasePermission):
    """
    Only users with an active subscription can access.
    """
    def has_permission(self, request, view):
        # Assume that each user's subscription is stored in the Subscription model
        user_subscription = request.user.subscription
        return user_subscription.is_active  # Check if the subscription is active or not
    
class IsGuest(BasePermission):
    """
    Only guest users (not logged in) can access.
    """
    def has_permission(self, request, view):
        return request.user.role == 'guest'
    
class IsUser(BasePermission):
    """
    Only regular users (with the user role) can have access.
    """
    def has_permission(self, request, view):
        return request.user.role == 'user'