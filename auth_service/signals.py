from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import RefreshToken

@receiver(social_account_added)
def create_jwt_for_social_user(request, sociallogin, **kwargs):
    """
    Signal to generate JWT tokens for a user who has logged in via Social Login.
    This function is triggered when a social account is added to the user (social_account_added).
    
    It generates an access and refresh token for the user using RefreshToken.
    """
    user = sociallogin.user
    # تولید توکن برای کاربر
    refresh = RefreshToken.for_user(user)
    # به عنوان مثال، چاپ توکن‌ها در لاگ (در پروژه واقعی می‌توان این توکن‌ها را به کاربر برگرداند)
    print(f"JWT generated for social user {user.email}:")
    print(f"Access Token: {str(refresh.access_token)}")
    print(f"Refresh Token: {str(refresh)}")
