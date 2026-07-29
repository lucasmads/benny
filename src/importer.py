import json
from pathlib import Path

from repository import JsonRepository
from config import (
    USERS_FILE,
    ROLES_FILE,
    PERMISSIONS_FILE
)


class Importer:

    def load(self, filename):

        with open(
            filename,
            encoding="utf8"
        ) as file:

            data = json.load(file)

        JsonRepository(
            USERS_FILE
        ).save(
            data.get("users", [])
        )

        JsonRepository(
            ROLES_FILE
        ).save(
            data.get("roles", [])
        )

        JsonRepository(
            PERMISSIONS_FILE
        ).save(
            data.get("permissions", [])
        )

        return True
