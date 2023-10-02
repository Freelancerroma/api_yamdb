from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категорий."""

    class Meta:
        model = Category
        fields = ('name', 'slug',)
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор жанров."""

    class Meta:
        model = Genre
        fields = ('name', 'slug',)
        lookup_field = 'slug'


class TitleReadSerializer(serializers.ModelSerializer):
    """Сериализатор произведений для отображения."""

    genre = GenreSerializer(
        many=True,
        read_only=True,
    )
    category = CategorySerializer(
        read_only=True,
    )
    rating = serializers.IntegerField(
        read_only=True,
    )

    class Meta:
        model = Title
        fields = '__all__'


class TitleWriteSerializer(serializers.ModelSerializer):
    """Сериализатор произведений для создания."""

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        slug_field='slug',
    )

    class Meta:
        model = Title
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """Отзывы serializers."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )

    def validate(self, data):
        author = self.context.get('request').user
        title_id = self.context.get('view').kwargs.get('title_id')
        if (
            self.context.get('request').method == 'POST'
            and Review.objects.filter(
                author=author,
                title__id=title_id
            ).exists()
        ):
            raise serializers.ValidationError(
                'Можно написать только один обзор к произведению'
            )
        return data

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date',)


class CommentSerializer(serializers.ModelSerializer):
    """Комментарии serializer."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date',)
