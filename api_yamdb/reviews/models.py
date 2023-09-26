from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


class Categories(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название категории')
    slug = models.SlugField(max_length=50,
                            unique=True,
                            verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название жанра')
    slug = models.SlugField(max_length=50,
                            unique=True,
                            verbose_name='Слаг')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название произведенеия')
    year = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1990),
                    MaxValueValidator(datetime.now().year)],
        verbose_name='Год выпуска произведения'
    )
    description = models.TextField(verbose_name='Описание произведения')
    genre = models.ManyToManyField(Genres, verbose_name='Жанр')
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='Категория')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=0)

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
