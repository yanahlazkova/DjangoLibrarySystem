from django import forms
from .models import User, Account


class UserForm(forms.Form):
    # class Meta:
    #     model = User
    #     fields = ('login', 'email', 'password')
    login = forms.CharField(label='Login')
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Password')


class EditUserForm(forms.ModelForm):
    firstname = forms.CharField(label='First Name')
    lastname = forms.CharField(label='Last Name')
    age = forms.IntegerField(label='Age')
    phone = forms.CharField(label='Phone')
    class Meta:
        model = Account
        fields = ['email', 'login', 'password', 'firstname', 'lastname', 'age',  'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # если редактируем существующую запись, подтянем данные из связанного User
        if self.instance and self.instance.pk:
            self.fields['firstname'].initial = self.instance.user.firstname if self.instance.user else ""
            self.fields['lastname'].initial = self.instance.user.lastname if self.instance.user else ""
            self.fields['age'].initial = self.instance.user.age if self.instance.user else ""
            self.fields['phone'].initial = self.instance.user.phone if self.instance.user else ""

    def save(self, commit=True):
        # сохраняем Account
        account = super().save(commit=False)

        if commit:
            account.save()

        # сохраняем связанного User
        user = account.user
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.age = self.cleaned_data['age']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()

        return account

SEARCH_CHOICES = [
    ('firstname', "Ім'я"),
    ('lastname', 'Прізвище'),
    ('age', 'Вік'),
    ('phone', 'Телефон'),
    ('email', 'Email'),
    ('login', 'Логін'),
]

class SearchForm(forms.Form):
    field = forms.ChoiceField(
        choices=SEARCH_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'search'}),
        label="Пошук за"
    )
    query = forms.CharField(label="Запрос", required=False)