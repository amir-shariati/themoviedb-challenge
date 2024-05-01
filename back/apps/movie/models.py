import datetime

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    adult = models.BooleanField(verbose_name=_('Adult'))
    backdrop_path = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Backdrop path'))

    movie_id = models.IntegerField(verbose_name=_('Movie id'))
    original_language = models.CharField(max_length=3, blank=True, null=True, verbose_name=_('Original language'))
    original_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Original title'))
    overview = models.TextField(verbose_name=_('Overview'))
    popularity = models.FloatField(verbose_name=_('Popularity'))
    poster_path = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Poster path'))
    release_date = models.CharField(max_length=12, blank=True, null=True, verbose_name=_('Release date'))
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Title'))
    video = models.BooleanField(verbose_name=_('Video'))
    vote_average = models.FloatField(verbose_name=_('Vote average'))
    vote_count = models.IntegerField(verbose_name=_('Vote count'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    def __str__(self):
        return f'title: {self.title} - updated_at: {self.updated_at}'

    class Meta:
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')
