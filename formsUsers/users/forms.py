from django import forms


class UserForm(forms.Form):
    firstname = forms.CharField(label="First name")
    lastname = forms.CharField(label='Last name')
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='E-mail')


class EditUserForm(forms.Form):
    id = forms.CharField(label='ID')
    firstname = forms.CharField(label="First name")
    lastname = forms.CharField(label='Last name')
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='E-mail')
