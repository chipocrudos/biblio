from rest_framework.viewsets import ModelViewSet

from ..serializers.library import Library, LibrarySerializer


class LibraryViewSet(ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
