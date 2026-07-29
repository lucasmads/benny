from pathlib import Path
from datetime import datetime


LOG_FILE = Path("logs/system.log")

LOG_FILE.parent.mkdir(
    exist_ok=True
)


class Logger:

    def write(
        self,
        level,
        message
    ):

        with open(
            LOG_FILE,
            "a",
            encoding="utf8"
        ) as file:

            file.write(

                f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "

                f"{level.upper():8}"

                f"{message}\n"

            )

    def info(self, message):

        self.write(
            "INFO",
            message
        )

    def warning(self, message):

        self.write(
            "WARNING",
            message
        )

    def error(self, message):

        self.write(
            "ERROR",
            message
        )
