from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логін')
    password = forms.CharField(label='Пароль')


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логін')
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Паролі не зпівпадають.")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такий E-mail вже існує.")
        return email
