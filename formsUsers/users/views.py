import os
import uuid

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import UserForm, EditUserForm
import users.methods as method


list_users_file = {}


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def get_data_file(request):
    # отримати дані з файлу
    is_open, data_file = method.json_handler(file_path='list_users.json')
    if not is_open:
        messages.error(request, message=data_file)
        # return redirect(to='users')
    else:
        global list_users_file
        list_users_file = data_file
        messages.info(request, message='Дані з файлу отримані')
        # return


def save_data_to_file(request):
    global list_users_file
    is_save, message = method.json_handler(file_path='list_users.json', data=list_users_file)
    if not is_save:
        messages.error(request, message=message)
    else:
        # messages.info(request, message=request.headers)
        messages.info(request, message='Дані збережені в файл')


def list_users(request):
    new_user_form = UserForm()
    edit_user_form = EditUserForm()

    global list_users_file

    if list_users_file == {}:
        get_data_file(request)

    if request.method == 'GET':
        context = {
            'form_new_user': new_user_form,
            'form_edit_user': edit_user_form,
            # 'message': len(list_users_file),
            'title': 'List users',
            'users': list_users_file
        }

        return render(request, 'users.html', context)


def add_user(request):

    if request.method == 'POST':

        form = UserForm(request.POST)
        if form.is_valid():
            global list_users_file

            user_id = str(uuid.uuid4())

            list_users_file[user_id] = {
                'firstname': form.data.get('firstname'),
                'lastname': form.data.get('lastname'),
                'age': form.data.get('age'),
                'email': form.data.get('email'),
            }

            save_data_to_file(request)
            messages.success(request, f'Added new user. Total users: {len(list_users_file)}.')
            return redirect('list_users')


def edit_user(request):
    form = EditUserForm(request.POST)
    if form.is_valid():
        user_id = form.data.get('id')
        user = {
            'firstname': form.data.get('firstname'),
            'lastname': form.data.get('lastname'),
            'age': form.data.get('age'),
            'email': form.data.get('email'),
            'language': form.data.get('language')
        }
        list_users_file[user_id] = user

        save_data_to_file(request)
        messages.success(request, f'Edited user with id {user_id}')
    else:
        messages.error(request, 'Дані не валідні')
    return redirect('list_users')


def delete_user(request, id_user):
    global list_users_file
    del_user = list_users_file[id_user]
    message = f'DELETED user ID: {id_user}'
    list_users_file.pop(id_user)

    save_data_to_file(request)
    messages.success(request, message)
    return redirect('list_users')