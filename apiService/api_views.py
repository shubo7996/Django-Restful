from .models import Songs
from .serializers import SongSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SongsList(APIView):
    
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

    def get_object(self,pk):

        try:
            return Songs.object.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        song = self.get_object(pk)
        serializer = SongSerializer(song,data=request.data)
        if serializer.is_valid():
            serializer.save()
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
