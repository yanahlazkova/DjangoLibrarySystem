from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('books/', views.books, name='books'),
    # path('books/<int:pk>', views.book_detail, name='book_pk'),
    path('books/<int:id>', views.book_by_id, name='book_id'),
    path('books/<str:genre>', views.book_by_genre, name='book_genre'),
    path('books/year/<str:year>', views.book_by_year, name='book_year'),
    path('add/books/', views.add_books_to_db, name='add_books'),
    path('del-books/', views.del_books_all, name='del_books'),
    path('add/reader/', views.new_reader, name='new_reader'),
    path('readers/', views.readers_all, name='readers'),
    path('reader/', views.add_reader, name='add_reader'),
    path('readers/<int:id>', views.reader_id, name='reader_id'),
]
