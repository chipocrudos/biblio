from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

usermodel = get_user_model()


class EmployedSerializer(ModelSerializer):

    class Meta:
        model = usermodel
        fields = [
            'id',
            'first_name',
            'last_name',
        ]
