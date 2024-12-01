from rest_framework import generics, serializers
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# ListView to retrieve all books    
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Read-only for unauthenticated users 
    # Add filtering, searrching and ordering features
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    # Define filter fields for filtering
    filtersets_fields = ['title', 'author', 'publication_year']

    # define search fields  for searching
    search_fields = ['title', 'author']

    # Define orderin fields for sorting
    ordering_fields = ['title', 'publication_year']
    Ordering = ['title']

# DetailView to retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

# CreateView to add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books


    def perform_create(self, serializer):
        # Custom validation: prevent books with a future publication year
        publication_year = serializer.validated_data['publication_year']
        if publication_year > 2024:  # Adjust to current or future date validation
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

# UpdateView to modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books


    def perform_update(self, serializer):
        # Custom validation: prevent updates to books that are already published
        book = self.get_object()  # Fetch the current book object
        if book.status == 'published':  # Adjust based on your model's status field
            raise serializers.ValidationError("Cannot update a published book.")
        serializer.save()
    permission_classes = [IsAuthenticated,]  # Only owner or authenticated users


# DeleteView to remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated,]  # Only owner or authenticated users can delete books
