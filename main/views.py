from rest_framework import generics
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


#class SingerListCreateAPIView(generics.ListCreateAPIView):
    #queryset = Singer.objects.all()
    #serializer_class = SingerSerializer

#class AlbumListCreateAPIView(generics.ListCreateAPIView):
    #queryset = Album.objects.all()
    #serializer_class = AlbumSerializer

#class SongListAPIView(generics.ListAPIView):
    #queryset = Song.objects.all()
    #serializer_class = SongViewSerializer

#class SongCreateAPIView(generics.CreateAPIView):
    #queryset = Song.objects.all()
    #serializer_class = SongSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @action(detail=True, methods=['get'])
    def songs(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        serializer = SongSerializer(album.songs.all(), many=True)
        return Response(serializer.data)


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SingerViewSet(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

    @action(detail=True, methods=['get'])
    def albums(self, request, pk):
        singer = get_object_or_404(Singer, pk=pk)
        serializer = AlbumSerializer(singer.albums.all(), many=True)
        return Response(serializer.data)


