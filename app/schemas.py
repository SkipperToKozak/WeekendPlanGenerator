from pydantic import BaseModel, Field

class ActivityBase(BaseModel):
    title: str = Field(min_length=2, max_length=30)
    description: str = Field(max_length=300)
    category: str = Field(min_length=2, max_length=30)
    duration: str = Field(min_length=2, max_length=30)
    mood: str = Field(min_length=2, max_length=30)
    weather: str = Field(min_length=2, max_length=30)
    budget: str = Field(min_length=2, max_length=30)
    people: str = Field(min_length=2, max_length=30)
