from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle updating the book
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle creating a new book
        pass
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('bookshelf:book_list')  # Redirect to a list of books after deletion

def search_books(request):
    search_term = request.GET.get('search_term', '')
    # Secure ORM-based filtering
    books = Book.objects.filter(title__icontains=search_term)
    return render(request, 'bookshelf/book_list.html', {'books': books})

from .forms import BookForm

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            # Save to the database
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.shortcuts import render
from .forms import ExampleForm  # Ensure this import is correct

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., save to the database)
            pass
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
