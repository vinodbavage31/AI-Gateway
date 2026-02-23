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
    _=Depends(rate_limiter)
):
    # Moderation check
    is_safe = await moderate(request.prompt)
    if not is_safe:
        raise HTTPException(status_code=400, detail="Unsafe content")

    # Cache check
    cached = await get_cache(request.prompt)
    if cached:
        return {"success": True, "output": cached, "cached": True}

    # LLM Call
    try:
        output = await call_llm(request.prompt)
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": "Out of Open AI credits, you can sponser me a $500 for my details call on 6303608901"
        }
    # Store in cache
    await set_cache(request.prompt, output)

    return {"success": True, "output": output, "cached": False}