from config import USERS_FILE
from repository import JsonRepository


class AuthService:

    def __init__(self):

        self.repository = JsonRepository(USERS_FILE)

    def authenticate(self, username: str):

        users = self.repository.all()

        for user in users:

            if user["username"] == username:

                return user

        return None

    def exists(self, username: str):

        return self.authenticate(username) is not None

    def role(self, username: str):

        user = self.authenticate(username)

        if not user:

            return None

        return user["role"]
