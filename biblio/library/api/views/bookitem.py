from rest_framework.viewsets import ModelViewSet

from ..serializers.bookitem import BookItem, BookItemSerializer


class BookItemViewset(ModelViewSet):
    serializer_class = BookItemSerializer
    queryset = BookItem.objects.all()
