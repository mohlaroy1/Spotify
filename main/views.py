from rest_framework import generics
from .serializers import *

class SingerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class AlbumListCreateAPIView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongListAPIView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongViewSerializer

class SongCreateAPIView(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
