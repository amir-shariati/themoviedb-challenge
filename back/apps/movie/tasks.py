import requests
import celery
from celery import shared_task
from celery.utils.log import get_task_logger
from datetime import datetime
from typing import TypedDict, List
from django.conf import settings
from .models import Movie

logger = get_task_logger(__name__)


class MovieResponseType(TypedDict):
    adult: bool
    backdrop_path: str
    # genre_ids: List[int]
    movie_id: int
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    release_date: str
    title: str
    video: bool
    vote_average: float
    vote_count: str


@shared_task
def movie_update_every_two_hours():
    logger.info(f'update weather at : {datetime.now()}')
    return True
