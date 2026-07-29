from auth import AuthService
from role_manager import RoleManager


class AccessService:

    def __init__(self):

        self.auth = AuthService()
        self.roles = RoleManager()

    def has_permission(
        self,
        username: str,
        permission: str
    ) -> bool:

        role = self.auth.role(username)

        if role is None:
            return False

        permissions = self.roles.permissions(role)

        return permission in permissions

    def check(
        self,
        username: str,
        permission: str
    ):

        if self.has_permission(
            username,
            permission
        ):

            print(
                f"Access granted for '{username}'."
            )

        else:

            print(
                f"Access denied for '{username}'."
            )
