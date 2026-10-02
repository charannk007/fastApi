import os
import asyncio

import asyncpg
from dotenv import load_dotenv

load_dotenv()


async def connect_db():
    connection = await asyncpg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    return connection


async def test_connection():
    connection = await connect_db()

    print("Connected to PostgreSQL successfully!")

    await connection.close()


asyncio.run(test_connection())