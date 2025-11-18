from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    # overriden class from BasePermission
    # called after has_permission return True - view-level authentication
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permission is only allowed to the owner of the requested object
        return obj.owner == request.user
