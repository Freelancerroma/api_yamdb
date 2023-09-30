from rest_framework import mixins, viewsets


class GetListCreateDeleteMixin(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
):
    """Миксин для методов Get, List, Create, Delete."""

    pass
