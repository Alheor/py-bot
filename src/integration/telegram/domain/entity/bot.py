from dataclasses import dataclass, field
from datetime import datetime, UTC
from uuid import UUID, uuid7

@dataclass
class Bot:
    api_key: str
    user_name: str
    update_id: str
    header_token: str
    id: int | None = field(default=None, init=False)
    uuid: UUID = field(default_factory=uuid7)
    is_active: bool = True
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def deactivate(self) -> None:
        if not self.is_active:
            return
        self.is_active = False
        self._touch()

    def _touch(self) -> None:
        self.updated_at = datetime.now(UTC)