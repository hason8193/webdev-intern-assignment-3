from django.urls import path
from . import views

app_name = 'scores'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('lookup/', views.score_lookup, name='lookup'),
    path('statistics/', views.score_statistics, name='statistics'),
    path('top-group-a/', views.top_group_a_students, name='top_group_a'),
    path('api/statistics/', views.statistics_api, name='statistics_api'),
    path('about/', views.AboutView.as_view(), name='about'),
]