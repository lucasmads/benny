from repository import JsonRepository
from config import (
    USERS_FILE,
    ROLES_FILE,
    PERMISSIONS_FILE
)


class Statistics:

    def __init__(self):

        self.users = JsonRepository(USERS_FILE)
        self.roles = JsonRepository(ROLES_FILE)
        self.permissions = JsonRepository(PERMISSIONS_FILE)

    def summary(self):

        return {

            "users": len(self.users.all()),

            "roles": len(self.roles.all()),

            "permissions": len(
                self.permissions.all()
            )

        }

    def print_summary(self):

        stats = self.summary()

        print()

        print("System Statistics")

        print("-" * 25)

        for key, value in stats.items():

            print(f"{key.capitalize():15}: {value}")
