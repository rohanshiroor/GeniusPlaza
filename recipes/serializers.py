from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.Serializer):
    name = serializers.CharField()
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('name', instance.name)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance