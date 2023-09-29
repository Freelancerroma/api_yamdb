"""User class models."""
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Own user class for yamdb project."""

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]

    username = models.CharField(
        'username',
        max_length=256,
        blank=False,
        unique=True,
    )

    email = models.EmailField(
        'email',
        max_length=256,
        unique=True,
    )

    role = models.CharField(
        'role',
        max_length=256,
        choices=ROLES,
        default=USER,
    )

    bio = models.TextField(
        'biography',
        blank=True,
    )

    first_name = models.CharField(
        'name',
        max_length=256,
        blank=True,
    )

    last_name = models.CharField(
        'surname',
        max_length=256,
        blank=True,
    )

    REQUIRED_FIELDS = ('email',)

    def __str__(self) -> str:
        """Redifed string method for custom user class."""
        return self.username
