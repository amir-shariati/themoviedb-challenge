from rest_framework import generics, views, filters
from .models import Movie
from .serializers import MovieSerializer


# Create your views here.
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


