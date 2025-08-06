import json
import os
from django.db import IntegrityError

from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from faker import Faker

from books.models import Reader, Book

fake = Faker(['uk_UA'])


"""Методи читання (відображення) даних
    new - дані готові до збереження але ще не додані у БД,
    edit - дані з БД для редагування,
    read - дані з БД тільки для читання (не можливо змінити)
"""


def reader_data(request, id=None):
    """ Вивід даних читача з БД """
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            reader_obj = Reader.objects.get(email=email)
            my_message = f'Читач з вказаним email {email} вже існує'
            return render(request, 'error_page.html', {'error_message': my_message})
        except Reader.DoesNotExist:
            # якщо дані ще не збережені, читача не знайдено в БД
            new_reader = Reader(
                firstname=request.POST.get('firstname'),
                lastname=request.POST.get('lastname'),
                email=request.POST.get('email'),
                # phone=request.POST.get('phone')
                )
            new_reader.save()

            reader = {
                'id': new_reader.id,
                'firstname': new_reader.firstname,
                'lastname': new_reader.lastname,
                'email': new_reader.email,
                # 'phone': new_reader.phone,
            }
            context = {
                'title': f'Читач id: {new_reader.id}',
                'method_read': 'edit',
                'reader': reader,
            }

            return render(request, 'new_reader.html', context=context)
        except Reader.MultipleObjectsReturned:
            my_message = f'Знайдено декілька читачів з ID 1. Це помилка в даних.'
            return render(request, 'error_page.html', {'error_message': my_message})

    elif request.method == 'GET':
        try:
            reader_db = Reader.objects.get(id=id)

            reader = {
                'id': reader_db.id,
                'firstname': reader_db.firstname,
                'lastname': reader_db.lastname,
                'email': reader_db.email,
                # 'phone': reader_db.phone,
            }
            context = {
                'title': f'Читач id: {id} Метод {request.method}',
                'method_read': 'read',
                'reader': reader,
            }

            return render(request, 'new_reader.html', context=context)

        except Reader.DoesNotExist:
            my_message = "Читача не знайдено."
            return render(request, 'error_page.html', {'error_message': my_message})
        except Reader.MultipleObjectsReturned:
            my_message = f'Знайдено декілька читачів з ID {id}. Це помилка в даних.'
            return render(request, 'error_page.html', {'error_message': my_message})

        # return HttpResponse(f'function reader_data, method GET (id={reader})')


def new_reader(request):
    """ Визивається коли вводяться перші дані реєстрації читача"""
    reader = {
        'firstname': fake.first_name(),
        'lastname': fake.last_name(),
        'email': fake.email(domain='ukr.net'),
        # 'phone': fake.phone_number(),
    }

    template = loader.get_template('new_reader.html')

    context = {
        'title': 'Реєстрація нового читача',
        'method_read': 'new',
        'reader': reader
    }

    return HttpResponse(template.render(context, request))


def reader_edit(request, id):
    try:
        reader_obj = Reader.objects.get(id=id)
        reader = {
            'id': id,
            'firstname': reader_obj.firstname,
            'lastname': reader_obj.lastname,
            'email': reader_obj.email,
            # 'phone': reader_db.phone,
        }
        if request.method == 'GET':

            if reader_obj.firstname == '':
                reader['firstname'] = fake.first_name()
            if reader_obj.lastname == '':
                reader['lastname'] = fake.last_name()
            # if reader_db['phone'] == '':
            #     reader['phone'] = fake.phone_number()
            if reader_obj.email == '':
                reader['email'] = fake.email()

            context = {
                'title': f'Редагування читача з id: {id}',
                'method_read': 'edit',
                'reader': reader
            }

            return render(request, 'new_reader.html', context)

        elif request.method == 'POST':
            email = request.POST.get('email')

            reader_obj.firstname = request.POST.get('firstname')
            reader_obj.lastname = request.POST.get('lastname')
            reader_obj.email = email
            try:
                reader_obj.save()
                context = {
                    'title': f'Збереження даних читача з id: {id}',
                    'method_read': 'read',
                    'reader': {
                        'id': id,
                        'firstname': reader_obj.firstname,
                        'lastname': reader_obj.lastname,
                        'email': reader_obj.email,
                        # 'phone': reader_db.phone,
                    }
                }
                return render(request, 'new_reader.html', context)
            except IntegrityError:
                my_message = f'Вже існує користувач з email {email}'
                return render(request, 'error_page.html', {'error_message': my_message})


    except Reader.DoesNotExist:
        my_message = "Читача не знайдено."
        return render(request, 'error_page.html', {'error_message': my_message})
    except Reader.MultipleObjectsReturned:
        my_message = f'Знайдено декілька читачів з ID {id}. Це помилка в даних.'
        return render(request, 'error_page.html', {'error_message': my_message})


