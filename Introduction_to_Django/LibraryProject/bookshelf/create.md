```python
>>> from bookshelf import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# output:
<Book: '1984' by George Orwell>