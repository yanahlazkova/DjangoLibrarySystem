import os
import uuid

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import UserForm
import users.methods as method


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def list_users(request):
    user_form = UserForm()

    context = {
        'form': user_form,
        'title': 'List users',
    }

    save_file, data_file = method.json_handler(file_path='list_users.json')

    if not save_file:
        context['error'] = data_file
        data_file = {}

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = {
                'firstname': form.data.get('firstname'),
                'lastname': form.data.get('lastname'),
                'age': form.data.get('age'),
                'email': form.data.get('email'),
            }
            user_id = str(uuid.uuid4())
            data_file[user_id] = user # method.get_fake_id()
            save_file, message = method.json_handler(file_path='list_users.json', data=data_file)

            if save_file:
                context['message'] = message
                context['users'] = data_file
                context['error'] = None
            else:
                context['message'] = data_file
                context['error'] = message
            return render(request, 'users.html', context)
    elif request.method == 'GET':
        context['message'] = None
        context['users'] = data_file
        context['error'] = None

        return render(request, 'users.html', context)


def add_user(request):

    if request.method == 'POST':
        user = {
            'firstname': request.POST.get('firstname'),
            'lastname': request.POST.get('lastname'),
            'age': request.POST.get('age'),
            'email': request.POST.get('email'),

        }
        # Поточна директорія, де знаходиться views.py
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        # Абсолютний шлях до .books.json
        json_path = os.path.join(BASE_DIR, 'list_users.json')

        method.json_handler(BASE_DIR, user)
        return render(request, 'users.html')


def edit_user(request, user_data):
    context = {
        'message': user_data
    }
    return render(request, 'users.html', context)