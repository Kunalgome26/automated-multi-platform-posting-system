import asyncio
from app.platforms.discord import DiscordPlatform

async def main():
    discord = DiscordPlatform()
    print("Discord webhook loaded successfully!")
    print("Discord integration is ready.")

if __name__ == "__main__":
    asyncio.run(main())