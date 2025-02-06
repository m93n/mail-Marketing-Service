from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom login view for users by JWT.
    This view takes email and password and if it was successful will
    return access and refresh tokens.
    """
    serializer_class = CustomTokenObtainPairSerializer