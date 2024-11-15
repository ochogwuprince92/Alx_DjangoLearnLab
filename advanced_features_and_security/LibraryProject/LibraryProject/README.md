can_view: Allows users to view books.

can_create: Allows users to create new books.

can_edit: Allows users to edit existing books.

can_delete: Allows users to delete books.

Editors: Can view, create, and edit books.

Viewers: Can only view books.

Admins: Can view, create, edit, and delete books.

Assign the relevant permissions to users by assigning them to the appropriate group.

Use the @permission_required decorator in views to enforce permission checks.