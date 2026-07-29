from config import ROLES_FILE
from repository import JsonRepository


class RoleManager:

    def __init__(self):

        self.repository = JsonRepository(ROLES_FILE)

    def all(self):

        return self.repository.all()

    def create(self, name: str):

        roles = self.all()

        if any(role["name"] == name for role in roles):
            return False

        roles.append(
            {
                "name": name,
                "permissions": []
            }
        )

        self.repository.save(roles)

        return True

    def delete(self, name: str):

        roles = [
            role
            for role in self.all()
            if role["name"] != name
        ]

        self.repository.save(roles)

    def assign_permission(
        self,
        role_name,
        permission
    ):

        roles = self.all()

        for role in roles:

            if role["name"] == role_name:

                if permission not in role["permissions"]:

                    role["permissions"].append(permission)

        self.repository.save(roles)

    def permissions(self, role_name):

        for role in self.all():

            if role["name"] == role_name:

                return role["permissions"]

        return []
