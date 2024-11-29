---

## API Endpoints

- **List Books**: `GET /api/books/`
- **Get Book Details**: `GET /api/books/<int:pk>/`
- **Create a Book**: `POST /api/books/`
- **Update a Book**: `PUT /api/books/<int:pk>/`
- **Delete a Book**: `DELETE /api/books/<int:pk>/`

---

## Custom Views

- **ListView** (`GET /api/books/`): Retrieves all books. Public access.
- **DetailView** (`GET /api/books/<int:pk>/`): Retrieves a single book by ID. Public access.
- **CreateView** (`POST /api/books/`): Allows authenticated users to add a book.
    - Custom validation: Prevents creating books with a future publication year.
- **UpdateView** (`PUT /api/books/<int:pk>/`): Allows authenticated users to update a book.
    - Custom validation: Prevents updating published books.
- **DeleteView** (`DELETE /api/books/<int:pk>/`): Allows authenticated users to delete a book.
    - Custom permission: Only the book owner can delete it.

---

## Permissions

- **ListView/DetailView**: `AllowAny` (public access)
- **CreateView/UpdateView/DeleteView**: `IsAuthenticated` (authenticated users only)
- **Custom Permission** (`IsOwnerOrReadOnly`): Used in `UpdateView` and `DeleteView` to restrict actions to the book owner.

---

## Testing

- **Create Book**: `POST /api/books/` (Requires authentication)
- **Update Book**: `PUT /api/books/<int:pk>/` (Requires authentication)
- **Delete Book**: `DELETE /api/books/<int:pk>/` (Requires authentication and ownership)

---

## Conclusion

This project demonstrates how to build a RESTful API for managing books, using Django REST Framework’s generic views and permissions to ensure security and functionality.
