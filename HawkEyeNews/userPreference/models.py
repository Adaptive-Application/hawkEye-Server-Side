from django.db import models

# Create your models here.


class userPreference(models.Model):

    preferenceName = models.CharField(max_length=15)
    preferenceScore = models.IntegerField(default=None)

    def __str__(self):
        return self.preferenceName


class userSubPreference(models.Model):

    userpreference_FK = models.ForeignKey(userPreference, on_delete=models.CASCADE)
    subpreferenceName = models.CharField(max_length=15)
    subpreferenceScore = models.IntegerField(default=None)