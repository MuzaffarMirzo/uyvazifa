from rest_framework import serializers
from .models import Food, FoodType, Comment

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'