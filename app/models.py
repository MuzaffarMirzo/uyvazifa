from django.db import models
from django.contrib.auth.models import User


class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tarkibi = models.TextField()
    narxi = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text