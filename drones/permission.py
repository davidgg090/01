from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):

    @classmethod
    def has_object_permission(cls, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user
