from fastapi import FastAPI, HTTPException
# import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/activities")
async def get_activities():
    return {"activities": ["running", "swimming", "cycling"]}

@app.get("/activities/{activity_id}")
async def get_activity(activity_id: int):
    activities = ["running", "swimming", "cycling"]
    if activity_id < 0 or activity_id >= len(activities):
        raise HTTPException(
            status_code=404,
            detail=f"Activity {activity_id} not found"
        )
    return {"activity": activities[activity_id]}

