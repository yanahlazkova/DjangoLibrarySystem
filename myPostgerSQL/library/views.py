from asgiref.typing import HTTPRequestEvent
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookForm
from library.models import Genre, Book, UserBooks
from users.models import User

from datetime import datetime

def main(request):
    return render(request, 'main.html')


def books(request):
    form = BookForm()
    if request.method == 'GET':
        list_books = Book.objects.all().values('title', 'author', 'year', 'genre__name')
        context = {
            'form': form,
            'books': list_books,
        }

        return render(request, 'books.html', context=context)
    return redirect('main')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Книга успешно добавлена!')
            return redirect('books')
        else:
            # Если форма невалидна, выводим сообщение об ошибке
            messages.error(request, 'Произошла ошибка при сохранении книги.')
        return redirect('books')
    else:
        return redirect('books')



def new_genre(request):
    if request.method == 'POST':
        genre_name = request.POST.get('genre')
        try:
            genre, created = Genre.objects.get_or_create(name=genre_name)

            if created:
                message = f'Жанр "{genre.name}" успешно добавлен.'
                # Возвращаем JSON-ответ с данными о жанре
                return JsonResponse({
                    'success': True,
                    'message': message,
                    'id': genre.id,
                    'name': genre.name
                })
            else:
                message = f'Жанр "{genre.name}" уже существует.'
                return JsonResponse({
                    'success': False,
                    'message': message,
                })

        except Exception as e:
            # Обработка других возможных ошибок
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

            # Если запрос не POST, возвращаем ошибку
    return JsonResponse({'success': False, 'message': 'Неверный метод запроса.'}, status=405)


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'GET':
        form = BookForm(instance=book)
        # print()
        # print(book)
        # print()
        context = {
            'form': form,
            'book': book,
        }
        return render(request, 'books.html', context=context)


def deleted_all_genres(request):
    try:
        # Удаляем все записи из модели Book
        deleted_count, _ = Genre.objects.all().delete()
        return JsonResponse({'success': True, 'message': f'Удалено {deleted_count} книг.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


def library(request):
    if request.method == 'GET':
        users = (User.objects.all()
                 .exclude(firstname=None)
                 .exclude(lastname=None)
                 .order_by('id')
                 .values('id', 'firstname', 'lastname', 'account__email')
                 )

        books = (Book.objects.all().order_by('id')
                 .values('id', 'title', 'author', 'year', 'genre__name', 'borrows__date_received', 'borrows__date_returned'))
        # print()
        # print(books[23])
        # print()
        context = {
            'users': users,
            'books': books,
        }
        return render(request, 'library.html', context=context)
    return render(request, 'library.html')


def receive_books(request):
    if request.method == 'POST':
        select_user_id = request.POST.get('select_user')
        selected_books_id = request.POST.getlist('select_book')

        user_db = get_object_or_404(User, id=select_user_id)

        user_db.books.add(*selected_books_id)

        current_time = datetime.now()

        for book_id in selected_books_id:
            user_book_entry = UserBooks.objects.get(user=select_user_id, book=book_id, date_received=None)
            user_book_entry.date_received = current_time
            user_book_entry.save()

        list_received_books = user_db.books.all().values(
            'title',
            'author',
            'year',
            'genre__name',
            'borrows__date_received',
            'borrows__date_returned').filter(borrows__date_received=current_time).order_by('id')

        context = {
            'title': f'{user_db.firstname} {user_db.lastname}',
            'user': f'{user_db.firstname} {user_db.lastname}',
            'message': 'Видано книжки:',
            'books': list_received_books,
        }

        return render(request, 'user_books.html', context=context)

    return redirect('library')


def user_books(request, user_id=None):
    """ Вивід взятих та повернутих книжок обраного читача"""
    if request.method == 'GET':
        user = User.objects.get(id=user_id)

        list_books = user.books.all().values('id', 'title', 'author', 'year', 'genre__name', 'borrows__date_received',
                                             'borrows__date_returned').order_by('id')
        context = {
            'title': f'{user.firstname} {user.lastname}',
            'user': user,
            'books': list_books,
        }

        return render(request, 'user_books.html', context=context)
    return redirect('library')


def return_books(request, user_id=None):
    if request.method == 'POST':
        selected_books_id = request.POST.getlist('select_book')
        user_db = get_object_or_404(User, id=user_id)

        # user_db.books.add(*selected_books_id)

        current_time = datetime.now()

        for book_id in selected_books_id:
            user_book_entry = UserBooks.objects.get(user=user_id, book=book_id)
            user_book_entry.date_returned = current_time
            user_book_entry.save()
            print('!!!Return:', user_book_entry)


        # return redirect('library')
        return redirect('user_books', user_id=user_id)
