from rest_framework import generics, serializers
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ListView to retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Read-only for unauthenticated users 

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
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Only owner or authenticated users


# DeleteView to remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Only owner or authenticated users can delete books
