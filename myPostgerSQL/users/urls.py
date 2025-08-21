from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_users, name='users'),
    path('new-user/', views.add_user, name='add_user'),
]