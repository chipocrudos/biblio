from django.contrib.auth.models import Group
from rest_framework import serializers
from users.models import UserProfile


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    groups_data = GroupSerializer(source='groups', many=True, read_only=True)

    class Meta:
        model = UserProfile

        fields = [
            'id',
            'email',
            'first_name',
            'phone',
            'password',
            'last_name',
            'is_active',
            'is_superuser',
            'groups',
            'groups_data'
        ]
