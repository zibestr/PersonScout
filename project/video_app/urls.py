from video_app import views
from django.urls import path


urlpatterns = [
    path('', views.root_page),
    path('main/', views.main_page, name='main-page'),
    path('hr_main/', views.hr_main_view, name='hr-page'),
    path('vacancies/', views.vacancies_page, name='vacancies-page'),
    path('vacancy-info/<int:pk>', views.vacancy_info_view, name='vacancy-info')
]
