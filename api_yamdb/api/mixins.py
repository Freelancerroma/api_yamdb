from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter


class GetListCreateDeleteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet для методов Get, List, Create, Delete."""

    filter_backends = (SearchFilter,)
    search_fields = ('name', )
    lookup_field = 'slug'


class GetPatchPostDeleteViewSet(viewsets.ModelViewSet):
    """ViewSet для запросов GET, PATCH, POST, DELETE."""

    http_method_names = ('get', 'patch', 'post', 'delete')
