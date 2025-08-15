from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.list_users, name='list_users'),
    path('users/list', views.add_user, name='add_user'),
    path('users/<str:id>', views.edit_user, name='edit_user'),
]
