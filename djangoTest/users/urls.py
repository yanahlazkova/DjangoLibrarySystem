from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('reg/', views.register_user, name='register_user'),
    path('user/', views.new_user, name='new_user'),
    path('user/<int:id>/', views.new_user, name='new_user_id'),
    path('user/info/', views.user_info, name='user_info'),
    path('del/', views.dell_users, name='dell_users'),
    path('<int:id>/', views.user_info, name='user_info'),
    # path('reg/<str:user>/<str:login>', views.register_user, name='register_user'),
]