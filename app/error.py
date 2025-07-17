@celery_app.task(bind=True, max_retries = 3)
def run_python_job(9self, job_name: str, duration: int = 5):
  try:
    if random.random() < 0.3:
      raise ValueError("Random failure")
    time.sleep(duration)
    return f"{job_name} done"
  except Exception as exc:
    raise self.retry(exc=exc, countdown=10)
