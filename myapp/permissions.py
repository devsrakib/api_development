from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("myapp.add_owner"):
                return True
            if user.has_perm("myapp.delete_owner"):
                return True
            if user.has_perm("myapp.change_owner"):
                return True
            if user.has_perm("myapp.view_owner"):
                return True
            return False
        return False
