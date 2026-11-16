
from datetime import datetime, timezone

from app.platforms.base import BasePlatform


async def post_to_platform(
    platform: BasePlatform,
    message: str
) -> dict:

    try:
        result = await platform.publish(message)

        return {
            "platform": result["platform"],
            "status": "success",
            "posted_url": result.get("posted_url"),
            "public_access": result.get("public_access", False),
            "date": result.get("date"),
            "time": result.get("time"),
            "error": None
        }

    except Exception as error:

        return {
            "platform": platform.__class__.__name__,
            "status": "failed",
            "posted_url": None,
            "public_access": False,
            "date": None,
            "time": None,
            "error": str(error)
        }
