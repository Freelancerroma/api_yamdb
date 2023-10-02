from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter


class GetListCreateDeleteMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Миксин для методов Get, List, Create, Delete."""

    filter_backends = (SearchFilter,)
    search_fields = ('name', )
    lookup_field = 'slug'
