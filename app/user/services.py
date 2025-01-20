import logging
import jwt
import os
from datetime import datetime, timedelta, timezone
from app.user.repository import fetch_user_by_email_and_password
from typing import Optional
from fastapi import FastAPI

logger = logging.getLogger(__name__)

async def login(app: FastAPI,email: str, password: str) -> Optional[str]:
    try:
        user = await fetch_user_by_email_and_password(app, email, password)
        if user:
            logger.info(f"User with email: {email} logged in successfully.")

            current_time = datetime.now(timezone.utc)
            token_expiration = current_time + timedelta(minutes=float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))

            token_data = {
                "sub": email,
                "user_id": str(user["id"]),
                "exp": token_expiration.timestamp(),
            }

            token = jwt.encode(token_data, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))

            return token
        else:
            logger.warning(f"User with email: {email} not found.")
            return None
    except Exception as e:
        logger.error(f"An error occurred in login function: {str(e)}", exc_info=True)
        return None