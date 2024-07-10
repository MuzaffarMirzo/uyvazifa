from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodViewSet, FoodTypeViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'foods', FoodViewSet)
router.register(r'foodtypes', FoodTypeViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]