from rest_framework import serializers
from .models import Artiste, Song, Lyrics

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["title", "release_date", "likes"]