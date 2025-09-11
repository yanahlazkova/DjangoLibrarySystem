from django import forms
from .models import Book, Genre


class BookForm(forms.ModelForm):
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        label='Вибір жанру',
        empty_label='--- Оберіть жанр ---'
    )
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'genre']



