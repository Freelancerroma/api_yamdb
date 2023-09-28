from django.urls import include, path
from rest_framework import routers

from .views import ReviewViewSet, CommentViewSet

v1_router = routers.DefaultRouter()
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]