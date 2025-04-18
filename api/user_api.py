from fastapi import APIRouter, HTTPException
from schemas.user_schema import UserSchema
from services import services

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=str)
async def create_user(user: UserSchema):
    return await services.user_service.create_user(user)

@router.get("/{user_id}", response_model=UserSchema)
async def get_user(user_id: str):
    user = await services.user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserSchema(**user)

@router.get("/", response_model=list[UserSchema])
async def list_users():
    return await services.user_service.list_users()

@router.put("/{user_id}", response_model=UserSchema)
async def update_user(user_id: str, user: UserSchema):
    updated = await services.user_service.update_user(user_id, user.dict(exclude_unset=True))
    return UserSchema(**updated)

@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    deleted = await services.user_service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": True}
