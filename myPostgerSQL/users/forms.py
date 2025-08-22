from django import forms


class UserForm(forms.Form):
    firstname = forms.CharField(label="First name")
    lastname = forms.CharField(label='Last name')
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='E-mail')
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Password')
    phone = forms.CharField(label='Phone number')


class EditUserForm(forms.Form):
    id = forms.CharField(label='ID', widget=forms.HiddenInput())
    firstname = forms.CharField(label="First name")
    lastname = forms.CharField(label='Last name')
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='E-mail')
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Password')
    phone = forms.CharField(label='Phone number')
