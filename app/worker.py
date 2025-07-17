from celery import Celery

celery_app = Celery(
  "worker",
  backend="redis://localhost:6379/0",
  broker="redis://localhost:6379/0"
)
