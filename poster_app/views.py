from poster_app.models import Poster
from .serializers import PosterSerializer, PosterListSerializer
from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                     )



class Post(ListCreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer


class PostList(ListAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterListSerializer


class PostDetails(RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer