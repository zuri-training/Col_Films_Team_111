
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_('you must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email = email, **other_fields)
        user.set_password(password)
        user.save()
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must be assigned to is_staff=true.')
        return self.create_user(email, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    reg_number = models.CharField(max_length=10)
    email = models.EmailField(_('email address'), unique= True)
    college_name = models.CharField(max_length=100)
    username = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    otp = models.CharField(max_length=6, null=True, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Otp(models.Model):
    registration_number = models.CharField(max_length=100)
    otp_code = models.CharField(max_length=10)

    def __str__(self):
        return self.otp_code + ' For ' + self.registration_number