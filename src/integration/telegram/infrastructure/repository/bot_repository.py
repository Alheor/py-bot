from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from src.integration.telegram.domain.entity.bot import Bot


class SqlAlchemyProductRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, uuid: UUID) -> Bot | None:
        return await self._session.get(Bot, uuid)