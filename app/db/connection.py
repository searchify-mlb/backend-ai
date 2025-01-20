import asyncpg
from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

@asynccontextmanager
async def init_db(app: FastAPI):
    app.state.db = await asyncpg.create_pool(
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        host=DB_HOST,
        port=DB_PORT,
    )
    print("Database connection pool created.")
    yield
    await app.state.db.close()
    print("Database connection pool closed.")

def get_db_pool(app: FastAPI):
    return app.state.db
