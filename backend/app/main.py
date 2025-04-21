from fastapi import FastAPI
from backend.app.routers import activities

# import requests

app = FastAPI()
app.include_router(activities.router, prefix="/activities", tags=["activities"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}





