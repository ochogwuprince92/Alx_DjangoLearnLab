from django.shortcuts import render
from rest_framework.generics import ListAPIView, DetailAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Book
from .serializers import BookSerializer
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# create ListView
class BookListView(ListAPIView):
    """
    API endpoint to retrieve all books.
    Supports filtering by author and publication_year.
    Open to unauthenticated users for read-only access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'publication_year']

# create DetailView
class BookDetailView(DetailAPIView):
    queryset = Book.objects.all()
    Serializer_class =BookSerializer

# create CreateView 
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # only authenticated user can add books

# create UpdateAView
class BookupdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # only authenticated user can add books 

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
