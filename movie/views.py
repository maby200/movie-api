from .models import Movie

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]