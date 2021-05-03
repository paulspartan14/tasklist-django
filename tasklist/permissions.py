from rest_framework.permissions import BasePermission

# Has_permission es el defecto por base
# en has_object_permission entra despues de validar el permiso anterior

class UserPermission(BasePermission):
    """
    A base class from which all permission classes should inherit.
    """
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        # almacenar el usuario & id 
        user = request.user
        user_id = view.kwargs.get('pk')

        if request.method == 'POST':
            return user.groups.filter(name__in=['Admin', 'User'])

        # si el metodo es GET y no tiene un id y no tiene el rol 'Admin' no entra
        if request.method == 'GET' and not user_id:
            return user.groups.filter(name__in=['Admin'])

        return True

    def has_object_permission(self, request, view, obj): 
        """
        Return `True` if `has_permission` is `True` and object permission is granted, `False` otherwise.
        """

        return True 