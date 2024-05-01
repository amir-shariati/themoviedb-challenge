from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import MovieListView, MovieRetrieveView

urlpatterns = [
    path('movie/', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>', MovieRetrieveView.as_view(), name='movie-detail'),

]
