from fastapi import FastAPI
from app.tasks import run_python_job
from uuid import uuid4

app = FastAPI()

@app.get("/")
def read_root():
  return {"msg": "Task Queue API is running"}

@app.post("/run-job")
def start_job(duration: int = 5):
  job_id = f"job-{uuid4().hex[:6]}"
  task = run_python_job.delay(job_id,duration)
  return {"job_id": job_id, "task_id": task.id}
