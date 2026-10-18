from fastapi import APIRouter, Header, HTTPException
from src.integration.telegram.schemas import webhook_schema
from src.integration.telegram.client import TelegramClient
from config.config import settings
from src.application.Us eCase import message_receiver

router = APIRouter()

@router.post("/webhook")
async def webhook(
        update: webhook_schema.WebhookBody,
        x_telegram_bot_api_secret_token: str | None = Header(default=None)
):
    if x_telegram_bot_api_secret_token != settings.webhook_secret:
        raise HTTPException(status_code=403)

    telegram_client = TelegramClient(settings.bot_token)

    await message_receiver.handle_update(update, telegram_client)

    return {"status": "ok"}