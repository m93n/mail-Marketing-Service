from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    ویو ورود سفارشی برای کاربران معمولی با استفاده از JWT.
    این ویو ایمیل و رمز عبور کاربر را دریافت می‌کند و در صورت موفقیت
    توکن‌های access و refresh را برمی‌گرداند.
    """
    serializer_class = CustomTokenObtainPairSerializer