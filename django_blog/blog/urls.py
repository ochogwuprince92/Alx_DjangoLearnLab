from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("home/", views.home, name= "home"),
    path("post/", views.post, name= "posts"),
    
    path('', views.PostListView.as_view(), name='post_list'),  # Example list view
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # Detail view
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Create view
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),  # Update view
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete view
    

    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
