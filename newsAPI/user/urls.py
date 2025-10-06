from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
#     path('login/', views.LoginView.as_view(), name='login'),
#     path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.list_users, name='users'),
    path('<int:id>/', views.user_by_id, name='user_by_id'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
]