from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput, DateTimeInput
from . models import Comment


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
        widgets = {'blog_date' : DateTimeInput()}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control comment-textarea',  # Custom class for styling
                    'placeholder': 'Leave a comment!',  # Placeholder text
                    'rows': 4,  
                    'cols': 100, 
                }
            )
        }
        




        