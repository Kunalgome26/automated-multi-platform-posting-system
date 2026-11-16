
import os
import httpx
from datetime import datetime, timezone
from dotenv import load_dotenv
from app.platforms.base import BasePlatform

load_dotenv()


class BlueskyPlatform(BasePlatform):
    BASE_URL = "https://bsky.social/xrpc"

    def __init__(self):
        self.handle = os.getenv("BLUESKY_HANDLE")
        self.password = os.getenv("BLUESKY_APP_PASSWORD")

        if not self.handle or not self.password:
            raise ValueError("Bluesky credentials are missing")

    async def publish(self, message: str) -> dict:
        async with httpx.AsyncClient(timeout=30) as client:

            # Step 1: Login and create a session
            login_response = await client.post(
                f"{self.BASE_URL}/com.atproto.server.createSession",
                json={
                    "identifier": self.handle,
                    "password": self.password
                }
            )

            if login_response.status_code != 200:
                raise Exception(
                    f"Bluesky Login Error: {login_response.text}"
                )

            session = login_response.json()
            access_token = session["accessJwt"]
            user_did = session["did"]

            # Step 2: Publish the post
            now = datetime.now(timezone.utc)
            created_at = now.isoformat().replace("+00:00", "Z")

            post_response = await client.post(
                f"{self.BASE_URL}/com.atproto.repo.createRecord",
                headers={
                    "Authorization": f"Bearer {access_token}"
                },
                json={
                    "repo": user_did,
                    "collection": "app.bsky.feed.post",
                    "record": {
                        "$type": "app.bsky.feed.post",
                        "text": message,
                        "createdAt": created_at
                    }
                }
            )

            if post_response.status_code != 200:
                raise Exception(
                    f"Bluesky Posting Error: {post_response.text}"
                )

            post_data = post_response.json()
            post_uri = post_data["uri"]
            post_id = post_uri.split("/")[-1]

            return {
                "platform": "Bluesky",
                "posted_url": (
                    f"https://bsky.app/profile/"
                    f"{self.handle}/post/{post_id}"
                ),
                "public_access": True,
                "date": now.strftime("%Y-%m-%d"),
                "time": now.strftime("%H:%M:%S")
            }
