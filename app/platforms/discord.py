
import httpx

from datetime import datetime, timezone
from app.platforms.base import BasePlatform
from app.config import DISCORD_WEBHOOK_URL


class DiscordPlatform(BasePlatform):

    def __init__(self):
        self.webhook_url = DISCORD_WEBHOOK_URL

        if not self.webhook_url:
            raise ValueError("Discord webhook URL is missing")

    async def publish(self, message: str) -> dict:

        async with httpx.AsyncClient(timeout=20) as client:

            response = await client.post(
                self.webhook_url,
                json={"content": message},
                params={"wait": "true"}
            )

            if response.status_code not in (200, 204):
                raise Exception(
                    f"Discord Error {response.status_code}: {response.text}"
                )

            data = response.json()
            timestamp = datetime.now(timezone.utc)

            return {
                "platform": "Discord",
                "posted_url": (
                    f"https://discord.com/channels/"
                    f"{data['guild_id']}/"
                    f"{data['channel_id']}/{data['id']}"
                    if data.get("guild_id") else None
                ),
                "public_access": False,
                "date": timestamp.strftime("%Y-%m-%d"),
                "time": timestamp.strftime("%H:%M:%S")
            }
