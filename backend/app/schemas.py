from datetime import datetime
from pydantic import BaseModel


class JobCreate(BaseModel):
    person: str
    task: str
    time: datetime
    message: str | None = None  # Optional field


class Job(JobCreate):
    id: int
    created_at: datetime
