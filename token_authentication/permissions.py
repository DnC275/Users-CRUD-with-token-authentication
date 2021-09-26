from rest_framework import permissions


class UsersObservationPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj or request.user.is_staff)
