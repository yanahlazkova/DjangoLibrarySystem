"""
URL configuration for newsAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import bad_request

from blog.views import page_not_found
# from django.views.defaults import page_not_found

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]

# Тема: Обробка виключень
# Якщо DEBUG = False
# https://docs.djangoproject.com/en/5.2/ref/urls/#django.conf.urls.handler404:~:text=.MEDIA_ROOT)-,handler400,-%C2%B6
# https://docs.djangoproject.com/en/5.2/topics/http/views/#django.http.Http404:~:text=handle%20those%20errors.-,The%20Http404%20exception,-%C2%B6
# https://youtu.be/af7KvkQORwo?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&t=806
handler404 = page_not_found # сторінка не знайдена
# handler500 = server_error # помилка серверу
# handler403 = permission_denied # доступ заборонено
# handler400 = bad_request # невірний запит