
import asyncio
from app.platforms.bluesky import BlueskyPlatform

async def main():
    print("Starting Bluesky test...")

    try:
        bluesky = BlueskyPlatform()
        print("Bluesky credentials loaded.")

        result = await bluesky.publish(
            "Hello! Testing my Automated Posting System."
        )

        print("Bluesky response:")
        print(result)

    except Exception as error:
        print("ERROR:", repr(error))


if __name__ == "__main__":
    asyncio.run(main())
