from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from middlewares.exception_handler import ExceptionHandlerMiddleware
from routes.register_routes import register_routes

app = FastAPI()

# Global Exception Handler Middleware
app.add_middleware(ExceptionHandlerMiddleware)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routes
register_routes(app)