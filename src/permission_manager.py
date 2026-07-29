from config import PERMISSIONS_FILE
from repository import JsonRepository


class PermissionManager:

    def __init__(self):

        self.repository = JsonRepository(PERMISSIONS_FILE)

    def all(self):

        return self.repository.all()

    def add(self, name: str):

        permissions = self.all()

        if any(p["name"] == name for p in permissions):
            return False

        permissions.append(
            {
                "name": name
            }
        )

        self.repository.save(permissions)

        return True

    def delete(self, name: str):

        permissions = [
            permission
            for permission in self.all()
            if permission["name"] != name
        ]

        self.repository.save(permissions)

    def exists(self, name: str):

        permissions = self.all()

        return any(
            permission["name"] == name
            for permission in permissions
        )
