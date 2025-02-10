from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom User Manager for manage creating users.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and Save an user with email and password.
        """
        if not email:
            raise ValueError("email address is required!")
        email = self.normalize_email(email) # normalize email address (lowercase words and delete spaces)
        user = self.model(email=email, **extra_fields) # self.model is the model that BaseUserManager handels. in here it's CustomUser that connected to CustomUserManager ==> (CustomUserManager.model == CustomUser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and Save a super user.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom model of users that logins with email.
    """
    
    ROLE_CHOICES = (
        ("user", "user"),
        ("admin", "admin"),
        ('guest', 'Guest'),
    )

    email = models.EmailField(unique=True, verbose_name="Email")
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user", verbose_name="User's Roll")
    
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_staff = models.BooleanField(default=False, verbose_name="staff")

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["-id"]

    def __str__(self):
        return self.email


class Subscription(models.Model):
    """
    Model of Subscription of users
    """

    PLAN_CHOICES = (
        ("free", "free"),
        ("basic", "basic"),
        ("premium", "premium"),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="subscription", verbose_name="user")
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES, default="free", verbose_name="type of subscription")
    start_date = models.DateTimeField(auto_now_add=True, verbose_name="start date")
    end_date = models.DateTimeField(null=True, blank=True, verbose_name="end date")

    class Meta:
        verbose_name = "subscription"
        verbose_name_plural = "subscriptions"
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.user.email} - {self.plan}"


import uuid
from django.utils import timezone
from datetime import timedelta

class EmailVerification(models.Model):
    """
    Model to manage verification of user's email
    """

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="email_verification", verbose_name="user")
    code = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name="verification code")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created date")
    expires_at = models.DateTimeField(verbose_name="expires date")

    class Meta:
        verbose_name = "verification code of email"
        verbose_name_plural = "verification codes of email"

    def save(self, *args, **kwargs):
        """
        Set expire date when saving
        """
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(hours=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} - {self.code}"
