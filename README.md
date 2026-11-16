# Automated Multi-Platform Posting System

## Project Overview
The Automated Multi-Platform Posting System is a Python-based application built using FastAPI. It allows users to publish a single message to multiple social media platforms through one API request.

The system integrates with five platforms:
- Telegram
- Discord
- Slack
- Bluesky
- Mastodon

## Features
- Single API endpoint for multi-platform publishing.
- Message validation with a maximum length of 200 characters.
- Validation requiring exactly one valid URL.
- Independent publishing and error handling for each platform.
- Platform-wise success and failure responses.
- Returns post URLs when provided by the platform API.
- Reports public accessibility, date, time, and error details.
- API documentation through Swagger UI.

## Technologies Used
- Python 3
- FastAPI
- Uvicorn
- Pydantic
- HTTPX
- Python-dotenv
- REST APIs

## Project Structure

```text
automated-posting/
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── config.py
│   ├── platforms/
│   │   ├── base.py
│   │   ├── telegram.py
│   │   ├── discord.py
│   │   ├── slack.py
│   │   ├── bluesky.py
│   │   └── mastodon.py
│   └── services/
│       └── posting_service.py
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd automated-posting
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file using `.env.example` as a reference.

Add your own API credentials for all five platforms. Never commit your actual `.env` file.

### 5. Run the application

```bash
uvicorn app.main:app --reload --port 4000
```

## API Usage

**Endpoint:** `POST /posting`

**Local URL:** `http://127.0.0.1:4000/posting`

### Sample Request

```json
{
  "message": "Check out my latest project! https://github.com/"
}
```

### Sample Response Structure

```json
{
  "success": true,
  "successful_platforms": 5,
  "failed_platforms": 0,
  "total_platforms": 5,
  "results": [
    {
      "platform": "Telegram",
      "status": "success",
      "posted_url": "https://example.com/post",
      "public_access": true,
      "date": "2026-11-16",
      "time": "12:00:00",
      "error": null
    }
  ]
}
```

The actual response contains an individual result for each platform.

## API Documentation

After starting the server, open:

`http://127.0.0.1:4000/docs`

Swagger UI allows you to test the API interactively.

## Error Handling

Each platform is processed independently. If one platform fails because of missing credentials or an API error, the system continues attempting to publish to the remaining platforms.

## Security

- API credentials are stored in environment variables.
- `.env` is excluded from Git using `.gitignore`.
- `.env.example` contains placeholders only.
- Never upload access tokens, passwords, or webhook URLs to a public repository.

## Author

Kunal Gome