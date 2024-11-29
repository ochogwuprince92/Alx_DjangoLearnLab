# Book API Views

## Endpoints:

1. **List all books**: `GET /books/`
2. **Retrieve a book**: `GET /books/<id>/`
3. **Add a book**: `POST /books/add/`
4. **Update a book**: `PUT /books/<id>/edit/`
5. **Delete a book**: `DELETE /books/<id>/delete/`

## Permissions:

- **List and Retrieve**: Open to all users (read-only).
- **Create, Update, and Delete**: Restricted to authenticated users.

## Filters:
- ListView supports filtering by:
  - `author`
  - `publication_year`

