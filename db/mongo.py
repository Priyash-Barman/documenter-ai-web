from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_URI, MONGO_DB

client = AsyncIOMotorClient(MONGO_URI)
mongo = client[MONGO_DB]
