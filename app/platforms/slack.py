
import os
import httpx
from datetime import datetime, timezone
from dotenv import load_dotenv
from app.platforms.base import BasePlatform

load_dotenv()


class SlackPlatform(BasePlatform):
    def __init__(self):
        self.webhook_url = os.getenv("SLACK_WEBHOOK_URL")

        if not self.webhook_url:
            raise ValueError("Slack webhook URL is missing")

    async def publish(self, message: str) -> dict:
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.post(
                self.webhook_url,
                json={"text": message}
            )

            if response.status_code != 200 or response.text != "ok":
                raise Exception(
                    f"Slack Error {response.status_code}: {response.text}"
                )

            posted_time = datetime.now(timezone.utc)

            return {
                "platform": "Slack",
                "posted_url": None,
                "public_access": False,
                "date": posted_time.strftime("%Y-%m-%d"),
                "time": posted_time.strftime("%H:%M:%S")
            }
