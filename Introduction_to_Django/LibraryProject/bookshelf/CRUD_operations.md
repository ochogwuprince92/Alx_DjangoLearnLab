```python
>>> from bookshelf import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# output: 
<Book: '1984' by George Orwell>

>>> book = Book.objects.get(title="1984")
>>> book.title, book.author, book.publication_year
# Output:
('1984', 'George Orwell', 1949)

>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title
# Output:
'Nineteen Eighty-Four'

>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
>>> Book.objects.all()
# output:
<QuerySet []>

