from django.urls import path
from . import views

urlpatterns = [
    path('day/', views.day_now, name='day-now'),
    path('time/', views.time_now, name='time-now'),
    path('programmer/', views.programmers_day, name='day-programmer'),
]