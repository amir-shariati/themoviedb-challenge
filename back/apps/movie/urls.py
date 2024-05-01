from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import MovieListView, MovieRetrieveView

urlpatterns = [
    path('movie/', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>', MovieRetrieveView.as_view(), name='movie-detail'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
