from django.db import IntegrityError
from django.forms import ValidationError
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


# class ModelObjectidField(serializers.Field):
#     """
#         We use this when we are doing bulk create/update. Since multiple instances share
#         many of the same fk objects we validate and query the objects first, then modify the request data
#         with the fk objects. This allows us to pass the objects in to be validated.
#     """

#     def to_representation(self, value):
#         return value.id

#     def to_internal_value(self, data):
#         return data
    
# class BulkCreateListSerializer(serializers.ListSerializer):
#     def create(self, validated_data):
#         result = [self.child.create(attrs) for attrs in validated_data]

#         try:
#             self.child.Meta.model.objects.bulk_create(result)
#         except IntegrityError as e:
#             raise ValidationError(e)

        

#         return result


# class TodoSerializer(serializers.ModelSerializer):
    

#     project = ModelObjectidField()

#     def create(self, validated_data):
#         instance = TodoItem(**validated_data)

#         if isinstance(self._kwargs["data"], dict):
#             instance.save()

#         return instance
    
#     class Meta:
#         model = TodoItem
#         fields = "__all__"
#         list_serializer_class = BulkCreateListSerializer