import httpx
import os
from dotenv import load_dotenv
from app.config import config

load_dotenv()           # Loads .env file into environment

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def call_llm(prompt: str):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": config["model"]["name"],
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": config["model"]["temperature"],
        "max_tokens": config["model"]["max_tokens"]
    }

    async with httpx.AsyncClient(timeout=config["model"]["timeout"]) as client:  # non-blocking, high concurrency, FastAPI compatible
        response = await client.post(url, headers=headers, json=payload)

        if response.status_code != 200:     # Error check
            raise Exception(response.text)

        data = response.json()
        return data["choices"][0]["message"]["content"]