import asyncio
from app.platforms.telegram import TelegramPlatform

async def main():
    print("Starting Telegram test...")

    try:
        telegram = TelegramPlatform()

        print("Telegram credentials loaded.")

        result = await telegram.publish(
            "Hello! Testing my Automated Posting System."
        )

        print("Telegram response:")
        print(result)

    except Exception as e:
        print("ERROR:", repr(e))

if __name__ == "__main__":
    asyncio.run(main())