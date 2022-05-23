from rest_framework.serializers import ModelSerializer

from ...models import Book
from ..serializers.employed import EmployedSerializer


class BookBasicSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(BookBasicSerializer):
    user_data = EmployedSerializer(source='user', read_only=True)

    class Meta(BookBasicSerializer.Meta):
        extra_fields = ['user_data']
