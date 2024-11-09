from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


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


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "patronymic")
