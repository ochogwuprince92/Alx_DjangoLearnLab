from django.urls import path
from .views import RegisterUserView, CustomAuthToken, UserProfileView,  FollowUserView, UnfollowUserView, UserListView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path("login/", CustomAuthToken.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('users/', UserListView.as_view(), name='user_list'),
]
