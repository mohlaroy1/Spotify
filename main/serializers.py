from datetime import timedelta

from rest_framework import serializers

from .models import Song, Album, Singer

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class AlbumForSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name', 'cover']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

    def validate_duration(self, duration):
        if duration >= timedelta(minutes=6):
            raise serializers.ValidationError("Song duration must be less than 6 minutes")
        return duration


class SongViewSerializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(slug_field='name', read_only=True)
    singer = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Song
        fields = "__all__"






