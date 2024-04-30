import requests
import celery
from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime

logger = get_task_logger(__name__)


@shared_task
def movie_update_every_two_hours():
    logger.info(f'update weather at : {datetime.now()}')
    return True
