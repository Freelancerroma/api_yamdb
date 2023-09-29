from django.urls import path, include
from rest_framework import routers
from .views import (
  CategoryViewSet,
  GenreViewSet,
  TitleViewSet,
  ReviewViewSet,
  CommentViewSet
)


app_name = 'api'

v1_router = routers.DefaultRouter()
v1_router.register('category', CategoryViewSet, basename='category')
v1_router.register('genre', GenreViewSet, basename='genre')
v1_router.register('title', TitleViewSet, basename='title')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
