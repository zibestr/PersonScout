from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser
from video_app.models import Speciality


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email", "is_superuser")
        labels = {
            "email": "Электронная почта",
            "is_superuser": "Аккаунт для HR?",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",
            "password": "Пароль"
        }
        help_texts = {
            "is_superuser": "ЗАГЛУШКА",
        }


class UserForm(forms.Form):
    profile_picture = forms.ImageField(required=False)
    first_name = forms.CharField(max_length=40, required=False)
    last_name = forms.CharField(max_length=40, required=False)
    patronymic = forms.CharField(max_length=40, required=False)
    video = forms.FileField(required=False)
    speciality = forms.ModelChoiceField(queryset=Speciality.objects.all(), required=False,
                                        to_field_name='name')


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ("first_name", "last_name", "patronymic", "profile_picture", "video__file", "preferred_speciality")
#         exclude = ("password",)
#         usable_password = None
