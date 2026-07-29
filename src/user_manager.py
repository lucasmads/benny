from config import USERS_FILE
from repository import JsonRepository


class UserManager:

    def __init__(self):

        self.repository = JsonRepository(USERS_FILE)

    def all(self):

        return self.repository.all()

    def create(
        self,
        username,
        role
    ):

        users = self.all()

        if any(
            user["username"] == username
            for user in users
        ):
            return False

        users.append(
            {
                "username": username,
                "role": role
            }
        )

        self.repository.save(users)

        return True

    def delete(self, username):

        users = [
            user
            for user in self.all()
            if user["username"] != username
        ]

        self.repository.save(users)

    def change_role(
        self,
        username,
        role
    ):

        users = self.all()

        for user in users:

            if user["username"] == username:

                user["role"] = role

        self.repository.save(users)

    def get(self, username):

        for user in self.all():

            if user["username"] == username:

                return user

        return None
