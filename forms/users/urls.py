from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('users/', views.add_user, name='add_user'),
]