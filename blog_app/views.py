from django.shortcuts import render, redirect, get_object_or_404
from . forms import CreateUserForm, LoginForm, CommentForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
# - authentication models and functions
from .models import Create_Blog, Comment
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def blog(request):
          
    queryset = Create_Blog.objects.all()
    context = {'blogs': queryset}
    return render(request, 'blog/blogs.html', context)

def detail_view(request, id):
    blog = Create_Blog.objects.get(id=id)
    comments = blog.comments.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user = request.user
            comment.save()
            return redirect('detail_view', id=blog.id)
        print("hit")
    context = {'blog': blog, "comments": comments, "form": form}
    return render(request, 'blog/detail_view.html', context)

def delete_comment(request, id, comment_id):
    blog = Create_Blog.objects.get(id=id)
    comment = Comment.objects.get(id=comment_id)
    
    if request.user == comment.user:
        comment.delete()
    return redirect('detail_view', id=blog.id)

def register_view(request):   
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')  
    context = {'registerform':form}
    return render(request, 'blog/register.html', context=context)

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:      
                auth.login(request, user)
                return redirect("blog")           
    context = {'loginform': form}                
    return render(request, 'blog/login.html', context=context)

def user_logout(request):
    auth.logout(request)
    return redirect('blog')

 # create function taking the HTTP request object (instance of HTTPRequest) which will extract and handle the data
@login_required(login_url='login/')
def add_blog(request):
    print("hit")
    if request.method == 'POST':
        data = request.POST
 # from object 'data' take POST request to get data from ModelForm fields 'ev_name' and 'ev_desc'
        blog_image = request.FILES.get('blog_image')
        blog_title = data.get('blog_title')
        blog_entry = data.get('blog_entry')
        #blog_date = data.get('blog_date')
 # Create_event class is called here with DB manager .objects query, .create() method both creates and saves the data instance
        Create_Blog.objects.create(
 # values are assigned to the corresponding db fields
            blog_image = blog_image,
            blog_title = blog_title,
            blog_entry = blog_entry,  
            #blog_date = blog_date,
            user =request.user,
        )
 # return redirect statement returns user to the 'add_blog' view upon submitting their data
 # 
        return redirect('blog')
    queryset = Create_Blog.objects.all()

    context = {'blogs': queryset}
    return render(request, 'blog/add_blog.html', context)

def delete_blog(request, id):
    print("hit")
    queryset = Create_Blog.objects.get(id=id)
    queryset.delete()
    return redirect('blog')

def update_blog(request, id):
    print("hit")
    queryset = Create_Blog.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        blog_title = data.get('blog_title')
        blog_entry = data.get('blog_entry')
        blog_image = request.FILES.get('blog_image')
        #blog_date = data.get('blog_date')
        
        queryset.blog_title = blog_title
        queryset.blog_entry = blog_entry
        #queryset.blog_date = blog_date
                
        if blog_image:
            queryset.blog_image = blog_image
        queryset.save()
        return redirect('blog')
    context = {'blog': queryset}
    return render(request, 'blog/update_blog.html', context)

<<<<<<< HEAD
def make_comment(request, id):
    print(request.method)
    queryset = Create_Blog.objects.get(id=id)
    if request.method == 'GET':
        if request.user not in queryset.users.all():
            queryset.bloggers.add(request.user)
            print("attendance confirmed")
        else:
            print("already signed up")
    return redirect('detail_view', id=id)
    
def comment_list(request):
    queryset = Create_Blog.blog.user.all()
    context = {'blogs': queryset}
    
    return render(request, 'blog/detail_view.html', context)
    
def blog_api(request):
    blog = Create_Blog.objects.all()
    blog_data = list(blog.values())
    return JsonResponse({'blog': blog_data}, safe=False)
=======



>>>>>>> ce1974e3619c3c589ecee2e551378dbca30b5f0a
