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


@shared_task()
def one_time_app_startup_task():
    logger.info('one_time_app_startup_task, this task call after app is up')
    st_date = '2024-04-01'
    en_date = '2024-04-02'
    page = 1
    headers = {'Authorization': f'Bearer {settings.THEMOVIEDB_API_KEY}'}
    payload = {
        'include_adult': 'false',
        'include_video': 'false',
        'language': 'en-US',
        'page': page,
        'release_date.gte': st_date,
        'release_date.lte': en_date,
        'sort_by': 'popularity.desc',
    }

    with requests.Session() as session:
        response = session.get(
            url=f'https://api.themoviedb.org/3/discover/movie',
            params=payload,
            headers=headers
        )

    res_json = response.json()
    total_pages = res_json.get('total_pages')
    total_results = res_json.get('total_results')

    if total_pages is not None:
        for page in range(total_pages + 1):
            movie_fetch_data.delay(page)
    else:
        logger.info(f'one_time_app_startup_task, res_json: {res_json}')


@shared_task
def movie_update_every_two_hours():
    logger.info(f'update weather at : {datetime.now()}')
    return True
