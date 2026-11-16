
import re
from pydantic import BaseModel, Field, field_validator, HttpUrl


class PostingRequest(BaseModel):

    message: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Message with exactly one CTA URL"
    )

    @field_validator("message")
    @classmethod
    def validate_message(cls, value):

        value = value.strip()

        if not value:
            raise ValueError("Message cannot be empty")

        urls = re.findall(r"""https?://[^\s<>"']+""", value)

        if len(urls) != 1:
            raise ValueError("Exactly one URL must be included")

        try:
            parsed_url = HttpUrl(urls[0])

            if "." not in parsed_url.host:
                raise ValueError("Invalid URL")

        except Exception:
            raise ValueError("Invalid URL")

        return value
