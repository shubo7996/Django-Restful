from django.urls import path
from .api_views import SongsList,SongsDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('songs/', SongsList.as_view()),
    path('songs/<int:pk>/', SongsDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)


