
from fastapi import FastAPI

from app.schemas import PostingRequest
from app.platforms.telegram import TelegramPlatform
from app.platforms.discord import DiscordPlatform
from app.platforms.slack import SlackPlatform
from app.platforms.bluesky import BlueskyPlatform
from app.platforms.mastodon import MastodonPlatform

from app.services.posting_service import post_to_platform

app = FastAPI(
    title="Automated Multi-Platform Posting System",
    description="Publish one message across five social platforms.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Automated Posting API is running!"}


@app.post("/posting")
async def create_post(request: PostingRequest):

    platform_factories = [
        ("Telegram", TelegramPlatform),
        ("Discord", DiscordPlatform),
        ("Slack", SlackPlatform),
        ("Bluesky", BlueskyPlatform),
        ("Mastodon", MastodonPlatform)
    ]

    results = []

    for name, factory in platform_factories:
        try:
            platform = factory()
            result = await post_to_platform(platform, request.message)

        except Exception as error:
            result = {
                "platform": name,
                "status": "failed",
                "posted_url": None,
                "public_access": False,
                "date": None,
                "time": None,
                "error": str(error)
            }

        results.append(result)

    successful = sum(
        result["status"] == "success" for result in results
    )

    return {
        "success": successful > 0,
        "successful_platforms": successful,
        "failed_platforms": len(results) - successful,
        "total_platforms": len(results),
        "results": results
    }
