from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Login and Logout Views
    path('login/', auth_views.LoginView.as_view(template_name = 'blog/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Registration view
    path('register/', views.register, name='register'),
    
    # Profile view
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='edit_profile'),
]

