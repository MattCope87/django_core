from django.urls import path
from . import views

# path here includes - URL in '', views module and name
urlpatterns = [
    path('', views.event, name='event'),
    
    path('register/', views.register_view, name='register_view'),
    
    path('login/', views.login_view, name='login_view'),
    
    path('events/add_event/', views.add_event, name='add_event'),
    
    path('events/<int:id>/detail_view/', views.detail_view, name='detail_view'),
    
    path('events/<int:id>/delete', views.delete_event, name='delete_event'),
    
    path('logout/', views.user_logout, name="user_logout"),
    
    path('events/<int:id>/update_event/', views.update_event, name="update_event"),

    path('events/<int:id>/RSVP_event/', views.RSVP_event, name="RSVP_event")
    
]
