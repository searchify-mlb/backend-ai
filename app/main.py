from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.connection import init_db
from app.user.routes import router as user_router
from app.search.routes import router as search_router
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

async def lifespan(app: FastAPI):
    async with init_db(app):
        yield

app = FastAPI(lifespan=init_db)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Open to all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router each domain
app.include_router(user_router)
app.include_router(search_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Project"}
