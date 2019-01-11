from django.urls import path
from .api_views import SongsList,SongsDetail
from .views import UserCreateApiView,UserCreateLoginView
from rest_framework.urlpatterns import format_suffix_patterns

#routers 

urlpatterns = [
    #redirects to api/songs 
    path('songs/', SongsList.as_view()),
    #redirects to api/songs/(1..n)
    path('songs/<int:pk>/', SongsDetail.as_view()),
    #redirects to api/user/register
    path('users/register/', UserCreateApiView.as_view()) ,
    #redirects to api/users/login
    path('users/login',UserCreateLoginView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)


