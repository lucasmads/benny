from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

USERS_FILE = DATA_DIR / "users.json"
ROLES_FILE = DATA_DIR / "roles.json"
PERMISSIONS_FILE = DATA_DIR / "permissions.json"
AUDIT_LOG_FILE = DATA_DIR / "audit_log.json"

EXPORT_DIR = DATA_DIR / "exports"
BACKUP_DIR = DATA_DIR / "backups"

EXPORT_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)
