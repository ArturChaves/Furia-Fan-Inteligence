from celery import Celery
from ml.segmenter import run_pipeline
import os

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "pyamqp://guest@rabbitmq//")

app = Celery('etl', broker=CELERY_BROKER_URL)

@app.task(bind=True, max_retries=3)
def clustering_task(self):
    try:
        run_pipeline()
    except Exception as exc:
        self.retry(exc=exc, countdown=60) 