"""Permissions for users."""
from rest_framework import permissions

from .models import User


class IsAdmin(permissions.BasePermission):
    """Admin class permissions."""

    def has_permission(self, request, view):
        """Define admin permissions."""
        return (
            request.user.is_authenticated
            and request.user.role == User.ADMIN
            or request.user.is_superuser
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Reading permissions class."""

    def has_permission(self, request, view):
        """Define reading permissions."""
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.role == User.ADMIN
            or request.user.is_superuser
        )


class IsAdminOrModeratorOrAuthorOrReadOnly(permissions.BasePermission):
    """Editing permissions class."""

    def has_permission(self, request, view, obj):
        """Define editing permissions."""
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.role == User.ADMIN
            or request.user.is_authenticated
            and request.user.role == User.MODERATOR
        )
