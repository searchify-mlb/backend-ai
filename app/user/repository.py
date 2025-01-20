from app.db.connection import get_db_pool
import logging
from asyncpg import PostgresError
from fastapi import FastAPI

logger = logging.getLogger(__name__)

async def fetch_user_by_email_and_password(app: FastAPI, email: str, password: str):
    query = """
    SELECT * FROM users
    WHERE email = $1 and password = $2 
    """
    pool = get_db_pool(app)
    try:
        async with pool.acquire() as conn:
            result = await conn.fetchrow(query, email, password)
            if result:
                return dict(result)
            else:
                logger.info(f"No user found for email: {email}")
                return None
    except PostgresError as e:
        logger.error(f"Database error occurred: {e}")
        return None
    except Exception as e:
        logger.error(f"An error occurred repository: {e}")
        return None