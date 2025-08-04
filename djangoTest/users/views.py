from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from faker import Faker

from users.models import User

fake = Faker()


def register_user(request):
    data_user = {
        'page': 'Реєстрація користувача',
        'login': fake.user_name(),
        'email': fake.email(domain='ukr.net'),
        'password': fake.password(length=8)
    }

    template = loader.get_template('register.html')

    return HttpResponse(template.render(data_user, request))


def add_user_to_db(user):
    new_user = User(
        login=user['login'],
        password=user['password'],
        email=user['email']
    )

    new_user.save()

    return new_user


def new_user(request, id=None):
    if request.method == 'POST':
        # user_id = request.POST.get('id')
        login = request.POST.get('login')  # Используем .get() для безопасного доступа
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Перевірити чи існує даний email в DB
        email_db = User.objects.filter(email=email).values() if User.objects.all() else 0
        if email_db:
            return HttpResponse(f'Користувач з email {email_db} вже існує.')

        new_user = {
            'login': login,
            'email': email,
            'password': password,
        }
        # зберігаємо нового користувача у БД
        user_db = add_user_to_db(new_user)

        context = {
            'id': user_db.id,
            'login': login,
            'email': email,
            'password': password,
        }
        return render(request, 'new_user.html', context)

    else:
        user_db = User.objects.get(id=id)
        context = {
            'id': user_db.id,
            'login': user_db.login,
            'password': user_db.password,
            'firstname': user_db.firstname,
            'lastname': user_db.lastname,
            'phone': user_db.phone,
            'email': user_db.email
        }
        if context['firstname'] == '':
            context['firstname'] = fake.first_name()
        if context['lastname'] == '':
            context['lastname'] = fake.last_name()
        if context['phone'] == '':
            context['phone'] = fake.phone_number()

        return render(request, 'new_user.html', context)
    # return HttpResponse(f'Hello, {user_name}, {email}')


def change_data_user(user):
    # знаходимо по id користувача у БД
    create_user = User.objects.get(id=user['id'])
    create_user.lastname = user['lastname']
    create_user.firstname = user['firstname']
    create_user.phone = user['phone']
    create_user.password = user['password']
    create_user.save()
    return create_user


def user_info(request, id):
    if request.method == 'POST':
        user_info = {
            'id': request.POST.get('id'),
            'login': request.POST.get('login'),
            'email': request.POST.get('email'),
            'lastname': request.POST.get('lastname'),
            'firstname': request.POST.get('firstname'),
            'phone': request.POST.get('phone'),
            'password': request.POST.get('password')
        }

        user_db = change_data_user(user_info)

        context = {
            'id': user_db.id,
            'login': user_db.login,
            'password': user_db.password,
            'firstname': user_db.firstname,
            'lastname': user_db.lastname,
            'phone': user_db.phone,
            'email': user_db.email
        }

        return render(request, 'user_info.html', context)
    else:
        # Ваш код для обработки GET-запроса
        user_db = User.objects.get(id=id)
        context = {
            'id': user_db.id,
            'login': 'myuser',#user_db.login,
            'password': user_db.password,
            'firstname': user_db.firstname,
            'lastname': user_db.lastname,
            'phone': user_db.phone,
            'email': user_db.email
        }


        return render(request, 'user_info.html', context)


def list_users(request):
    if not request.GET:
        users_db = User.objects.all().values()

        context = {
            'users': users_db
        }
        return render(request, 'users.html', context)

        # return HttpResponse('База користувачів пуста')
        # return HttpResponse(f'Hello, {request.GET}')
    else:
        user_email = request.GET.get('email')
        new_user = User.objects.filter(email=user_email).values()

        return HttpResponse(f'New users: {new_user}')


def dell_users(request):
    users = User.objects.all()
    for user in users:
        user.delete()
    list_users(request)
    return HttpResponse('Дані видалені...')
