from fastapi import HTTPException
from fastapi import APIRouter, Query
from sqlalchemy.orm import sessionmaker

from typing import List, Optional

from backend.app.models import engine, Activity

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

# User can provide many filters at once and many values for each filter
@router.get("/filtered")
async def get_activities_filtered(
    categories: Optional[List[str]] = Query(None, alias="category"),
    durations: Optional[List[str]] = Query(None, alias="duration"),
    moods: Optional[List[str]] = Query(None, alias="mood"),
    budgets: Optional[List[str]] = Query(None, alias="budget"),
    people: Optional[List[str]] = Query(None, alias="people"),
    weathers: Optional[List[str]] = Query(None, alias="weather")
):
    query = session.query(Activity)

    if categories:
        query = query.filter(Activity.category.in_(categories))
    if durations:
        query = query.filter(Activity.duration.in_(durations))
    if moods:
        query = query.filter(Activity.mood.in_(moods))
    if budgets:
        query = query.filter(Activity.budget.in_(budgets))
    if people:
        query = query.filter(Activity.people.in_(people))
    if weathers:
        query = query.filter(Activity.weather.in_(weathers))

    return query.all()
#TODO What if there is no activity that matches the filters?