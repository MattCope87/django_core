from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput, DateTimeInput

from django.forms import ModelForm
# create/register a user:

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# - authenticating a user (Model Form)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class ExampleForm(forms.Form):
    event = forms.DateTimeField(widget=DateTimeInput())
                  
class ExampleModelForm(forms.Form):
    class Meta:
        widgets = {'ev_date' : DateTimeInput()}


    
