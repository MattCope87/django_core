from django.urls import path
from . import views

# path here includes - URL in '', views module and name
urlpatterns = [
    path('', views.blog, name='blog'),
    
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.user_logout, name="user_logout"),

    path('blogs/add_blog/', views.add_blog, name='add_blog'),
    path('blogs/<int:id>/detail_view/', views.detail_view, name='detail_view'),
    path('blogs/<int:id>/delete', views.delete_blog, name='delete_blog'),
    path('blogs/<int:id>/update_blog/', views.update_blog, name="update_blog"),
    path('blogs/blog_data/', views.blog_api, name="blog_data"),
    path('blogs/<int:id>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
        
    
]