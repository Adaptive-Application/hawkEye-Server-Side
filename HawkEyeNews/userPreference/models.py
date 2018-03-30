from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class category(models.Model):
    categoryName = models.CharField(max_length=20)
    categoryCode = models.CharField(max_length=10)

    def __str__(self):
        return self.categoryName


class subcategory(models.Model):
    category_FK = models.ForeignKey(category, on_delete=models.CASCADE)
    subcategoryName = models.CharField(max_length=20)
    subcategoryCode = models.CharField(max_length=10)

    def __str__(self):
        return self.subcategoryName


class userPreference(models.Model):

    userId = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    preferenceCode = models.CharField(max_length=10)
    preferenceScore = models.IntegerField(default=None)

    def __str__(self):
        return self.userId.username + " " + self.preferenceCode


class userSubPreference(models.Model):

    userpreference_FK = models.ForeignKey(userPreference, on_delete=models.CASCADE)
    subpreferenceCode = models.CharField(max_length=10)
    subpreferenceScore = models.IntegerField(default=None)

    def __str__(self):
        return  self.subpreferenceCode
