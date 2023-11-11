from rest_framework import serializers
from .models import TodoItem

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = [
            'id',
            'title',
            'status'
        ]


class TodoCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    