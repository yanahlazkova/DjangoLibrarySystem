from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user.forms import LoginForm

# class LoginView:
#     pass
#
#
# class LogoutView:
#     pass
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            user = authenticate(username=data_form['login'], password=data_form['password'])
            if user and user.is_active:
                login(request, user)
                return redirect('home')

        error = 'Невірний логін або пароль'
        return render(request, "user/login.html", {"form": form, 'error': error})

    else:
        form = LoginForm()
        return render(request, "user/login.html", {"form": form})




def logout_user(request):
    logout(request)
    return redirect('home')


def sign_up(request):
    return HttpResponse('register')


def user_by_id(request):
    return None


def list_users(request):
    return None