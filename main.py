from fastapi import FastAPI
from backends import service

app = FastAPI()

# app.add_middleware()

app.include_router(service.router)
