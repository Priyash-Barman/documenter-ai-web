from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
import traceback

class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            # Optional: Log stack trace
            traceback.print_exc()
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"},
            )
