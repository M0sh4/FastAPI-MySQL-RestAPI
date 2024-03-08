from fastapi import FastAPI 
from src.routes.user import user

app = FastAPI(
    title="CRUD FASTAPI",
    description="CRUD en FastAPI",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "user routes"
    }]
)

app.include_router(user)