import json
import time
import base64

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from .models import Video, PersonalityGroup, Personality, Speciality
from login.models import CustomUser
from django.contrib.auth.decorators import user_passes_test, login_required
from . import tasks
from .forms import FileFieldForm
import numpy as np
from .utils import OCEAN2MBTI
from pgvector.django import CosineDistance


def root_page(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('login-page'))
    if request.user.is_superuser:
        return redirect(reverse_lazy('hr-page'))
    return redirect(reverse_lazy('account-page', kwargs={'pk': request.user.id}))


@user_passes_test(lambda u: u.is_superuser)
def hr_main_view(request):
    if request.method == 'POST':
        form = FileFieldForm(request.POST, request.FILES)
        if form.is_valid():
            for f in form.cleaned_data['video']:
                Video.objects.create(file=f, vector=np.random.random((5,)))
            speciality = form.cleaned_data['speciality']
            cand_number = form.cleaned_data['candidate_number']

            return render(request, 'video_app/hr_main.html', 
                          {'show': True,
                           'user_info': [{'user': user,
                                          'mbti': OCEAN2MBTI(user.video.vector)[1] if user.video is not None else None}
                                           for user in CustomUser.objects.filter(is_superuser=False).annotate(distance=CosineDistance('video__vector', speciality.vector) * 100)
                                                        .order_by(CosineDistance('video__vector', speciality.vector))[:cand_number]],
                                           'max_number': len(CustomUser.objects.filter(is_superuser=False)
                                                         .all())})
    else:
        form = FileFieldForm()
    return render(request, 'video_app/hr_main.html',
                  {'form': form,
                   'specialities': Speciality.objects.all(),
                   'show': False})


def hr_show_candidates(request, pk):
    cand = CustomUser.objects.get(id=pk)
    return render(request, 'video_app/candidat.html',
                  {'cand': cand,
                   'mbti': OCEAN2MBTI(cand.video.vector.tolist())[1] if cand.video is not None
                                      else None,
                   'ocean': list(map(lambda x: int(x * 10 + 0.5), cand.video.vector.tolist())) if cand.video is not None else None})
