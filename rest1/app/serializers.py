from rest_framework import serializers

from app import models


# class ArticleSerializer(serializers.ModelSerializer):
#     tags = TagSerializer(many = True,read_only = True)

#     class meta:
#         model=models.Article
#         fields='__all__'

# class ItemSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=200)
#     price = serializers.FloatField()
#     quantity = serializers.IntegerField(required=False, default=1)

#     class Meta:
#         model = Item
#         fields = ('__all__')
from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
