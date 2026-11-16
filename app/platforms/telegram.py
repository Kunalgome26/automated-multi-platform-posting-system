
import httpx

from datetime import datetime, timezone
from app.platforms.base import BasePlatform
from app.config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)


class TelegramPlatform(BasePlatform):

    def __init__(self):
        self.token = TELEGRAM_BOT_TOKEN
        self.chat_id = TELEGRAM_CHAT_ID

        if not self.token or not self.chat_id:
            raise ValueError("Telegram credentials are missing")

        self.api_url = (
            f"https://api.telegram.org/bot{self.token}/sendMessage"
        )

    async def publish(self, message: str) -> dict:

        async with httpx.AsyncClient(timeout=20) as client:

            response = await client.post(
                self.api_url,
                json={
                    "chat_id": self.chat_id,
                    "text": message
                }
            )

            data = response.json()

            # Handle Telegram API errors
            if response.status_code != 200:
                raise Exception(
                    f"Telegram Error {response.status_code}: "
                    f"{data.get('description', response.text)}"
                )

            if not data.get("ok"):
                raise Exception(
                    data.get("description", "Telegram API error")
                )

            # Extract response details
            result = data["result"]

            message_id = result["message_id"]
            timestamp = result["date"]

            posted_time = datetime.fromtimestamp(
                timestamp, tz=timezone.utc
            )

            channel = self.chat_id.lstrip("@")

            posted_url = None
            public_access = False

            if self.chat_id.startswith("@"):
                posted_url = (
                    f"https://t.me/{channel}/{message_id}"
                )
                public_access = True

            return {
                "platform": "Telegram",
                "posted_url": posted_url,
                "public_access": public_access,
                "date": posted_time.strftime("%Y-%m-%d"),
                "time": posted_time.strftime("%H:%M:%S")
            }
