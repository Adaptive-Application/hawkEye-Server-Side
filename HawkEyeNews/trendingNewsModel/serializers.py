from rest_framework import serializers

from .models import trendingNews


class trendingNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = trendingNews
        fields = '__all__'












