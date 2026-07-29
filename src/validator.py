from repository import JsonRepository
from config import USERS_FILE, ROLES_FILE, PERMISSIONS_FILE


class Validator:

    def __init__(self):

        self.users = JsonRepository(USERS_FILE)
        self.roles = JsonRepository(ROLES_FILE)
        self.permissions = JsonRepository(PERMISSIONS_FILE)

    def username(self, username: str) -> bool:

        return (
            len(username.strip()) >= 3
            and username.isalnum()
        )

    def role_exists(self, role: str) -> bool:

        roles = self.roles.all()

        return any(
            r["name"] == role
            for r in roles
        )

    def permission_exists(self, permission: str) -> bool:

        permissions = self.permissions.all()

        return any(
            p["name"] == permission
            for p in permissions
        )

    def user_exists(self, username: str) -> bool:

        users = self.users.all()

        return any(
            u["username"] == username
            for u in users
        )
