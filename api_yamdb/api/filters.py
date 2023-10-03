from django_filters.rest_framework import (
    CharFilter,
    FilterSet,
)


class TitleFilter(FilterSet):
    """Фильтр для Title."""

    genre = CharFilter(field_name='genre__slug')
    category = CharFilter(field_name='category__slug')
    name = CharFilter(field_name='name', lookup_expr='icontains')
