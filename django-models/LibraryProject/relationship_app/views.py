# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library  # Import both Book and Library models
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Full path for the template

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Full path for the template
    context_object_name = 'library'
