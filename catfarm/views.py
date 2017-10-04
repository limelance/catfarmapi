from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedOrCreate
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from .models import Cat
from .serializers import CatSerializer, UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    """
    Точки входа API для работы с котами
    """
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope)
    serializer_class = CatSerializer

    def get_queryset(self):
        """
        Фильтрация выдачи
        """
        return Cat.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Сохрание кота с указанием владельца
        """
        serializer.save(owner=self.request.user)


class UserSignUp(generics.CreateAPIView):
    """
    Точка входа для регистрации пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrCreate,)
