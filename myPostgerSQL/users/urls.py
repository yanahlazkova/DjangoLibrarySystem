from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_users, name='users'),
    path('new-user/', views.add_user, name='add_user'),
    path('delete_user/<int:id>/', views.del_user, name='del_user'),
    path("get_user/<int:id>/", views.get_user, name="get_user"),
    # path('edit_user/<int:id>/', views.edit_user, name='edit_user'),
]