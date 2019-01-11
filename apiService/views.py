from django.shortcuts import render
from .serializers import UserSerializer,UserLoginSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from .permissions import IsAuthenticatedAndOwner

#current_acive user 
User = get_user_model()


class UserCreateApiView(CreateAPIView):
#permission class set to Admin Users only
    permission_classes = [IsAdminUser,]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateLoginView(APIView):
#permission class set to Authenticated User or read Only
    permission_classes = [AllowAny,]
    serializer_class = UserLoginSerializer

"""
This Method contains the user to log in

"""
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)