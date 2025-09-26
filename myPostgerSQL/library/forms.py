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

SEARCH_CHOICES = [
    ('title', "Назва"),
    ('author', 'Автор'),
    ('year', 'Рік'),
    ('genre', 'Жанр'),

]

class SearchForm(forms.Form):
    field = forms.ChoiceField(
        choices=SEARCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'search'}),
        label="Пошук за"
    )
    query = forms.CharField(label="Запрос", required=False)

