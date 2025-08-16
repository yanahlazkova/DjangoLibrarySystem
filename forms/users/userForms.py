from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(label='First name ')
    last_name = forms.CharField(label='Last name ')
    login = forms.CharField(label='Login ', required=False)
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='E-mail')