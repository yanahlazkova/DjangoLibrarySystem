from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user.forms import LoginUserForm, RegisterUserForm


# class LoginView:
#     pass
#
#
# class LogoutView:
#     pass
def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            user = authenticate(username=data_form['username'], password=data_form['password'])
            if user and user.is_active:
                login(request, user)
                return redirect('home')

        error = 'Невірний логін або пароль'
        return render(request, "user/login.html", {"form": form, 'error': error})

    else:
        form = LoginUserForm()
        return render(request, "user/login.html", {"form": form})




def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            # if user and user.is_active:
            #     login(request, user)
            return render(request, 'user/login.html', {"form": form, 'user_data': user})

        return render(request, "user/register.html", {"error": form.errors, "form": form})

    else:
        from faker import Faker
        fake = Faker()

        form = RegisterUserForm()
        new_user = {
            'username': fake.user_name(),
            'email': fake.email(),
            'password': '1111',
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        }

        return render(request, 'user/register.html', context={'form': form, 'new_user': new_user})


def user_by_id(request):
    return None


def list_users(request):
    return None