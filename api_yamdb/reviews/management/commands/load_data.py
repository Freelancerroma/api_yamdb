import csv

from django.conf import settings
from django.core.management import BaseCommand
from django.db.utils import IntegrityError

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

TABLES = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
}


# flake8: noqa: E303
class Command(BaseCommand):

    def handle(self, *args, kwargs):
        for model, csv_f in TABLES.items():
            with open(
                f'{settings.BASE_DIR}/static/data/{csv_f}',
                'r',
                encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                for data in reader:
                    print(data)
                    try:
                        if model == Category:
                            category = Category.objects.create(data)
                            category.save()
                        if model == Genre:
                            genre = Genre.objects.create(data)
                            genre.save()
                        if model == Title:
                            category_id = data.pop('category')
                            category = Category.objects.get(pk=category_id)
                            data['category'] = category
                            title = Title.objects.create(data)
                            title.save()
                        if model == Review:
                            author_id = data.pop('author')
                            author = User.objects.get(pk=author_id)
                            data['author'] = author
                            review = Review.objects.create(data)
                            review.save()
                        if model == Comment:
                            author_id = data.pop('author')
                            author = User.objects.get(pk=author_id)
                            data['author'] = author
                            comment = Comment.objects.create(data)
                            comment.save()
                        if model == User:
                            user = User.objects.create(**data)
                            user.save()
                    except IntegrityError:
                        self.stdout.write(self.style.WARNING(
                            'Запись уже существует'))
                    except Exception as ex:
                        print(ex)
        self.stdout.write(self.style.SUCCESS('Данные загружены'))
