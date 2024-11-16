can_view: Allows users to view books.

can_create: Allows users to create new books.

can_edit: Allows users to edit existing books.

can_delete: Allows users to delete books.

Editors: Can view, create, and edit books.

Viewers: Can only view books.

Admins: Can view, create, edit, and delete books.

Assign the relevant permissions to users by assigning them to the appropriate group.

Use the @permission_required decorator in views to enforce permission checks.

## Security Measures

- **DEBUG = False**: Disabled debug mode in production to prevent sensitive data leakage.
- **CSRF and Session Cookies**: Configured to be sent only over HTTPS.
- **Content Security Policy**: Restricts content loading to trusted sources.
- **ORM Queries**: Used Django ORM to prevent SQL injection vulnerabilities.
