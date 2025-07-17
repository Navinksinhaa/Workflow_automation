from celery.result import AsyncResult
from app.worker import celery_app

@app.get("/status/{task_id}")
def get_task_status(task_id: str):
  res = AsyncResult(task_is, app = celery_app)
  return {
    "task_id": task_id,
    "status": res.status,
    "result": res.result
}
