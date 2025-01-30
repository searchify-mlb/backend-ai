from fastapi import APIRouter, Header
from app.search.services import search as search_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/{query}")
async def search(query: str, authorization: str = Header(...)):
    try:
        result = await search_service(query)

        return {"message": "Search successful", "result": result}
    except Exception as e:
        logger.error(f"An error occurred in search route: {e}")
        return {"message": "Search failed"}