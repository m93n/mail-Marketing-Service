from django.contrib import admin
from .models import CustomUser, Subscription, EmailVerification

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'role', 'is_active', 'is_staff')
    search_fields = ('email', 'full_name')
    ordering = ('email',)
