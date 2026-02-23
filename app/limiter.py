from collections import defaultdict
from time import time
from fastapi import Request, HTTPException
from app.config import config

request_log = defaultdict(list)

async def rate_limiter(request: Request):
    client_ip = request.client.host
    current_time = time()

    window = config["rate_limit"]["window"]
    limit = config["rate_limit"]["requests"]

    request_log[client_ip] = [
        t for t in request_log[client_ip]
        if current_time - t < window
    ]

    if len(request_log[client_ip]) >= limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    request_log[client_ip].append(current_time)