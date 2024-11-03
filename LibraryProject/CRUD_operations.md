# CRUD Operations Documentation

This document provides an overview of the CRUD operations performed on the Book model in the Django application.

## 1. Create Operation

### Command
```python
# Creating a new Book instance
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

1984

# Retrieving books with the title "1984"
retrieved_books = Book.objects.filter(title="1984")
for book in retrieved_books:
    print(book.title, book.author, book.publication_year)

1984 George Orwell 1949
1984 George Orwell 1949
1984 George Orwell 1949
1984 George Orwell 1949

# Updating the title of the book "1984" to "Nineteen Eighty-Four"
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update.title)

Nineteen Eighty-Four

# Deleting the book titled "Nineteen Eighty-Four"
book_to_delete = Book.objects.filter(title="Nineteen Eighty-Four").first()
book_to_delete.delete()

# Confirming the deletion
remaining_books = Book.objects.filter(title="1984")
print(f"Books remaining titled '1984': {remaining_books.count()}")

Books remaining titled '1984': 0

