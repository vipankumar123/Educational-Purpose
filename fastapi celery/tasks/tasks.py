from datetime import datetime
from celery import Celery

# celery Configuration
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

# create Celery instance
celery = Celery(
    "tasks",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=["tasks.tasks"] 
)

# Example task registration
@celery.task(name="tasks.scheduled_task")
def scheduled_taskss(task_id: int, message: str):
    now = datetime.utcnow()
    print(f"Scheduled task {task_id} executed at {now}: {message}")
    
