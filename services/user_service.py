from schemas.user_schema import UserSchema
from bson import ObjectId

class UserService:
    def __init__(self, db):
        self.collection = db["users"]

    async def create_user(self, user: UserSchema):
        result = await self.collection.insert_one(user.dict(by_alias=True, exclude={"id"}))
        return str(result.inserted_id)

    async def get_user(self, user_id: str):
        return await self.collection.find_one({"_id": ObjectId(user_id)})

    async def list_users(self):
        cursor = self.collection.find()
        return [UserSchema(**doc) async for doc in cursor]

    async def update_user(self, user_id: str, user_data: dict):
        await self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_data})
        return await self.get_user(user_id)

    async def delete_user(self, user_id: str):
        result = await self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
