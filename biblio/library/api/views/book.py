from rest_framework.viewsets import ModelViewSet

from ..serializers.book import Book, BookSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
