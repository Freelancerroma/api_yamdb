from rest_framework import viewsets
from reviews.models import Category, Genre, Title, Review
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    CommentSerializer
)
from django.shortcuts import render
from rest_framework import viewsets
from reviews.models import Review, Title
from .permissions import AdminModeratorAuthorReader
from django.shortcuts import get_object_or_404


class CategoryViewSet(viewsets.ModelViewSet):
    """Получение списка всех категорий."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    """Получение списка всех жанров."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    """Получение списка всех произведений."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """Обзоры viewset."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AdminModeratorAuthorReader,)

    def get_title(self):
        return get_object_or_404(Title, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.get_title().reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())


class CommentViewSet(viewsets.ModelViewSet):
    """Комментарии viewset."""

    serializer_class = CommentSerializer
    permission_classes = (AdminModeratorAuthorReader,)

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
