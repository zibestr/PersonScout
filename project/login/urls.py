from login import views
from django.urls import path


urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login-page'),
    path('register', views.RegistrationView.as_view(), name='register-page'),
    path('account/<int:pk>', views.CustomAccountView.as_view(), name='account-page'),
    path('logout', views.logout_view, name='logout-page')
]