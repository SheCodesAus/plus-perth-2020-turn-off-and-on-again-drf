from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(Self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.username == request.user
        

