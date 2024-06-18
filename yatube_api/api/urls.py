"""Настройка URL-адреса для API."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='v1-posts')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='v1-comments'
)
router_v1.register('groups', GroupViewSet, basename='v1-groups')
router_v1.register('follow', FollowViewSet, basename='v1-follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
