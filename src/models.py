from dataclasses import dataclass, field


@dataclass
class Role:
    name: str
    permissions: list[str] = field(default_factory=list)


@dataclass
class User:
    username: str
    role: str


@dataclass
class Permission:
    name: str
    description: str = ""


@dataclass
class AuditRecord:
    username: str
    action: str
    status: str
    timestamp: str
