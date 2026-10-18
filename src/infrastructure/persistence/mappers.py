from sqlalchemy.orm import registry
from src.integration.telegram.infrastructure.persistence.tables.bot import bot_table
from src.integration.telegram.domain.entity.bot import Bot

mapper_registry = registry()

def start_mappers() -> None:
    mapper_registry.map_imperatively(Bot, bot_table)