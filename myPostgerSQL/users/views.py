import uuid

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserForm, EditUserForm
from .models import User, Account

new_user_form = UserForm()
edit_user_form = EditUserForm()

def get_list_users():
    try:
        users = Account.objects.all().values()

        list_users = []
        for user in users:
            user_data = User.objects.get(id=user['user_id'])
            data = {
                    'id': user['id'],
                    'email': user['email'],
                    'login': user['login'],
                    'password': user['password'],
                    'firstname': user_data.firstname,
                    'lastname': user_data.lastname,
                    'age': user_data.age,
                    'phone': user_data.phone,
                }
            list_users.append(data)

        return list_users
    except Exception as e:
        return {'message': f'DataBase is empty or {e}'}


def all_users(request):
    if request.method == 'GET':
        search_by = request.GET.get('search_by')
        query = request.GET.get('gsearch')

        # Отримати список користувачів з БД
        list_users = get_list_users()

        if search_by and query:
            # __iexact - регістро-незалежний
            # __icontains - може містити
            list_users = []
            match search_by:
                case 'firstname':
                    list_users = User.objects.filter(firstname__icontains=query)
                case 'lastname':
                    list_users = User.objects.filter(lastname__icontains=query)
                case 'age':
                    list_users = User.objects.filter(age__icontains=query)
                case 'email':
                    list_users = User.objects.filter(email__icontains=query)
                case 'phone':
                    list_users = User.objects.filter(phone__icontains=query)
                case 'id':
                    list_users = User.objects.filter(id__icontains=query)

        context = {
            'form_new_user': new_user_form,
            'form_edit_user': edit_user_form,
            'title': 'List users',
            'users': list_users,
            'search_by': search_by,
        }

        return render(request, 'users.html', context)
    # return HttpResponse('List users')
    return redirect('/')


def add_user(request):
    if request.method == 'POST':
        # print()
        # print(dir(request))
        # print()
        # print(request.user)

        form = UserForm(request.POST)
        if form.is_valid():
            user_account = Account(
                email=form.cleaned_data['email'],
                login=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
                )
            user = User()
            user.save()
            user_account.user = user
            user_account.save()
            messages.info(request, message=f'Додано нового користувача з id: {user_account.id}')
    return redirect('users')


def del_user(request, id):
    if request.method == 'DELETE':
        try:
            user = Account.objects.get(id=id)  # дістаємо конкретного користувача
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
        user = Account.objects.get(id=id)
        return True, user
    except ObjectDoesNotExist:
        return False, f'Користувач з id {id} не існує.'


def get_user(request, id_user):
    if request.method == 'GET':
        is_get, data = get_user_by_id(id_user)
        # print()
        # print('Data get:')
        # print(data.user)
        # print()
        user_data = {
            "id": data.id,
            "firstname": data.user.firstname if data.user else None,
            "lastname": data.user.lastname if data.user else None,
            "age": data.user.age if data.user else None,
            "email": data.email,
            "login": data.login,
            "password": data.password,
            "phone": data.user.phone if data.user else None,
        }
        if is_get:
            return JsonResponse({"success": True, "user": user_data})
        else:
            return JsonResponse({"success": False, "error": data}, status=404)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)


def edit_user(request, id_user):
    account_user = get_object_or_404(Account, id=id_user)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=account_user)  # 🔹 instance=user!
        if form.is_valid():
            # print()
            # print('DATA edit:')
            # print(form.cleaned_data)
            # print()
            form.save()
            messages.success(request, f'Дані користувача {form.cleaned_data['firstname']} оновлено')
            return redirect('users')
        else:
            messages.error(request, f'Форма невалідна: {form.errors}')
    else:
        form = EditUserForm(instance=account_user)  # при GET — підставляємо існуючі дані

    # якщо GET або POST з помилками, треба відобразити форму
    return render(request, "edit_user.html", {"form": form})


def search_firstname(request):
    if request.method == 'GET':
        search_by = request.GET.get('search_by')
        search_word = request.GET.get('gsearch')
        # __iexact - регістро-незалежний
        # __icontains - може містити
        if search_word == '':
            return redirect('users')
        list_users = []
        match search_by:
            case 'firstname':
                list_users = User.objects.filter(firstname__icontains=search_word)
            case 'lastname':
                list_users = User.objects.filter(lastname__icontains=search_word)
            case 'age':
                list_users = User.objects.filter(age__icontains=search_word)
            case 'email':
                list_users = User.objects.filter(email__icontains=search_word)
            case 'phone':
                list_users = User.objects.filter(phone__icontains=search_word)
            case 'id':
                list_users = User.objects.filter(id__icontains=search_word)
        context = {
            'form_new_user': new_user_form,
            'form_edit_user': edit_user_form,
            'title': 'List users',
            'search_by': search_by,
            'users': list_users
        }

        return render(request, 'users.html', context)

    return redirect('users')
    #     return HttpResponse(request.GET.get('search_by'))