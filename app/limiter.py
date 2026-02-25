from collections import defaultdict
from time import time
from fastapi import Request, HTTPException
from app.config import config

request_log = defaultdict(list)             #Creates dictionary where missing keys auto-create empty list.

async def rate_limiter(request: Request):
    client_ip = request.client.host
    current_time = time()                   # Gets current Unix timestamp.

    window = config["rate_limit"]["window"]     #Pulls settings from config.
    limit = config["rate_limit"]["requests"]    #Pulls settings from config.

    request_log[client_ip] = [                  #removes old timestamps, keeps only recent ones, This is sliding window algorithm.
        t for t in request_log[client_ip]       
        if current_time - t < window
    ]

    if len(request_log[client_ip]) >= limit:    #If too many requests → block.
        raise HTTPException(status_code=429, detail="Rate limit exceeded")  #429 = Too Many Requests.

    request_log[client_ip].append(current_time)