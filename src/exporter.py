import json
from pathlib import Path
from datetime import datetime

from repository import JsonRepository
from config import (
    USERS_FILE,
    ROLES_FILE,
    PERMISSIONS_FILE,
    EXPORT_DIR
)


class Exporter:

    def export_all(self):

        data = {

            "users": JsonRepository(
                USERS_FILE
            ).all(),

            "roles": JsonRepository(
                ROLES_FILE
            ).all(),

            "permissions": JsonRepository(
                PERMISSIONS_FILE
            ).all()

        }

        filename = (
            EXPORT_DIR /
            f"permissions_"
            f"{datetime.now():%Y%m%d_%H%M%S}.json"
        )

        with open(
            filename,
            "w",
            encoding="utf8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        return filename
