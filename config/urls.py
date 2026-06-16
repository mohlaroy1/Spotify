from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singer/', SingerListCreateAPIView.as_view()),
    path('album/', AlbumListCreateAPIView.as_view()),
    path('song/', SongListAPIView.as_view()),
    path('song/add/', SongCreateAPIView.as_view()),
]
