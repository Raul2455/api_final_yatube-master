"""Этот модуль определяет модели для приложения "posts"."""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель, представляющая собой группу записей."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        """Возвращает строковое представление группы."""
        return str(self.title)


class Post(models.Model):
    """Модель, представляющая собой сообщение."""

    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name="posts", blank=True, null=True
    )

    def __str__(self):
        """Возвращает строковое представление записи."""
        return str(self.text)


class Comment(models.Model):
    """Модель, представляющая собой комментарий к записи."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """
    Модель, представляющая собой отношения.

    следования между пользователями.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        """Мета-параметры для следующей модели."""

        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='user_following')
        ]
