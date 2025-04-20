from fastapi import HTTPException
from fastapi import APIRouter
from requests import Session
from sqlalchemy.orm import sessionmaker

from app.models import engine, Activity

router = APIRouter()

Session = sessionmaker(bind=engine)
session = Session()




@router.get("/")
async def get_activities():
    return {"activities": ["running", "swimming", "cycling"]}

@router.get("/id/{activity_id}")
async def get_activity(activity_id: int):
    activities = ["running", "swimming", "cycling"]
    if activity_id < 0 or activity_id >= len(activities):
        raise HTTPException(
            status_code=404,
            detail=f"Activity {activity_id} not found"
        )
    return {"activity": activities[activity_id]}
@router.get("/filtered")
async def get_activities_filtered():
    query = session.query(Activity)

    # if "category" in filters:
    #     query = query.filter(Activity.category.in_(filters["category"]))
    # if "budget" in filters:
    #     query = query.filter(Activity.budget.in_(filters["budget"]))
    # if "weather" in filters:
    #     query = query.filter(Activity.weather == filters["weather"])
    # if "mood" in filters:
    #     query = query.filter(Activity.mood == filters["mood"])
    # if "people" in filters:
    #     query = query.filter(Activity.people == filters["people"])

    return query.all()