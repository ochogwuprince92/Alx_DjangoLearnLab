```python
# Deleting the book with the title "Nineteen Eighty-Four"
book_to_delete = Book.objects.filter(title="Nineteen Eighty-Four").first()
book_to_delete.delete()
remaining_books = Book.objects.filter(title="1984")
print(f"Books remaining titled '1984': {remaining_books.count()}")

#Expected Output
Books remaining titled '1984': 0
