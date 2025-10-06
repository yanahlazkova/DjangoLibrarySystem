from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label='Логін')
    password = forms.CharField(label='Пароль')