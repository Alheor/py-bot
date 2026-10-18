from sqlalchemy import BigInteger, Identity, MetaData, Table, Column, String, Integer, Boolean, DateTime, Uuid
from src.infrastructure.persistence.metadata import metadata

bot_table = Table(
    "bot",
    metadata,
    Column("id", BigInteger, Identity(), primary_key=True),
    Column("uuid", Uuid, nullable=False, unique=True),
    Column("api_key", String(255), nullable=False),
    Column("header_token", String(255), nullable=False),
    Column("user_name", String(255), nullable=False),
    Column("update_id", String(255), nullable=False),
    Column("is_active", Boolean, nullable=False, server_default="true"),
    Column("created_at", DateTime(timezone=True), nullable=False),
    Column("updated_at", DateTime(timezone=True), nullable=False),
)