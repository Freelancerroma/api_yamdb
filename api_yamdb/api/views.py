from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Category, Genre, Review, Title
from users.permissions import IsAdmin, IsModerator, IsUser, ReadOnly

from .mixins import GetListCreateDeleteMixin
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleViewSerializer, TitleWriteSerializer)


class CategoryViewSet(GetListCreateDeleteMixin):
    """Получение списка всех категорий."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (
        IsAdmin,
        ReadOnly,
    )
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(GetListCreateDeleteMixin):
    """Получение списка всех жанров."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (
        IsAdmin,
        ReadOnly,
    )


class TitleViewSet(viewsets.ModelViewSet):
    """Получение списка всех произведений."""

    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    )
    serializer_class = TitleViewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (
        IsAdmin,
        ReadOnly,
    )

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TitleViewSerializer
        return TitleWriteSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """Обзоры viewset."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (
        IsUser,
        IsModerator,
        IsAdmin,
        ReadOnly
    )

    def get_title(self):
        return get_object_or_404(Title, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.get_title().reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())


class CommentViewSet(viewsets.ModelViewSet):
    """Комментарии viewset."""

    serializer_class = CommentSerializer
    permission_classes = (
        IsUser,
        IsModerator,
        IsAdmin,
        ReadOnly
    )

    def get_review(self):
        return get_object_or_404(
            Review,
            id=self.kwars.get('review_id'),
            title=self.kwars.get('title_id')
        )

    def get_queryset(self):
        return self.get_review().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())
