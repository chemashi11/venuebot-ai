from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "venuebot_worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    imports=["app.services.reporting"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    broker_connection_retry_on_startup=True,
)

celery_app.conf.beat_schedule = {
    "generate-monthly-report-first-of-month": {
        "task": "app.services.reporting.generate_and_email_report",
        "schedule": crontab(minute=0, hour=2, day_of_month=1),
    },
}