<div style="background-color: white; color: black; font-family: Arial, sans-serif; padding: 10px;">

# blog_app - about

Event blog allows users to register and log in to a shared blogging space. Users can perform basic functions such as post, edit, delete, and comment.

# layout

### Django Project File Structure with README.md

```
Blog Manager MC
django_tutorial/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .gitignore
├── README.md
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __pycache__/
├── blog_app/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── ...
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── blog/
│           ├── add_blog.html
│           ├── base.html
│           ├── blogs.html
│           ├── detail_view.html
│           ├── login.html
│           ├── register.html
│           └── update_blog.html
├── media/
│   └── blog_app/
│       └── blog/
│           └── blogs/
```
          

# Installation

### Deployment Environment

Using a Windows operating system and appropriate IDE with python

### Dependencies

```
Ensure Django is installed: 
* pip install Django

Install Pillow for image processing
* pip install Pillow
```

### Working directory
```
Open the folder 'Event Blog Manager MC' in VS Code and ensure 'django_tutorial' is the working directory via terminal:
* C:\...Blog Manager MC\django_tutorial>

You should be ready to run the application successfully:
* C:\...Blog Manager MC\django_tutorial> python manage.py runserver
```
You are ready to register and log in to start using the application

## Models
Two models were created to support the  of our blog functions. Specifically, user details, blog posts. Comment handled individual comments users make as related to 

1. **Create_Blog**
User log in details are stored as well as linking user id to blog id, tracking their activity. 

2. **Comment**
Comments are stored separately but linked through user id to blog id

## Forms

allowing our models to work, we create forms.py to manage validation and finer aspects of data handling such as widgets controlling data input

```
# - authenticating a user (Model Form)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# - formatting text input
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
 

```

## Views - Blog functionality

* blog
* add_blog
* delete_blog
* update_blog
* detail_view
* delete_comment

Creating objects from our Create_Blog and Comment models alongside Forms classes, the views give users CRUD functionality. Django's library of classes and methods provide the basis for functions

## Views - Authentication arrangement

* register_view
* login_view
* logout

Using Django's own library, UserCreationForm and AuthenticateForm provide class-based authentication and authorisation for users to register on the application. Forms.py further enables us to validate user authentication input with widgets

# Third party packages

bootstrap links are inserted at the top of html templates adding styling

```
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
```



# Test cases and form validation

### registering an account:
![alt text](<media/test_img/Screenshot 2024-12-02 202206.png>)

### logging into an account:
![log in](<media/test_img/Screenshot 2024-12-02 202013.png>)

### posting a blog
![alt text](<media/test_img/Screenshot 2024-12-02 202145.png>)

### users must be logged in to comment
![alt text](<media/test_img/Screenshot 2024-12-02 202357.png>)

### input validation - fields must be complete
![alt text](<media/test_img/Screenshot 2024-12-02 205611.png>)
![alt text](<media/test_img/Screenshot 2024-12-02 205631.png>)
![alt text](<media/test_img/Screenshot 2024-12-02 205419.png>)
![alt text](<media/test_img/Screenshot 2024-12-02 205433.png>)

### username and timestamp record
![alt text](<media/test_img/Screenshot 2024-12-02 202458.png>)


## Unit and integration testing within blog_app

```
from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from .models import Create_Blog

# Create your tests here.

class BlogViewTest(TestCase):
    def setUp(self):
        # Create a user and a blog post for the tests
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')
        self.blog = Create_Blog.objects.create(
            user=self.user,
            blog_title="Test Test",
            blog_entry="This is a test blog post"
        )
        self.client = Client()

class UserViewsTest(TestCase):
    def setUp(self):
        # Create a user for the tests
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')

```