from datetime import datetime, timezone
from app.schemas import Job, JobCreate
from fastapi import FastAPI
from app.database import SQLDatabase

app = FastAPI()
db = SQLDatabase(
    user="plantation",
    password="worker",
    host="localhost",
    port=5432,
    db_name="chore_scheduler",
)

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.post("/jobs/", response_model=JobCreate)
async def create_job(job_input: JobCreate):
    job = Job(**job_input.model_dump())

    job.created_at = datetime.now(tz=timezone.utc)
    job.id = 1
    return job
