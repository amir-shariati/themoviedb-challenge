from django.apps import AppConfig


class MovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.movie'

    def ready(self):
        from .tasks import one_time_app_startup_task
        if not settings.TASK_START_UP_ALREADY_RUN and settings.DOCKER_BACKEND_SERVER:
            one_time_app_startup_task.delay()
            settings.TASK_START_UP_ALREADY_RUN = True
