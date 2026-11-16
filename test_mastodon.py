
import asyncio
from app.platforms.mastodon import MastodonPlatform

async def main():
    print("Starting Mastodon test...")

    try:
        mastodon = MastodonPlatform()
        print("Mastodon credentials loaded.")

        result = await mastodon.publish(
            "Hello! Testing my Automated Posting System."
        )

        print("Mastodon response:")
        print(result)

    except Exception as error:
        print("ERROR:", repr(error))


if __name__ == "__main__":
    asyncio.run(main())
