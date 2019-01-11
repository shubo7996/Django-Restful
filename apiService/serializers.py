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
        kargs = {"password":
            {"write_only" : True
            }}

        def create(self,validated_data):
            username = validated_data['username']
            password = validated_data['password']
            email = validated_data['email']
            user_obj = User(
                username = username,
                email = email
            )
            user_obj.set_password(password)
            user_obj.save()
            return validated_data

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True,read_only=True)
    username = serializers.CharField()
    class Meta:
        model = User
        fields = ( 
            'username', 
            'password',
            'token'
            )
        kargs = {"password":
            {"write_only" : True
            }}

        def create(self,validated_data):
            username = validated_data['username']
            password = validated_data['password']
            email = validated_data['email']
            user_obj = User(
                username = username,
                email = email
            )
            user_obj.set_password(password)
            user_obj.save()
            return validated_data

class SongSerializer(serializers.ModelSerializer):

    #owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = models.Songs
        fields = (
            'title',
            'artist'
        )


