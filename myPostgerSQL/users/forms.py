from django import forms
from .models import User


class UserForm(forms.Form):
    # firstname = forms.CharField(label="First name")
    # lastname = forms.CharField(label='Last name')
    # age = forms.IntegerField(label='Age')
    login = forms.CharField(label='Login')
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Password')
    # phone = forms.CharField(label='Phone number')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'age', 'email',
                  'login', 'password', 'phone']
