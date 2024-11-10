from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db.models import Q
from django.apps import apps


class CustomUser(AbstractBaseUser, PermissionsMixin):
    profile_picture = models.ImageField(blank=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    patronymic = models.CharField(max_length=40, null=True, blank=True)
    video = models.OneToOneField('video_app.Video', on_delete=models.RESTRICT, null=True, blank=True)
    speciality = models.ForeignKey('video_app.Speciality', on_delete=models.RESTRICT, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
