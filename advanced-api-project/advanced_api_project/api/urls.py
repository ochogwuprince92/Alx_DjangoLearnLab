from django.urls import path
from .views import (
BookListView, 
BookDetailView, 
BookCreateView, 
BookDeleteView, 
BookupdateView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name = 'book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name= 'book-detail'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/edit/', BookDeleteView.as_view(), name='Book-edit'),
    path('books/<int:pk>/de;ete/', BookDeleteView.as_view(), name='book-delete')

]

