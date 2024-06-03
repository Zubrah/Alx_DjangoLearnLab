# Permissions and Groups Setup

## Custom Permissions

The `Book` model has the following custom permissions defined:

- `can_view`: Can view book
- `can_create`: Can create book
- `can_edit`: Can edit book
- `can_delete`: Can delete book

## Groups

The following groups have been created with specific permissions:

- **Editors**
  - Permissions: can_edit, can_create
- **Viewers**
  - Permissions: can_view
- **Admins**
  - Permissions: can_view, can_create, can_edit, can_delete

## Views and Permissions

The following views enforce permissions:

- `book_list`: Requires `can_view` permission
- `book_create`: Requires `can_create` permission
- `book_edit`: Requires `can_edit` permission
- `book_delete`: Requires `can_delete` permission

## Testing Permissions

1. Create test users and assign them to the groups (Editors, Viewers, Admins).
2. Log in as these users and verify access to views (list, create, edit, delete) to ensure permissions are correctly applied.
