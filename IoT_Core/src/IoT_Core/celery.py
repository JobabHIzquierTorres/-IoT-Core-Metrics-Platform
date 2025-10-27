import os

from celery import Celery
from kombu import Queue, Exchange

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IoT_Core.settings")

app = Celery("IoT_Core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# nodos
nodes = [
    "node-1",
    "node-2",
    "node-3",
    # "node-4",
]

# declarando las colas
CELERY_TASK_QUEUES = []
CELERY_BEAT_SCHEDULE = {}
for node in nodes:
    CELERY_TASK_QUEUES.append(
        Queue(node, Exchange(node), routing_key=node)
    )
    key = f"check-temp-{node}"
    CELERY_BEAT_SCHEDULE[key] = {
        "task": "sensors.tasks.measure_temp_task",
        "schedule": 3.0,  # Every 3 secs
        "options": {"queue": node},  # apply_async
    }

# worker
app.conf.task_queues = CELERY_TASK_QUEUES
# beat
app.conf.beat_schedule = CELERY_BEAT_SCHEDULE
