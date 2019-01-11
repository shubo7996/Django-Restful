from rest_framework import serializers 
from . import models
from django.contrib.auth import get_user_model
from django.db.models import Q

# Current Active User
User = get_user_model()

#Serializer Class for the current active user 
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 
            'username', 
            'password',
            'email'
            )
"""

This Method contains Validation of User Input Data

"""

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

#Serializer for the User' Login model
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
"""
Method for the Validation of input data for Login

"""

    def validate(self,data):
        username = data.get("username")
        password = data.get("password")
        if not username:
            raise serializers.ValidationError("Username is required!")
            
        user = User.objects.filter(
            Q(username = username)|
            Q(password = password)
            ).distinct()
            
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This username is not valid!")
            
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Incorrect Password")
            
        data['token'] = "random"
            
        return data


#Serializer Class for Song model
class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Songs
        fields = (
            'title',
            'artist'
        )


