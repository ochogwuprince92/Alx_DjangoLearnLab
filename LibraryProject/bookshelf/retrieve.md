```python
# Retrieving books with the title "1984"
retrieved_books = Book.objects.filter(title="1984")
for book in retrieved_books:
    print(book.title, book.author, book.publication_year)

#Expected output
1984 George Orwell 1949
1984 George Orwell 1949
1984 George Orwell 1949
1984 George Orwell 1949

