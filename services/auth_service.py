from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from schemas.user_schema import UserCreate
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


class AuthService:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

    def __init__(self, db):
        self.collection = db["users"]
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    async def create_user(self, user: UserCreate):
        user_dict = user.dict()
        user_dict["hashed_password"] = self.get_password_hash(user_dict.pop("password"))
        await self.collection.insert_one(user_dict)
        user_dict.pop("hashed_password")
        return user_dict

    async def authenticate_user(self, email: str, password: str):
        user = await self.collection.find_one({"email": email})
        if user and self.verify_password(password, user["hashed_password"]):
            return user
        return None

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = await self.collection.find_one({"email": email})
        if user is None:
            raise credentials_exception
        return user
