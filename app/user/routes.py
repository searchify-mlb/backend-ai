from fastapi import APIRouter, Request
from app.user.services import login
from app.user.schemas import LoginRequest
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/login")
async def user_login(login_request: LoginRequest, request: Request):
    email = login_request.email
    password = login_request.password
    app = request.app

    logger.info(f"email: {email}, password: {password}")

    token = await login(app, email, password)

    return {"message": "Login successful", "token": token}