
from app.schemas import PostingRequest

tests = [
    ("Valid", "Check this out https://example.com"),
    ("Empty", ""),
    ("No URL", "Hello everyone"),
    ("Two URLs", "Visit https://example.com and https://google.com"),
    ("Invalid URL", "Visit https://invalid"),
    ("Too long", "A" * 201)
]

for name, message in tests:
    try:
        PostingRequest(message=message)
        print(name, "ACCEPTED")
    except Exception:
        print(name, "REJECTED")
