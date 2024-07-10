from rest_framework import viewsets
from .models import Food, FoodType, Comment
from .serializers import FoodSerializer, FoodTypeSerializer, CommentSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
