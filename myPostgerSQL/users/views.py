import uuid

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserForm, EditUserForm
from .models import User


def get_list_users():
    try:
        list_users = User.objects.all().values()
        return list_users
    except Exception as e:
        return {'message': f'DataBase is empty or {e}'}


def all_users(request):
    new_user_form = UserForm()
    edit_user_form = EditUserForm()

    if request.method == 'GET':
        # Отримати список користувачів з БД
        list_users_file = get_list_users()
        context = {
            'form_new_user': new_user_form,
            'form_edit_user': edit_user_form,
            'title': 'List users',
            'users': list_users_file
        }

        return render(request, 'users.html', context)
    # return HttpResponse('List users')


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User(
                firstname = form.cleaned_data['firstname'],
                lastname = form.cleaned_data['lastname'],
                age = form.cleaned_data['age'],
                email = form.cleaned_data['email'],
                login = form.cleaned_data['login'],
                password = form.cleaned_data['password'],
                phone = form.cleaned_data['phone'],
            )
            new_user.save()
            # messages.info(request, message=f'Додано нового користувача з id: {new_user['id']}')
    return redirect('users')


def del_user(request, id):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(id=id)  # дістаємо конкретного користувача
            email = user.email  # запам'ятали, бо після delete() його вже не буде
            user.delete()

            return JsonResponse({
                "success": True,
                "email": email,
                "message": f"Deleted user {email}"
            })
        except User.DoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"}, status=404)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)


def get_user(request, id_user):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=id_user)
            user_data = {
                "id": user.id,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "age": user.age,
                "email": user.email,
                "login": user.login,
                "password": user.password,
                "phone": user.phone,
            }
            return JsonResponse({"success": True, "user": user_data})
        except ObjectDoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"}, status=404)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)


def edit_user(request, id_user):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(id=id_user)
                user_data = {
                    "id": user.id,
                    "firstname": user.firstname,
                    "lastname": user.lastname,
                    "age": user.age,
                    "email": user.email,
                    "login": user.login,
                    "password": user.password,
                    "phone": user.phone,
                }