from repository import JsonRepository
from config import AUDIT_LOG_FILE
from utils import timestamp


class AuditService:

    def __init__(self):

        self.repository = JsonRepository(
            AUDIT_LOG_FILE
        )

    def record(
        self,
        username,
        action,
        status
    ):

        logs = self.repository.all()

        logs.append(

            {

                "username": username,

                "action": action,

                "status": status,

                "timestamp": timestamp()

            }

        )

        self.repository.save(logs)

    def all(self):

        return self.repository.all()

    def latest(
        self,
        limit=10
    ):

        return self.all()[-limit:]
