from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CustomUserCreationForm, UserForm
from .models import CustomUser
from video_app.models import Video, Speciality
from video_app.models import Speciality
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login, authenticate
import numpy as np
from video_app.utils import OCEAN2MBTI

class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    template_name = 'login/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect(reverse_lazy('root-page'))


class CustomLoginView(LoginView):
    template_name = 'login/login.html'
    model = CustomUser

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        self.next_page = reverse_lazy('root-page')
        return HttpResponseRedirect(self.next_page)
    

def account_view(request, pk):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = request.user
            print(form.cleaned_data)
            if form.cleaned_data['first_name']:
                user.first_name = form.cleaned_data['first_name']
            if form.cleaned_data['last_name']:
                user.last_name = form.cleaned_data['last_name']
            if form.cleaned_data['patronymic']:
                user.patronymic = form.cleaned_data['patronymic']
            if form.cleaned_data['speciality']:
                user.speciality = form.cleaned_data['speciality']
                print(user.speciality)
            if request.FILES.get('profile_picture'):
                user.profile_picture = request.FILES['profile_picture']
            if request.FILES.get('video'):
                user.video = Video.objects.create(file=request.FILES['video'], vector=np.random.random((5,)))
            user.save()
            return redirect(reverse_lazy('account-page', kwargs={'pk': pk}))
    else:
        if request.user.video is not None:
            form = UserForm({'first_name': request.user.first_name,
                            'last_name': request.user.last_name,
                            'patronymic': request.user.patronymic,
                            'profile_picture': request.user.profile_picture,
                            'video': request.user.video.file,
                            'speciality': request.user.speciality})
        else:
            form = UserForm()
    return render(request, 'video_app/index.html',
                  {'form': form,
                   'specialities': Speciality.objects.all(),
                   'mbti': OCEAN2MBTI(request.user.video.vector.tolist()) if request.user.video is not None
                                      else None,
                   'ocean': request.user.video.vector.tolist() if request.user.video is not None else None})


class CustomAccountView(UpdateView):
    template_name = 'video_app/index.html'
    form_class = UserForm
    model = CustomUser
    
    def form_valid(self, form):
        user = form.save()

        return redirect(reverse_lazy('account-page',
                               kwargs={'pk': user.pk}))
    

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('login-page'))
