from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name='books'),
    path('add/', views.add_books, name='add_books')
]