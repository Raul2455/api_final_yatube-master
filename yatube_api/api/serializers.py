"""Сериализаторы для API."""

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Follow, User, Group


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для Post модели."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        """Мета-класс для постсериализатора."""

        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.SlugRelatedField(
        read_only=True, slug_field='id'
    )

    class Meta:
        """Мета-класс для CommentSerializer."""

        model = Comment
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow."""

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following']
        )
    ]

    def validate(self, data):
        """Убедитесь, что пользователь не может следить за собой."""
        if self.context['request'].user == data.get('following'):
            raise serializers.ValidationError(
                'Нельзя подписаться на себя'
            )
        return data

    class Meta:
        """Мета-класс для FollowSerializer."""

        model = Follow
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        """Мета-класс для GroupSerializer."""

        model = Group
        fields = '__all__'
