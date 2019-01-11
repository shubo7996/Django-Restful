from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model

user = get_user_model()

#Custom Permission

class IsAuthenticatedAndOwner(BasePermission):
    message = 'You must be the owner of this object.'
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user