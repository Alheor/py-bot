import httpx

class TelegramClient:
    def __init__(self, token: str):
        self._base_url = f"https://api.telegram.org/bot{token}"

    async def send_message(self, chat_id: int, text: str) -> None:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self._base_url}/sendMessage",
                json={"chat_id": chat_id, "text": text},
            )
            response.raise_for_status()