def readers_all(request):
    template = loader.get_template('readers.html')

    readers_db = Reader.objects.all().values()

    context = {
        'readers': readers_db,
        'request': request
    }
    # change_email_reader()

    return HttpResponse(template.render(context, request))


def add_books_to_db(request):
    # Поточна директорія, де знаходиться views.py
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Абсолютний шлях до .books.json
    json_path = os.path.join(BASE_DIR, 'books3.json')

    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            books_json = json.load(file)

        # books = []

        for book_info in books_json.values():
            book = Book(
                book_id=book_info['idBook'],
                title=book_info['title'],
                author=book_info['author'],
                year=int(book_info['year']) if book_info['year'] else 0,
                ebook=book_info['eBookChecked'],
                filename=book_info['ebookFileName'] if book_info['eBookChecked'] else '-',
                genre=book_info['genre'])
            book.save()

    except FileNotFoundError:
        print(f"Ошибка: Файл '{json_path}' не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка: Не удалось декодировать JSON из файла '{json_path}'. Проверьте его формат.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


    template = loader.get_template('books.html')

    book_db = Book.objects.all().values()

    context = {
        'message': json_path,
        'books': book_db
    }

    return HttpResponse(template.render(context, request))


def books(request):
    template = loader.get_template('books.html')

    book_db = Book.objects.all().values()

    context = {
        'message': 'List of books:',
        'books': book_db
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'books.html', context)


def book_detail(request, pk):
    template = loader.get_template('book_detail.html')

    book_db = Book.objects.all().values()[pk]

    context = {
        'message': f'Книга під номером: {pk}',
        'books': book_db
    }
    return HttpResponse(template.render(context, request))


def book_by_id(request, id):
    template = loader.get_template('book_detail.html')
    book_db = Book.objects.filter(id=id).values()
    # book_db = Book.objects.get(id=id)

    context = {
        'message': f'Книга з id: {id}',
        # 'book': {
        #     'book_id': book_db.book_id,
        #     'title': book_db.title,
        #     'author': book_db.author,
        #     'year': book_db.year,
        #     'e-book': book_db.ebook,
        #     'file-name': book_db.filename,
        #     'genre': book_db.genre
        # }
        'book': book_db[0]
    }
    return HttpResponse(template.render(context, request))




def book_by_genre(request, genre):
    template = loader.get_template('books.html')

    book_db = Book.objects.filter(genre=genre).values()

    context = {
        'message': f'Книги жанру: {genre}' if len(book_db) else 'Дані відсутні',
        'books': book_db
    }
    return HttpResponse(template.render(context, request))


def book_by_year(request, year):
    template = loader.get_template('books.html')

    book_db = Book.objects.filter(year=year).values()

    context = {
        'message': year,#f'Книги {year} року:' if len(book_db) else 'Дані відсутні',
        'books': book_db
    }
    return HttpResponse(template.render(context, request))


def del_books_all(request):
    """ Видалення всіх книг з БД """
    books_db = Book.objects.all()

    for book in books_db:
        book.delete()

    template = loader.get_template('delete-books.html')

    books_db = Book.objects.all().values()

    context = {
        # 'message': 'All data deleted..' if book_db == None else 'DataBase'
        'message': books_db
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())