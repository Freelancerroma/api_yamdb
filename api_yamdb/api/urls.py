from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    ReviewViewSet,
    CommentViewSet
)
from users.views import (
    APIAuthSignup,
    APIAuthToken,
    APIUserDetail,
    APIUserMe,
    UserViewSet
)

app_name = 'api'

v1_router = routers.DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')
v1_router.register('category', CategoryViewSet, basename='category')
v1_router.register('genre', GenreViewSet, basename='genre')
v1_router.register('title', TitleViewSet, basename='title')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/users/me/', APIUserMe.as_view()),
    path('v1/users/<str:username>/', APIUserDetail.as_view()),
    path('v1/auth/signup/', APIAuthSignup.as_view()),
    path('v1/auth/token/', APIAuthToken.as_view()),
]
