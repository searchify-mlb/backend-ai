import logging
from app.machine_learning.src.app import search_videos, init_vector_store

logger = logging.getLogger(__name__)

async def search(query: str):
    try:
        vector_store = init_vector_store()

        result = search_videos(query, vector_store)

        return result
    except Exception as e:
        logger.error(f"An error occurred in search service: {e}")
        return None
