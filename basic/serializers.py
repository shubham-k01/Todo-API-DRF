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

    def create(self, validated_data):
        return super().create(validated_data)

class TodoCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    