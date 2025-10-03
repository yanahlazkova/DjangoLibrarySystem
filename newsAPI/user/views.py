from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# class LoginView:
#     pass
#
#
# class LogoutView:
#     pass
def login(response):
    return HttpResponse('login')


def logout(response):
    return HttpResponse('logout')


