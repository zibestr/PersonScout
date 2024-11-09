from django.http.request import HttpRequest as HttpRequest
from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login, authenticate

class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    template_name = 'login/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect(reverse_lazy('account-page',
                               kwargs={'pk': user.pk}))


class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    next_page = reverse_lazy('main-page')


class CustomAccountView(UpdateView):
    template_name = 'login/account.html'
    form_class = CustomUserChangeForm
    model = CustomUser
    
    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()

        return redirect(reverse_lazy('account-page',
                               kwargs={'pk': user.pk}))
    

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('login-page'))
