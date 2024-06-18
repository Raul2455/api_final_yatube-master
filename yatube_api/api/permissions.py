"""
Этот модуль содержит пользовательские.

разрешения для приложения 'api'.
"""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    Разрешение, позволяющее только автору объекта изменять его.

    Остальные пользователи могут только просматривать.
    """

    def has_object_permission(self, request, view, obj):
        """
        Проверяет, имеет ли пользователь разрешение.

        на выполнение запроса с объектом.
        """
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
