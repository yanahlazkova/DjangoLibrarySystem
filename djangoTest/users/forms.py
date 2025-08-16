from django import forms


class UserForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
