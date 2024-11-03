
### **3. update.md**
```markdown
# Update Operation

## Command
```python
# Updating the title of the book from "1984" to "Nineteen Eighty-Four"
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update.title)

#Expected Output
Nineteen Eighty-Four
