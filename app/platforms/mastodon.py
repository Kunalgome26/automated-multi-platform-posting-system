
import os
import httpx
from datetime import datetime
from dotenv import load_dotenv
from app.platforms.base import BasePlatform

load_dotenv()


class MastodonPlatform(BasePlatform):

    def __init__(self):
        self.access_token = os.getenv("MASTODON_ACCESS_TOKEN")
        self.base_url = os.getenv(
            "MASTODON_API_BASE_URL",
            "https://mastodon.social"
        ).rstrip("/")

        if not self.access_token:
            raise ValueError("Mastodon access token is missing")

    async def publish(self, message: str) -> dict:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                f"{self.base_url}/api/v1/statuses",
                headers={
                    "Authorization": f"Bearer {self.access_token}"
                },
                json={
                    "status": message,
                    "visibility": "public"
                }
            )

            if response.status_code not in (200, 201):
                raise Exception(
                    f"Mastodon Error {response.status_code}: "
                    f"{response.text}"
                )

            data = response.json()
            created_at = datetime.fromisoformat(
                data["created_at"].replace("Z", "+00:00")
            )

            return {
                "platform": "Mastodon",
                "posted_url": data.get("url"),
                "public_access": data.get("visibility") == "public",
                "date": created_at.strftime("%Y-%m-%d"),
                "time": created_at.strftime("%H:%M:%S")
            }
