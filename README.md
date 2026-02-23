# AI Gateway

AI Gateway is a FastAPI-based backend service that acts as a gateway for interacting with Large Language Models (LLMs). It provides a clean API interface to send prompts and receive AI-generated responses.

This project is designed with proper structure, environment variable management, and production-ready practices.

---

## Features

- FastAPI-based REST API
- Async LLM integration
- Environment variable-based secret management
- Configurable model settings
- Clean project structure
- GitHub secret-safe setup

---

## Project Structure
```
ai_gateway/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── llm_client.py
│   └── config.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/AI-Gateway.git
cd AI-Gateway
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

> Make sure `.env` is listed in `.gitignore` and is never pushed to GitHub.
> You can use `.env.example` as a reference template.

---

## Running the Server

Start the FastAPI server with:
```bash
python -m uvicorn app.main:app --reload
```

Once running, open:
```
http://127.0.0.1:8000/docs
```

This opens the interactive Swagger UI where you can test the API.

---

## API Endpoint

### `POST /generate`

**Request Body:**
```json
{
  "prompt": "Your input text here"
}
```

**Response:**
```json
{
  "success": true,
  "output": "Generated response"
}
```

---

## Error Handling

The application:

- Handles external API failures
- Prevents secret exposure
- Returns structured error responses
- Avoids server crashes due to third-party failures

---

## Security Notes

- API keys are stored using environment variables
- `.env` is excluded from version control
- Leaked keys must be revoked immediately
- Secrets are never hardcoded in source files

---

## Future Improvements

- Add logging and monitoring
- Add Docker support
- Add rate limiting
- Add authentication layer
- Add CI/CD pipeline

---

## License

This project is for learning and development purposes.
