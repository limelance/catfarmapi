from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    """
    API END points
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
