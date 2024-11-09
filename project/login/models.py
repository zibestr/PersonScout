from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db.models import Q
from django.apps import apps


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    patronymic = models.CharField(max_length=40, null=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class HR(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, primary_key=True)


class Applicant(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, primary_key=True)
