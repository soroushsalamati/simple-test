from .models import *
from rest_framework.serializers import ModelSerializer


class PosterSerializer(ModelSerializer):
    class Meta:
        model = Poster
        fields = "__all__"


class PosterListSerializer(ModelSerializer):
    class Meta:
        model = Poster
        fields = ['id']


class PosterSerializer(ModelSerializer):
    class Meta:
        model = Poster
        fields = "__all__"
