from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import *

router = DefaultRouter()
router.register('songs', SongViewSet)
router.register('albums', AlbumViewSet)
router.register('singers', SingerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('singer/', SingerListCreateAPIView.as_view()),
    #path('album/', AlbumListCreateAPIView.as_view()),
    #path('song/', SongListAPIView.as_view()),
    #path('song/add/', SongCreateAPIView.as_view()),
]
