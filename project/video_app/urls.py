from video_app import views
from django.urls import path


urlpatterns = [
    path('', views.root_page, name='root-page'),
    path('hr_main/', views.hr_main_view, name='hr-page'),
    path('cand-info/<int:pk>', views.hr_show_candidates, name='cand-info')
]
