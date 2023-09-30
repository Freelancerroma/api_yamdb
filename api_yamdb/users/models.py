"""User class models."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


class User(AbstractUser):
    """Own user class for yamdb project."""

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    )

    username = models.CharField(
        'username',
        max_length=150,
        blank=False,
        unique=True,
    )

    email = models.EmailField(
        'email',
        max_length=254,
        unique=True,
    )

    role = models.CharField(
        'role',
        max_length=30,
        choices=ROLES,
        default=USER,
    )

    bio = models.TextField(
        'biography',
        blank=True,
    )

    first_name = models.CharField(
        'name',
        max_length=150,
        blank=True,
    )

    last_name = models.CharField(
        'surname',
        max_length=150,
        blank=True,
    )

    confirmation_code = models.CharField(
        max_length=150,
        default=get_random_string(length=15),
        editable=False,
    )

    REQUIRED_FIELDS = ('email',)

    def __str__(self) -> str:
        """Redifed string method for custom user class."""
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER
