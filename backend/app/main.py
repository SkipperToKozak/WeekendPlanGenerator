from fastapi import FastAPI
from backend.app.routers import activities
from fastapi.middleware.cors import CORSMiddleware

# import requests

app = FastAPI()
app.include_router(activities.router, prefix="/activities", tags=["activities"])

# CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}





