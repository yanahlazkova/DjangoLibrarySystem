from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('books/', views.books, name='books'),
    path('library/', views.library, name='library'),
    path('new_book/', views.add_book, name='add_book'),
    path('genre/', views.new_genre, name='new_genre'),
    path('del/', views.deleted_all_genres, name='deleted_all_genres'),
    path('receive_books/', views.receive_books, name='receive_books'),
    path('user_books/<int:user_id>/', views.user_books, name='user_books'),
    path('return_books/<int:user_id>/', views.return_books, name='return_books'),
    path('book_users/<int:book_id>/', views.book_users, name='book_users'),
]