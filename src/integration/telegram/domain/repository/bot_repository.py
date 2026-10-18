from typing import Protocol
from uuid import UUID
from src.integration.telegram.domain.entity.bot import Bot

class BotRepository(Protocol):
    async def get(self, uuid: UUID) -> Bot | None: ...