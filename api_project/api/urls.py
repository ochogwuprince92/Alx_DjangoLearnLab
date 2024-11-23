from django.urls import path, include 
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# initialize the router
router = DefaultRouter()

# register the router
router.register(r'books_all', BookViewSet, basename='book_all')

# include the router's urls
urlpatterns = [
    path('books/', BookList.as_view(), name = 'book-list'),
    path('', include(router.urls)),
]
