from .models import Songs
from .serializers import SongSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAuthenticatedAndOwner
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)


class SongsList(APIView):
    
    #pemission class object inherited from the rest framework's permission class
    permission_classes=[IsAuthenticatedAndOwner,IsAdminUser,]

    #just in ordr to make the inputs in HTML format
    serializer_class = SongSerializer

    """
        This Contains The GET and POST method for making the api

    """

    def get(self,request,format=None):
        queryset = Songs.objects.all()
        serializer_class = SongSerializer(queryset,many=True)
        return Response(serializer_class.data)

    def post(self,request,format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

           
class SongsDetail(APIView):

    
    #we have met before
    serializer_class = SongSerializer


    #you know what i am talking about
    permission_classes = [IsAuthenticatedAndOwner,]


    """

    This contains the READ,UPDATE,DESTROY method for the api

    """

    def get_object(self,pk):

        try:
            return Songs.objects.get(pk=pk)
        except Songs.DoesNotExist :
            raise Http404

    def get(self,request,pk,format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        song = self.get_object(pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


