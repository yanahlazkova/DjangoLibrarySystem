from django import forms


class UserForm(forms.Form):
    firstname = forms.CharField(label="First name")
    lastname = forms.CharField(label='Last name')
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='E-mail')


class EditUserForm(forms.Form):
    id = forms.CharField(label='ID', widget=forms.HiddenInput())
    firstname = forms.CharField(label="First name")
    lastname = forms.CharField(label='Last name')
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='E-mail')
    language = forms.ChoiceField(label='Language',
                                 required=False,
                                 choices={'RU': 'російська',
                                          "UK": 'українська',
                                          "EN": 'англійська',
                                          },
                                 initial=''
                                 )


# from django import forms
#
#
# class UserForm(forms.Form):
#     firstname = forms.CharField(label="First name",
#                                 help_text='Enter the firstname',
#                                 error_messages={"required": "Please enter your name"},
#                                 )
#     lastname = forms.CharField(label='Last name')
#     age = forms.IntegerField(label='Age')
#     email = forms.EmailField(label='E-mail')
#
#
# class EditUserForm(forms.Form):
#     id = forms.CharField(label='ID', widget=forms.HiddenInput())
#     # id = forms.CharField(label='ID', disabled=True)
#     firstname = forms.CharField(label="First name")
#     lastname = forms.CharField(label='Last name')
#     age = forms.IntegerField(label='Age')
#     email = forms.EmailField(label='E-mail')
#     language = forms.ChoiceField(label='Language') #,
#     #                              required=False,
#     #                              help_text='Choice the ')
