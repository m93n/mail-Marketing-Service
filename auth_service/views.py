from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from .models import CustomUser, Subscription
from .serializers import CustomTokenObtainPairSerializer, UserSerializer, SubscriptionSerializer
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom login view for users by JWT.
    This view takes email and password and if it was successful will
    return access and refresh tokens.
    """
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
