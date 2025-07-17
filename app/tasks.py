from .worker import celery_app
import time
import random

@celery_app.task(name="run_python_job")
def run_python_job(job_name: str, duration : int = 5):
  print(f"[{job_name}] Started")
# scraping, parsing, training, emailing, etc .. to be continued
  time.sleep(duration)
  result = f"[{job_name}] 
  print(result)
  return result
