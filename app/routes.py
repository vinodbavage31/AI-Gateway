from fastapi import APIRouter, HTTPException, Depends
from app.schemas import PromptRequest
from app.limiter import rate_limiter
from app.moderation import moderate
from app.llm_client import call_llm
from app.cache import get_cache, set_cache

router = APIRouter()

@router.post("/generate")
async def generate(
    request: PromptRequest,
    _=Depends(rate_limiter)         # run rate limiter before handler
):
    # Moderation check
    is_safe = await moderate(request.prompt)        # Guard layer
    if not is_safe:
        raise HTTPException(status_code=400, detail="Unsafe content")

    # Cache check
    cached = await get_cache(request.prompt)        # Performance optimization
    if cached:
        return {"success": True, "output": cached, "cached": True}

    # LLM Call
    try:
        output = await call_llm(request.prompt)     # Core business action
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "LLM service temporarily unavailable"
        }
    # Store in cache
    await set_cache(request.prompt, output)         # Write-through caching pattern

    return {"success": True, "output": output, "cached": False}