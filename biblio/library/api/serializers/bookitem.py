from rest_framework.serializers import ModelSerializer

from ...models import BookItem
from .book import BookBasicSerializer
from .library import LibrarySerializer
from .rack import RackSerializer


class BookItemSerializer(ModelSerializer):

    library_data = LibrarySerializer(source='library', read_only=True)
    rack_data = RackSerializer(source='rack', read_only=True)
    book_data = BookBasicSerializer(source='book', read_only=True)

    class Meta:
        model = BookItem
        fields = '__all__'
        extra_fields = ['library_data', 'rack_data', 'book_data']
