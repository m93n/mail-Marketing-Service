from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Subscription

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom Serializer for getting JWT Token.
    This serializer validates inputs (email, password) 
    and if it was successful it will return two Tokens (access و refresh).
    """

    def validate(self, attrs):
        data = super().validate(attrs)
        data['email'] = self.user.email
        data['full_name'] = getattr(self.user, 'full_name', '')
        return data

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ["id", "full_name", "email", "role", "is_active"]

class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Displaying user information in JSON

    class Meta:
        model = Subscription
        fields = "__all__"
