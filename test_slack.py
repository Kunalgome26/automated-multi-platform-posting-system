
import asyncio
from app.platforms.slack import SlackPlatform

async def main():
    print("Starting Slack test...")

    try:
        slack = SlackPlatform()
        print("Slack webhook loaded.")

        result = await slack.publish(
            "Hello! Testing my Automated Posting System."
        )

        print("Slack response:")
        print(result)

    except Exception as error:
        print("ERROR:", repr(error))


if __name__ == "__main__":
    asyncio.run(main())
