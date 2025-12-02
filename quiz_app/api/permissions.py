from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Custom permission to allow access only to the owner of the object."""


    message = "You must be the owner of this object."
    

    def has_object_permission(self, request, view, obj):
        """Check if the user have permission to the object."""


        return obj.owner == request.user