from datetime import datetime
from app.schemas import Job, JobCreate

def test_job_create_schema():
    test_job = {
        "person": "LeBron",
        "task": "Mop kitchen floor",
        "time": "2024-10-01T10:00:00Z",
        "message": "Use the new mop",
    }

    job_creation = JobCreate(**test_job)
    assert job_creation.person == "LeBron"
    assert job_creation.task == "Mop kitchen floor"
    assert job_creation.time == datetime.fromisoformat("2024-10-01T10:00:00Z")
    assert job_creation.message == "Use the new mop"
