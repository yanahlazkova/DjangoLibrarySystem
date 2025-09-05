from django import forms
from .models import User


class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ('login', 'email', 'password')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'age', 'email',
                  'login', 'password', 'phone']
