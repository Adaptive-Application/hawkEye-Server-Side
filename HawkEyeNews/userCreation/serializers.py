from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(max_length=30,
                                     validators=[UniqueValidator(queryset=User.objects.all())]
                                     )
    password = serializers.CharField(min_length=8, write_only=True)

    first_name = serializers.CharField(max_length=15)

    last_name = serializers.CharField(max_length=15)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        print(validated_data['first_name'], validated_data['last_name'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        return user
