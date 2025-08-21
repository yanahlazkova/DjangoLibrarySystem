from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_users, name='users'),
    path('new-user/', views.add_user, name='add_user'),
    path('new-deleted-user/<int:id>', views.del_user, name='del_user'),
]