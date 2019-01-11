from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

#class UserSerializer(serializers.ModelSerializer):
#    
#    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Songs.objects.all())

#    class Meta:
 #       model = User
 #       fields = (
 #           'id', 
 #           'username', 
 #           'snippets'
 #           )

class SongSerializer(serializers.ModelSerializer):

    #owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = models.Songs
        fields = (
            'title',
            'artist'
        )


