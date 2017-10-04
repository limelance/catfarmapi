from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    """
    Сериализатор кота
    """
    class Meta:
        model = Cat
        fields = ('id', 'name', 'breed', 'age', 'hairiness')

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователей
    """
    class Meta:
        model = User
        fields = ('username', 'password')
