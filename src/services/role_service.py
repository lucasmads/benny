from role_manager import RoleManager
from permission_manager import PermissionManager


class RoleService:

    def __init__(self):

        self.roles = RoleManager()
        self.permissions = PermissionManager()

    def assign_permission(
        self,
        role,
        permission
    ):

        if not self.permissions.exists(
            permission
        ):

            return False

        self.roles.assign_permission(
            role,
            permission
        )

        return True

    def create_role(
        self,
        role
    ):

        return self.roles.create(role)

    def delete_role(
        self,
        role
    ):

        self.roles.delete(role)

    def list_roles(self):

        return self.roles.all()

    def role_permissions(
        self,
        role
    ):

        return self.roles.permissions(role)
