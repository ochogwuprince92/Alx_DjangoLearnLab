from django.urls import path, include 
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token    # Import DRF's token view

# initialize the router
router = DefaultRouter()

# register the router
router.register(r'books_all', BookViewSet, basename='book_all')

# include the router's urls
urlpatterns = [
    path('books/', BookList.as_view(), name = 'book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name = 'api_token_auth'), # Endpoint for token retrieval
]
