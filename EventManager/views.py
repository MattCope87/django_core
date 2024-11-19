from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
# - authentication models and functions
from .models import Create_Event
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def event(request):
          
    queryset = Create_Event.objects.all()
    context = {'events': queryset}
    return render(request, 'event/events.html', context)

def detail_view(request, id):
    
    queryset = Create_Event.objects.get(id=id)
    context = {'event': queryset}
    return render(request, 'event/detail_view.html', context)

    
def register_view(request):   
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    
    context = {'registerform':form}
    return render(request, 'event/register.html', context=context)

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
                return redirect("event")
            
    context = {'loginform': form}        
            
    return render(request, 'event/login.html', context=context)

def user_logout(request):
    auth.logout(request)
    return redirect('event')
    
 # create function taking the HTTP request object (instance of HTTPRequest) which will extract and handle the data
@login_required(login_url='login/')
def add_event(request):
    print("hit")
    if request.method == 'POST':
        data = request.POST
 # from object 'data' take POST request to get data from ModelForm fields 'ev_name' and 'ev_desc'
        ev_image = request.FILES.get('ev_image')
        ev_name = data.get('ev_name')
        ev_desc = data.get('ev_desc')
        ev_location = data.get('ev_location')
        ev_date = data.get('ev_date')
        
 # Create_event class is called here with DB manager .objects query, .create() method both creates and saves the data instance
        Create_Event.objects.create(
 # values are assigned to the corresponding db fields
            ev_image = ev_image,
            ev_name = ev_name,
            ev_desc = ev_desc,
            ev_location = ev_location,
            ev_date = ev_date,
            user =request.user,
        )
 # return redirect statement returns user to the 'add_event' view upon submitting their data
 # 
        return redirect('event')
    queryset = Create_Event.objects.all()

    context = {'events': queryset}
    return render(request, 'event/add_event.html', context)

def delete_event(request, id):
    print("hit")
    queryset = Create_Event.objects.get(id=id)
    queryset.delete()
    return redirect('event')

def update_event(request, id):
    print("hit")
    queryset = Create_Event.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        ev_name = data.get('ev_name')
        ev_desc = data.get('ev_desc')
        ev_image = request.FILES.get('ev_image')
        ev_date = data.get('ev_date')
        ev_location = data.get('ev_location')
        
        queryset.ev_name = ev_name
        queryset.ev_desc = ev_desc
        queryset.ev_date = ev_date
        queryset.ev_location = ev_location
        
        if ev_image:
            queryset.ev_image = ev_image
        queryset.save()
        return redirect('event')
    context = {'event': queryset}
    return render(request, 'event/update_event.html', context)

def RSVP_event(request, id):
    print(request.method)
    queryset = Create_Event.objects.get(id=id)
    if request.method == 'GET':
        if request.user not in queryset.attendees.all():
            queryset.attendees.add(request.user)
            print("attendance confirmed")
        else:
            print("already signed up")
         
       

    return redirect('detail_view', id=id)

    
def RSVP_list(request):
    queryset = Create_Event.event.attendees.all()
    context = {'events': queryset}
    
    return render(request, 'event/detail_view.html', context)
    
    

def api_event(request):
    events = Create_Event.objects.all()
    events_data = list(events.values())
    return JsonResponse({'event': events_data}, safe=False)        
