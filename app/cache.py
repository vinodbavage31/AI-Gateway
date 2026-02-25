import hashlib

cache_store = {}        # In-memory dictionary cache, Fast but temporary

def generate_key(prompt: str):
    return hashlib.sha256(prompt.encode()).hexdigest()  # fixed length, avoids huge keys, avoids special char issues

async def get_cache(prompt: str):
    key = generate_key(prompt)
    return cache_store.get(key)

async def set_cache(prompt: str, value: str):
    key = generate_key(prompt)
    cache_store[key] = value