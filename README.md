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
- Validation requiring exactly one valid HTTP or HTTPS URL.
- Independent publishing and error handling for each platform.
- Platform-wise success and failure responses.
- Returns post URLs when provided by the platform API.
- Reports public accessibility, date, time, and error details.
- Interactive API documentation through Swagger UI.

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
automated-multi-platform-posting-system/
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
├── test_validation.py
├── test_telegram.py
├── test_discord.py
├── test_slack.py
├── test_bluesky.py
├── test_mastodon.py
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kunalgome26/automated-multi-platform-posting-system.git
cd automated-multi-platform-posting-system
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

Create a `.env` file in the project root using `.env.example` as a reference.

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Add your own API credentials for all five platforms in the `.env` file.

**Important:** Never commit your actual `.env` file or expose API tokens, passwords, or webhook URLs.

### 5. Run the application

```bash
uvicorn app.main:app --reload --port 4000
```

The application will run at:

```text
http://127.0.0.1:4000
```

## API Usage

**Endpoint:** `POST /posting`

**Local URL:** `http://127.0.0.1:4000/posting`

### Sample Request

```json
{
  "message": "Check out my latest project! https://github.com/Kunalgome26"
}
```

### Sample Response

The following is an illustrative response showing one platform result. The actual API response contains results for all five platforms.

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
      "posted_url": "https://t.me/example/123",
      "public_access": true,
      "date": "2026-11-16",
      "time": "09:15:04",
      "error": null
    }
  ]
}
```

The response includes:

- Overall success status.
- Number of successful and failed platforms.
- Total number of platforms.
- Individual platform publishing status.
- Posted URL, when available.
- Public accessibility.
- Date and time.
- Error details, if publishing fails.

## API Documentation

After starting the server, open:

```text
http://127.0.0.1:4000/docs
```

Swagger UI allows you to interactively explore and test the API.

## Validation

The API validates incoming messages before attempting publication:

- Message cannot be empty.
- Message cannot exceed 200 characters.
- Exactly one valid HTTP or HTTPS URL must be included.

Invalid requests return HTTP `422 Unprocessable Content`.

## Error Handling

Each platform is processed independently. If publishing fails on one platform because of missing credentials or an API error, the system continues attempting to publish to the remaining platforms.

The response provides the status and error details for each platform.

## Testing

Run the message validation tests using:

```bash
python test_validation.py
```

The validation tests check empty messages, URL requirements, multiple URLs, invalid URLs, and the 200-character limit.

The individual platform test scripts require valid platform credentials. Running them may create actual social media posts.

## Security

- API credentials are stored in environment variables.
- `.env` is excluded from Git using `.gitignore`.
- `.env.example` contains placeholders only.
- Never upload access tokens, passwords, or webhook URLs to a public repository.

## Author

**Kunal Gome**

GitHub: https://github.com/Kunalgome26

**GitHub Repository:**  
https://github.com/Kunalgome26/automated-multi-platform-posting-system