# Event Blog

Event blog allows users to register and log in to a shared blogging space. Users can perform basic functions on their blogs such as post, edit, delete, and comment.

## layout

# Django Project File Structure with README.md

Event Blog Manager MC
Django_tutorial/

├── manage.py             
├── db.sqlite3            
├── requirements.txt      
├── .gitignore             
├── README.md             
├── core/           
│   ├── _init_.py       
│   ├── settings.py       
│   ├── urls.py           
│   ├── asgi.py           
│   ├── wsgi.py           
│   └── _pycache_/      
├── blog_app/             
│   ├── migrations/       
│   │   ├── _init_.py    
│   │   └── ...           
│   ├── _init_.py       
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
│                   
├── media/                
│   └── blog_app/blog/blogs               
             


## Installation

### Deployment Environment

Using a Windows operating system and appropriate IDE with python

### Dependencies

Ensure Django is installed: 
* pip install Django

Install Pillow for image processing
* pip install Pillow

### Working directory

Open the folder 'Event Blog Manager MC' in VS Code and ensure 'django_tutorial' is the working directory via terminal:
* C:\...Event Blog Manager MC\django_tutorial>

You should be ready to run the application successfully:
* C:\...Event Blog Manager MC\django_tutorial> python manage.py runserver

You are ready to register and log in to start using the application

## models

two models were created to support the  of our blog functions. Specifically, user details, blog posts. Comment handled individual comments users make as related to 

### Create_Blog

User log in details are stored as well as linking user id to blog id, tracking their activity. 

### Comment

Comments are stored separately but linked through user id to blog id

## Forms

allowing our models to work, we create forms.py to manage validation and finer aspects of data handling such as widgets controlling data input

## views - Blog functionality

* blog
* add_blog
* delete_blog
* update_blog
* detail_view
* delete_comment

Creating objects from our Create_Blog and Comment models alongside Forms classes, the views give users CRUD functionality. Django's library of classes and methods provide the basis for functions

## views - authentication arrangement

* register_view
* login_view
* logout

Using Django's own library, UserCreationForm and AuthenticateForm provide class-based authentication and authorisation for users to register on the application

## Third party packages

bootstrap links are inserted at the top of html templates adding styling

## Test cases


### registering an account


### posting 


