from fastapi import FastAPI
from app.db.connection import init_db
from app.user.routes import router as user_router
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

async def lifespan(app: FastAPI):
    async with init_db(app):
        yield

app = FastAPI(lifespan=init_db)

# Include the router each domain
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Project"}
