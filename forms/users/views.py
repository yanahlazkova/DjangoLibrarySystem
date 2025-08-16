import uuid

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .userForms import UserForm


users_dict = {}


def main(request):
    return render(request, 'main.html')


def users(request):
    user_form = UserForm()
    return render(request, 'users.html', context={
        'form': user_form,
        'title': 'List',
        'users': users_dict,
        'message': len(users_dict)
    })


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            users_dict = {
                str(uuid.uuid4()): {
                    'firstname': form.cleaned_data.get('firstname'),
                    'lastname': form.cleaned_data.get('lastname'),
                    'login': form.cleaned_data.get('login'),
                    'age': form.cleaned_data.get('age'),
                    'email': form.cleaned_data.get('email'),
                }

            }
            # return redirect('users')  # Перенаправляем пользователя на страницу со списком
            return render(request, 'users.html')
    else:
        # Если запрос не POST, то это ошибка
        return redirect('users')