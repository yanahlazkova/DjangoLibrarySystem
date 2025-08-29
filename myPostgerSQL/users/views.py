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
                email=form.cleaned_data['email'],
                login=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
            )
            new_user.save()
            messages.info(request, message=f'Додано нового користувача з id: {new_user.id}')
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


def get_user_by_id(id):
    try:
        user = User.objects.get(id=id)
        return True, user
    except ObjectDoesNotExist:
        return False, f'Користувач з id {id} не існує.'


def get_user(request, id_user):
    if request.method == 'GET':
        is_get, data = get_user_by_id(id_user)
        user_data = {
            "id": data.id,
            "firstname": data.firstname,
            "lastname": data.lastname,
            "age": data.age,
            "email": data.email,
            "login": data.login,
            "password": data.password,
            "phone": data.phone,
        }
        if is_get:
            return JsonResponse({"success": True, "user": user_data})
        else:
            return JsonResponse({"success": False, "error": data}, status=404)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)


def edit_user(request, id_user):
    user = get_object_or_404(User, id=id_user)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)  # 🔹 instance=user!
        if form.is_valid():
            form.save()
            messages.success(request, f'Дані користувача {user.firstname} оновлено')
            return redirect('users')
        else:
            messages.error(request, f'Форма невалідна: {form.errors}')
    else:
        form = EditUserForm(instance=user)  # при GET — підставляємо існуючі дані

    # якщо GET або POST з помилками, треба відобразити форму
    return render(request, "edit_user.html", {"form": form})