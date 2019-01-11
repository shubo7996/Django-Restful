from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 
            'username', 
            'password',
            'email'
            )

class SongSerializer(serializers.ModelSerializer):

    #owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = models.Songs
        fields = (
            'title',
            'artist'
        )


