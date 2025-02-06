from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
