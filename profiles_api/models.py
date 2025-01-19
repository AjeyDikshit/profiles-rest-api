from django.db import models

# Note: Need to import few more libraries manually
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

""" Learning point: The above 2 are the standard classes we need for overriding/customizing the default Django user model """


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email: str, name: str, password: str = None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have a email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, name: str, password: str):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """returns full name of the user"""
        return self.name

    def get_short_name(self):
        """returns short name of user"""
        return self.name

    def __str__(self):
        """Returns string representation of user"""
        return self.email
