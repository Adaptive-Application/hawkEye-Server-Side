from django.db import models


class trendingNews(models.Model):
    newsTag = models.CharField(max_length=15)
    newsTagCode = models.CharField(max_length=10)
    newsUrl = models.CharField(max_length=500)
