from rest_framework import serializers 
from . import models
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ( 
            'username', 
            'password',
            'email'
            )

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

        def validate(self,data):
            username = data.get("username")
            password = data.get("password")
            if not username:
                raise serializers.ValidationError("Username is required!")
            
            user = User.objects.filter(
                Q(username = username)
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



class SongSerializer(serializers.ModelSerializer):

    #owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = models.Songs
        fields = (
            'title',
            'artist'
        )


