from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.list_users, name='list_users'),
    path('users/add', views.add_user, name='add_user'),
    path('users/edit_user', views.edit_user, name='edit_user'),
    path('users/delete_user/<str:id_user>', views.delete_user, name='delete_user'),
]
