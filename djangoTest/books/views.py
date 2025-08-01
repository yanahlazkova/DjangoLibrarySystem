import json
import os

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from faker import Faker

from books.models import Reader, Book


# def add_books(request):
#     template = loader.get_template('add_books.html')
#     return HttpResponse(template.render())


def add_reader_to_db(request):
    fake = Faker(['uk_UA'])
    readers = []
    for _ in range(3):
        reader = Reader(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            email=fake.email(domain='ukr.net')
        )
        reader.save()
    template = loader.get_template('readers.html')

    readers_db = Reader.objects.all().values()

    context = {
        'readers': readers_db
    }

    return HttpResponse(template.render(context, request))


def change_email_reader():
    fake = Faker()
    readers = Reader.objects.all()
    for reader in readers:
        reader.email = fake.email()
        reader.save()


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
    template = loader.get_template('books.html')

    book_db = Book.objects.filter(id=id).values()

    context = {
        'message': f'Книга з id: {id}' if len(book_db) else 'Дані відсутні',
        'books': book_db
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