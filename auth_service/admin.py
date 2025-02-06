from django.contrib import admin
from .models import CustomUser, Subscription, EmailVerification

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'role', 'is_active', 'is_staff')
    search_fields = ('email', 'full_name')
    ordering = ('email',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date')
    search_fields = ('user__email',)
    ordering = ('-start_date',)


