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
        logger.info(f'one_time_app_startup_task, total_pages: {total_pages}, total_results: {total_results}')
        for page in range(total_pages + 1):
            movie_fetch_data.delay(page)
    else:
        logger.info(f'one_time_app_startup_task, res_json: {res_json}')


@shared_task
def movie_update_every_two_hours():
    logger.info(f'update weather at : {datetime.now()}')
    return True
def movie_fetch_data(page=1):
    st_date = '2024-04-01'
    en_date = '2024-04-02'
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
    results: List[MovieResponseType] = res_json.get('results')

    movie_data: MovieResponseType = dict()
    if response.status_code == 200:
        for movie in results:
            movie_data['adult'] = movie.get('adult')
            movie_data['backdrop_path'] = movie.get('backdrop_path')
            # movie_data['genre_ids'] = movie.get('genre_ids')
            movie_data['movie_id'] = movie.get('id')
            movie_data['original_language'] = movie.get('original_language')
            movie_data['original_title'] = movie.get('original_title')
            movie_data['overview'] = movie.get('overview')
            movie_data['popularity'] = movie.get('popularity')
            movie_data['poster_path'] = movie.get('poster_path')
            movie_data['release_date'] = movie.get('release_date')
            movie_data['title'] = movie.get('title')
            movie_data['video'] = movie.get('video')
            movie_data['vote_average'] = movie.get('vote_average')
            movie_data['vote_count'] = movie.get('vote_count')

            movie_persist_data_to_db(movie_data)


